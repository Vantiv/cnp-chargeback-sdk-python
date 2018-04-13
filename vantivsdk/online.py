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
import os
from requests.auth import HTTPBasicAuth
from vantivsdk import (fields_chargeback, utils, communication)

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
conf = utils.Configuration()
home_dir = os.environ['HOME']


# conf.header = {"Accept":"application/com.vantivcnp.services-v2+xml", "Content-Type":"application/com.vantivcnp.services-v2+xml"}

"""
Retrieval requests
"""


def get_case_id(case_id):
    response = _get_response(case_id, "")
    return response


def get_token(token):
    response = _get_response(token, "token")
    return response


def get_card_number(card_number, expiration_date):
    response = _get_response(card_number, "cardNumber", expiration_date, "expirationDate")
    return response


def get_arn(arn):
    response = _get_response(arn, "arn")
    return response


def get_activity_date(activity_date):
    response = _get_response(activity_date, "date")
    return response


def get_financial_impact(activity_date, financial_impact):
    response = _get_response(activity_date, "date", financial_impact, "financialOnly")
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
    response = _put_response(case_id, request_body)
    return response


def add_note_to_case(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "ADD_NOTE"
    request_body.note = note
    response = _put_response(case_id, request_body)
    return response


def assume_liability(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_ACCEPTS_LIABILITY"
    request_body.note = note
    response = _put_response(case_id, request_body)
    return response


def represent_case(case_id, note, representment_amount=None):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_REPRESENT"
    request_body.note = note
    request_body.representedAmount = representment_amount
    response = _put_response(case_id, request_body)
    return response


def respond_to_retrieval_request(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_RESPOND"
    request_body.note = note
    response = _put_response(case_id, request_body)
    return response


def request_arbitration(case_id, note):
    request_body = fields_chargeback.chargebackUpdateRequest()
    request_body.activityType = "MERCHANT_REQUESTS_ARBITRATION"
    request_body.note = note
    response = _put_response(case_id, request_body)
    return response


"""
Document requests
"""


def upload_document(case_id, document):
    response = communication.post_document_responses(case_id, document)
    return response


def retrieve_document(case_id, document_id):
    communication.get_document_responses(case_id, document_id)


def replace_document(case_id, document_id, document_path):
    response = communication.update_document_responses(case_id, document_id, document_path)
    return response


def remove_document(case_id, document_id):
    response = communication.delete_document_response(case_id, document_id)
    return response


def list_documents(case_id):
    response = communication.get_document_response(case_id)
    return response


"""
Internal methods
"""


def _get_response(parameter_value1, parameter_key1, parameter_value2=None, parameter_key2=None):
    """ generate response with request method  GET
    :param parameter_value1: the parameter value to be appended in url
    :param parameter_key1: the paramater to be appended in url
    :return: returns the response received
    """
    url = conf.url

    if parameter_key1 != "":
        url = url + "?"
        parameter_key1 = parameter_key1 + "="
    request = url + parameter_key1 + str(parameter_value1)

    if parameter_value2 is not None:
        if parameter_key2 != "":
            parameter_key2 = parameter_key2 + "="
        request = request + "&" + parameter_key2 + str(parameter_value2)

    response = communication.http_get_request(request)
    return response


def _put_response(parameter_value1, request_body):
    request = conf.url + "/" + str(parameter_value1)
    response = communication.http_put_request(request, request_body)
    return response


class VantivException(Exception):
    pass
