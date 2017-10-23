# -*- coding: utf-8 -*-l
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
from __future__ import absolute_import, print_function, unicode_literals

import requests
import xmltodict
import six
import pyxb
import os
from requests.auth import HTTPBasicAuth
from vantivsdk import (fields_chargeback, utils, dict2obj)


package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
conf = utils.Configuration()
home_dir = os.environ['HOME']


def _get_response(parameter_value, parameter_key):
    """ generate response with request method  get
    :param parameter_value: the parameter value to be appended in url
    :param parameter_key: the paramater to be appended in url
    :return: returns the response received
    """
    url = conf.url
    try:
        if parameter_key != "":
            url = url  + "?"
            parameter_key = parameter_key + "="
        request = url + parameter_key + str(parameter_value)
        http_response = requests.get(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    # print("URL :", )
    print("Request : ", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')
    return response


def _get_responses(parameter_value1, parameter_key1, parameter_value2, parameter_key2):
    """ generate response with multiple parameters with request method  get
    :param parameter_value1:  the parameter value to be appended in url
    :param parameter_key1: the paramater to be appended in url
    :param parameter_value2: the parameter value to be appended in url
    :param parameter_key2: the paramater to be appended in url
    :return:
    """

    if parameter_key1 != "":
        url = conf.url + "?"
        parameter_key1 = parameter_key1 + "="
        parameter_key2 = parameter_key2 + "="

    try:
        request = url + parameter_key1 + str(parameter_value1) + "&" + parameter_key2 + str(parameter_value2)
        http_response = requests.get(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("Request :", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


def _create_request_xml(request_body):
    """ Create xml string from request object
    :param request_body: request_body
    :return: XML string
    """
    request_xml = utils.obj_to_xml(request_body)

    if conf.print_xml:
        print('Request XML:\n', request_xml.decode('utf-8'), '\n')

    return request_xml


def _check_response(response):
    """check the status code of the response
    :param response: http response generated
    :return: raises an exception
    """

    if response.status_code != 200:
        raise utils.VantivException("Error with Https Response, Status code: ", response.status_code)

    # Check empty response
    if not response:
        raise utils.VantivException("The response is empty, Please call Vantiv eCommerce")


def _check_response_dict(response, return_format='dict'):
    """ check the response format
    :param response: http response generated
    :param return_format:
    :return: raises an Exception
    """
    skip = False
    if response.text.__contains__('chargebackUpdateResponse'):
        response_dict = xmltodict.parse(response.text)['chargebackUpdateResponse']
    elif response.text.__contains__('chargebackRetrievalResponse'):
        response_dict = xmltodict.parse(response.text)['chargebackRetrievalResponse']
    elif response.text.__contains__('Merchant'):
        response_dict = xmltodict.parse(response.text)['Merchant']
    else:
        skip = True

    if not skip:
        if response_dict['@xmlns'] != "":
            return_f_l = return_format.lower()
            if return_f_l == 'xml':
                response_xml = response.text
                return response_xml
            elif return_f_l == 'object':
                return fields_chargeback.CreateFromDocument(response.text)
            else:
                if conf.print_xml:
                    import json
                    print('Response Dict:\n', json.dumps(response_dict, indent=4), '\n\n')
                    return response_dict
        else:
            raise utils.VantivException("Invalid Format")
    else:
        with open(package_root+'/samples/doc.pdf', 'wb') as f:
            f.write(response.content)


def _put_responses(parameter_value1, request_body):
    """ generate response with request method  put
    :param parameter_value1: the parameter value to be appended in url
    :param request_body: the input object for the xml
    :return: return the response generated
    """

    try:
        request = conf.url + str(parameter_value1)
        http_response = requests.put(request, headers={"Content-Type": "application/com.vantivcnp.services-v2+xml", "Accept": "application/com.vantivcnp.services-v2+xml"},
                                     auth=HTTPBasicAuth(conf.user, conf.password),
                                     data=_create_request_xml(request_body))
        print("Request :", request)
        print("Response :", http_response)
        _check_response(http_response)
        response = _check_response_dict(http_response, return_format='dict')
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def _get_document_response(parameter_value1, parameter_value2):
    """ generate response with multiple parameters with request method  get
    :param parameter_value1:  the parameter value to be appended in url
    :param parameter_value2: the parameter value to be appended in url
    :return:
    """

    url = conf.url + "documents/"

    try:

        request = url + str(parameter_value1) + "/" + str(parameter_value2)
        http_response = requests.get(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("Request: ", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


def _get_document_responses(parameter_value1, parameter_value2, parameter_value3):

    url = conf.url + "documents/"
    try:
        request = url + str(parameter_value1) + "/" + str(parameter_value2) + "/" + str(parameter_value3)
        http_response = requests.get(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print(requests)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


def _delete_document_response(parameter_value1, parameter_value2, parameter_value3):
    url = conf.url + "documents/"

    try:
        request = url + str(parameter_value1) + "/" + str(parameter_value2) + "/" + str(parameter_value3)
        http_response = requests.delete(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print(requests)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


# def _upload_document_response(parameter_value1, parameter_value2, parameter_value3, file_type, extension):
#     conf.url = conf.url + "documents/"
#     file = open(package_root+"/samples/000_puppy_picture.jpg", 'rb').read()
#     try:
#         http_response = requests.post(conf.url + str(parameter_value1) + "/" + str(parameter_value2) + "/" + str(parameter_value3),
#                                      data=file,
#                                      headers={"Content-Type": file_type+"/"+extension},
#                                      auth=HTTPBasicAuth(conf.user, conf.password))
#
#     except requests.RequestException:
#         raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
#
#     print(requests)
#     print("Response :", http_response)
#     _check_response(http_response)
#     response = _check_response_dict(http_response, return_format='dict')
#
#     return response


"""
Functions for the different combinations of get and put requests
"""


def _post_responses(param, param1, param2, data, headertype):

    url = conf.url + "documents/" + param + "/" + param1 + "/" + param2
    try:
        http_response = requests.post(url=url,
                                      headers={"Content-Type": headertype },
                                      auth=HTTPBasicAuth(conf.user, conf.password), data=data)
        print("Request :", requests)
        print("Response :", http_response)
        _check_response(http_response)
        response = _check_response_dict(http_response, return_format='dict')
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def _put_response_upload(param, param1, param2, data, headertype):

    url = conf.url + "documents/" + param + "/" + param1 + "/" + param2
    try:
        http_response = requests.put(url=url,
                                     headers={"Content-Type": headertype},
                                     auth=HTTPBasicAuth(conf.user, conf.password), data=data)
        print("Request :", requests)
        print("Response :", http_response)
        _check_response(http_response)
        response = _check_response_dict(http_response, return_format='dict')

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def _get_case_id(case_id):
    response = _get_response(case_id, "")
    return response


def _get_token(token):
    response = _get_response(token, "token")
    return response


def _get_card_number(card_number, expiration_date):
    response = _get_responses(card_number, "cardNumber", expiration_date, "expirationDate")
    return response


def _get_arn(arn):
    response = _get_response(arn, "arn")
    return response


def _get_activity_date(activity_date):
    response = _get_response(activity_date.date(), "date")
    return response


def _get_actionable(actionable):
    response = _get_response(actionable, "actionable")
    return response


def _put_chargeback_update(caseId, request_body):
    response = _put_responses(caseId, request_body)
    return response


def _get_case_document(merchant_id, case_id):
    response = _get_document_response(merchant_id, case_id)
    return response


def _get_document(merchant_id, case_id, document_id):
    response = _get_document_responses(merchant_id, case_id, document_id)
    return response


def _get_documents(merchant_id, case_id):
    response = _get_document_response(merchant_id, case_id)
    return response


def _delete_document(merchant_id, case_id, document_id):
    response = _delete_document_response(merchant_id, case_id, document_id)
    return response


# def _upload_document(merchant_id, case_id, document_id, type, extension):
#     response = _upload_document_response(merchant_id, case_id, document_id, type, extension)
#     return response


def _post_document(merchant_id, case_id, document_id, request_body, headertype):
    response = _post_responses(merchant_id, case_id, document_id, request_body, headertype)
    return response


def _put_document(merchant_id, case_id, document_id, request_body, headertype):
    response = _put_response_upload(merchant_id, case_id, document_id, request_body, headertype)
    return response


class VantivException(Exception):
    pass
