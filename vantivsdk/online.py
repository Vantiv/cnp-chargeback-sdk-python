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

import mimetypes

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


# conf.header = {"Accept":"application/com.vantivcnp.services-v2+xml", "Content-Type":"application/com.vantivcnp.services-v2+xml"}


def _get_response(parameter_value, parameter_key):
    """ generate response with request method  GET
    :param parameter_value: the parameter value to be appended in url
    :param parameter_key: the paramater to be appended in url
    :return: returns the response received
    """
    url = conf.url
    try:
        if parameter_key != "":
            url = url + "?"
            parameter_key = parameter_key + "="
        request = url + parameter_key + str(parameter_value)
        http_response = requests.get(request, headers=conf.chargebackApi_headers,
                                     auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    # print("URL :", )
    print("Request : ", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')
    return response


def _get_responses(parameter_value1, parameter_key1, parameter_value2, parameter_key2):
    """ generate response with multiple parameters with request method  GET
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
        http_response = requests.get(request, headers=conf.chargebackApi_headers,
                                     auth=HTTPBasicAuth(conf.user, conf.password))

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
        with open(package_root + '/samples/doc.pdf', 'wb') as f:
            f.write(response.content)


def _put_responses(parameter_value1, request_body):
    """ generate response with request method  PUT
    :param parameter_value1: the parameter value to be appended in url
    :param request_body: the input object for the xml
    :return: return the response generated
    """

    try:
        request = conf.url + str(parameter_value1)
        http_response = requests.put(request, headers=conf.chargebackApi_headers,
                                     auth=HTTPBasicAuth(conf.user, conf.password),
                                     data=_create_request_xml(request_body))
        print("Request :", request)
        print("Response :", http_response)
        _check_response(http_response)
        response = _check_response_dict(http_response, return_format='dict')
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def _get_document_response(case_id):
    """ generate response when merchant id, case id is given using GET method
    :param parameter_value1:  the parameter value to be appended in url
    :param case_id: the parameter value to be appended in url
    :return:
    """

    url = conf.url

    try:

        request = url + "/list/" + str(case_id)
        http_response = requests.get(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("Request: ", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


def _get_document_responses(case_id, document_id):
    """ generate response when merchant id, case id and document id is given using GET method

    :param parameter_value1: merchant id to be appended to url
    :param case_id: case id to be appended to ur
    :param document_id: document id to be appended to ur
    :return: the http response generated
    """
    url = conf.url
    try:
        request = url + "/retrieve/" + str(case_id) + "/" + str(document_id)
        http_response = requests.get(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("Request:", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


def _delete_document_response(case_id, document_id):
    """ generate response when merchant id, case id and document id is given using DELETE method

    :param parameter_value1: merchant id to be appended to url
    :param case_id: case id to be appended to ur
    :param document_id: document id to be appended to ur
    :return: the http response generated
    """

    url = conf.url
    try:
        request = url + "/remove/" + str(case_id) + "/" + str(document_id)
        http_response = requests.delete(request, auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("Request:", request)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response


def _post_document_responses(case_id, path):
    """ generate response when merchant id, case id and document id is given using POST method

    :param merchant_id:merchant id to be appended to url
    :param case_id:case id to be appended to url
    :param document_id:document id to be appended to ur
    :param path: file path of the document to be uploaded
    :param headertype: appropriate header for the document to be uploaded
    :return:
    """
    try:
        with open(path, 'rb') as f:
            data = f.read()

        document_id = path.split("/")[-1]
        headertype = mimetypes.guess_type(path)[0]
        url = conf.url + "/upload/" + str(case_id) + "/" + str(document_id)
        http_response = requests.post(url=url,
                                      headers={"Content-Type": headertype},
                                      auth=HTTPBasicAuth(conf.user, conf.password), data=data)
        print("Request :", url)
        print("Response :", http_response)
        _check_response(http_response)
        response = _check_response_dict(http_response, return_format='dict')
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def _update_document_responses(case_id, document_id, path):
    """generate response when merchant id, case id and document id is given using PUT method

    :param merchant_id: merchant_id:merchant id to be appended to url
    :param case_id: case_id:case id to be appended to url
    :param document_id: document id to be appended to ur
    :param path: file path of the document to be uploaded
    :param headertype: appropriate header for the document to be uploaded
    :return:
    """
    try:
        url = conf.url + "/replace/" + case_id + "/" + document_id
        with open(path, 'rb') as f:
            data = f.read()

        headertype = mimetypes.guess_type(path)[0]
        http_response = requests.put(url=url,
                                     headers={"Content-Type": headertype},
                                     auth=HTTPBasicAuth(conf.user, conf.password), data=data)
        print("Request :", url)
        print("Response :", http_response)
        _check_response(http_response)
        response = _check_response_dict(http_response, return_format='dict')

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


"""
Functions for the different combinations of get and put requests
"""


def get_case_id(case_id):
    response = _get_response(case_id, "")
    return response


def get_token(token):
    response = _get_response(token, "token")
    return response


def get_card_number(card_number, expiration_date):
    response = _get_responses(card_number, "cardNumber", expiration_date, "expirationDate")
    return response


def get_arn(arn):
    response = _get_response(arn, "arn")
    return response


def get_activity_date(activity_date):
    response = _get_response(activity_date, "date")
    return response


def get_financial_impact(activity_date, financial_impact):
    response = _get_responses(activity_date, "date", financial_impact, "financialOnly")
    return response


def get_actionable(actionable):
    response = _get_response(actionable, "actionable")
    return response


"""
Update requests
"""


def assign_case_to_user(case_id, user_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "ASSIGN_TO_USER"
    request_body.assignedTo = user_id
    request_body.note = note
    response = _put_chargeback_update(case_id, request_body)
    return response


def add_note_to_case(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "ADD_NOTE"
    request_body.note = note
    response = _put_chargeback_update(case_id, request_body)
    return response


def assume_liability(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_ACCEPTS_LIABILITY"
    request_body.note = note
    response = _put_chargeback_update(case_id, request_body)
    return response


def represent_case(case_id, note, representment_amount=None):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_REPRESENT"
    request_body.note = note
    request_body.representedAmount = representment_amount
    response = _put_chargeback_update(case_id, request_body)
    return response


def respond_to_retrieval_request(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_RESPOND"
    request_body.note = note
    response = _put_chargeback_update(case_id, request_body)
    return response


def request_arbitration(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_REQUESTS_ARBITRATION"
    request_body.note = note
    response = _put_chargeback_update(case_id, request_body)
    return response


"""
Document requests
"""

def upload_document(case_id, document):
    response = _post_document_responses(case_id, document)
    return response


def retrieve_document(case_id, document_id):
    _get_document(case_id, document_id)
    return None


def replace_document(case_id, document_id, document_path):
    response = _update_document_responses(case_id, document_id, document_path)
    return response


def remove_document(case_id, document_id):
    response = _delete_document_response(case_id, document_id)
    return response


def list_documents(case_id):
    response = _get_document_response(case_id)
    return response

"""
Internal methods
"""


def _put_chargeback_update(caseId, request_body):
    response = _put_responses(caseId, request_body)
    return response


def _get_case_document(case_id):
    response = _get_document_response(case_id)
    return response


def _get_document(case_id, document_id):
    response = _get_document_responses(case_id, document_id)
    return response


def _get_documents(merchant_id, case_id):
    response = _get_document_response(merchant_id, case_id)
    return response


def _delete_document(case_id, document_id):
    response = _delete_document_response(case_id, document_id)
    return response


def _post_document(case_id, path):
    response = _post_document_responses(case_id, path)
    return response


def _put_document(merchant_id, case_id, document_id, path, headertype):
    response = _update_document_responses(merchant_id, case_id, document_id, path, headertype)
    return response


class VantivException(Exception):
    pass
