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
import os

import re
import requests
from requests.auth import HTTPBasicAuth
from vantivsdk import (utils)

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
conf = utils.Configuration()
home_dir = os.environ['HOME']

chargebackApi_headers = {"Accept": "application/com.vantivcnp.services-v2+xml",
                         "Content-Type": "application/com.vantivcnp.services-v2+xml"}


def get_retrieval_request(request_url, config=conf):
    try:
        http_response = requests.get(request_url, headers=chargebackApi_headers,
                                     auth=HTTPBasicAuth(config.user, config.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nGET request to:", request_url, config)
    print_to_console("\nResponse :", utils.generate_retrieval_response(http_response, "xml"), config)
    check_response(http_response)
    response = utils.generate_retrieval_response(http_response)
    return response


def http_put_request(request_url, request_xml, config=conf):
    try:
        http_response = requests.put(request_url, headers=chargebackApi_headers,
                                     auth=HTTPBasicAuth(config.user, config.password),
                                     data=create_request_xml(request_xml))
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nPUT request to:", request_url, config)
    print_to_console("\nResponse :", utils.generate_update_response(http_response, "xml"), config)
    check_response(http_response)
    response = utils.generate_update_response(http_response)
    return response


def get_document_request(request_url, document_path, config=conf):
    """ generate response when merchant id, case id and document id is given using GET method

    :param parameter_value1: merchant id to be appended to url
    :param case_id: case id to be appended to ur
    :param document_id: document id to be appended to ur
    :return: the http response generated
    """
    try:
        http_response = requests.get(request_url, auth=HTTPBasicAuth(config.user, config.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nGET Request to:", request_url, config)
    check_response(http_response)
    retrieve_file(http_response, document_path, config.print_xml)


def delete_document_response(request_url, config=conf):
    try:
        http_response = requests.delete(request_url, auth=HTTPBasicAuth(config.user, config.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nDELETE request to:", request_url, config)
    print_to_console("\nResponse :", utils.generate_document_response(http_response, "xml"), config)
    check_response(http_response)
    response = utils.generate_document_response(http_response)
    return response


def post_document_request(request_url, document_path, config=conf):
    try:
        data, content_type = get_file_content(document_path)
        http_response = requests.post(url=request_url,
                                      headers={"Content-Type": content_type},
                                      auth=HTTPBasicAuth(config.user, config.password), data=data)
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nPOST request to:", request_url, config)
    print_to_console("\nFile:", document_path, config)
    print_to_console("\nResponse :", utils.generate_document_response(http_response, "xml"), config)
    check_response(http_response)
    response = utils.generate_document_response(http_response)
    return response


def put_document_request(request_url, document_path, config=conf):
    try:
        data, content_type = get_file_content(document_path)
        http_response = requests.put(url=request_url,
                                     headers={"Content-Type": content_type},
                                     auth=HTTPBasicAuth(config.user, config.password), data=data)
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nPUT request to:", request_url, config)
    print_to_console("\nFile:", document_path, config)
    print_to_console("\nResponse :", utils.generate_document_response(http_response, "xml"), config)
    check_response(http_response)
    response = utils.generate_document_response(http_response)
    return response


def get_document_list_request(request_url, config=conf):
    try:
        http_response = requests.get(request_url, headers=chargebackApi_headers,
                                     auth=HTTPBasicAuth(config.user, config.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    print_to_console("\nGET request to:", request_url, config)
    print_to_console("\nResponse :", utils.generate_document_response(http_response, "xml"), config)
    check_response(http_response)
    response = utils.generate_document_response(http_response)
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


def retrieve_file(response, document_path, print_xml):
    with open(document_path, 'wb') as f:
        for block in response.iter_content(1024):
            f.write(block)

    if print_xml:
        print("\nDocument saved at: ", document_path)


def create_request_xml(request_body):
    """ Create xml string from request object
    :param request_body: request_body
    :return: XML string
    """
    request_xml = utils.obj_to_xml(request_body)
    # if conf.print_xml:
    #     print('\nRequest XML:\n', request_xml.decode('utf-8'), '\n')
    return request_xml


def get_file_content(path):
    with open(path, 'rb') as f:
        data = f.read()
    content_type = mimetypes.guess_type(path)[0]
    return data, content_type


def neuter_xml(xml_string):
    xml_string = re.sub(r"<accNum>.*</accNum>", "<accNum>****</accNum>", xml_string)
    xml_string = re.sub(r"<user>.*</user>", "<user>****</user>", xml_string)
    xml_string = re.sub(r"<password>.*</password>", "<password>****</password>", xml_string)
    xml_string = re.sub(r"<track>.*</track>", "<track>****</track>", xml_string)
    xml_string = re.sub(r"<number>.*</number>", "<number>****</number>", xml_string)
    return xml_string


def print_to_console(prefix_message, xml_string, config=conf):
    if config.print_xml:
        if config.neuter_xml:
            xml_string = neuter_xml(xml_string)
        print(prefix_message, xml_string)
