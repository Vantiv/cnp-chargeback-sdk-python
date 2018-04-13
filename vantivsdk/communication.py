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


def http_get_request(request_url):
    try:
        http_response = requests.get(request_url, headers=conf.chargebackApi_headers,
                                     auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("GET request to:", request_url)
    print("Response :", http_response)
    check_response(http_response)
    response = check_response_dict(http_response, return_format='dict')
    return response


def http_put_request(request_url, request_xml):
    try:
        http_response = requests.put(request_url, headers=conf.chargebackApi_headers,
                                     auth=HTTPBasicAuth(conf.user, conf.password),
                                     data=create_request_xml(request_xml))
        print("Request :", request_url)
        print("Response :", http_response)
        check_response(http_response)
        response = check_response_dict(http_response, return_format='dict')
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def get_document_responses(case_id, document_id):
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
    check_response(http_response)
    response = check_response_dict(http_response, return_format='dict')

    return response


def delete_document_response(case_id, document_id):
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
    check_response(http_response)
    response = check_response_dict(http_response, return_format='dict')

    return response


def post_document_responses(case_id, path):
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
        check_response(http_response)
        response = check_response_dict(http_response, return_format='dict')
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def update_document_responses(case_id, document_id, path):
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
        check_response(http_response)
        response = check_response_dict(http_response, return_format='dict')

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    return response


def get_document_response(case_id):
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
    check_response(http_response)
    response = check_response_dict(http_response, return_format='dict')

    return response


def check_response(response):
    """check the status code of the response
    :param response: http response generated
    :return: raises an exception
    """

    if response.status_code != 200:
        raise utils.VantivException("Error with Https Response, Status code: ", response.status_code)

    # Check empty response
    if not response:
        raise utils.VantivException("The response is empty, Please call Vantiv eCommerce")


def check_response_dict(response, return_format='dict'):
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


def create_request_xml(request_body):
    """ Create xml string from request object
    :param request_body: request_body
    :return: XML string
    """
    request_xml = utils.obj_to_xml(request_body)

    if conf.print_xml:
        print('Request XML:\n', request_xml.decode('utf-8'), '\n')

    return request_xml


class VantivException(Exception):
    pass