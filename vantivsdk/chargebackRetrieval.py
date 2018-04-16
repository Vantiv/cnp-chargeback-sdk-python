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

import os

from vantivsdk import (fields_chargeback, utils, communication)

package_root = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
conf = utils.Configuration()
home_dir = os.environ['HOME']


# conf.header = {"Accept":"application/com.vantivcnp.services-v2+xml", "Content-Type":"application/com.vantivcnp.services-v2+xml"}

"""
Retrieval requests
"""


def get_case_id(case_id, config=conf):
    response = _get_response(case_id, "", None, None, config)
    return response


def get_token(token, config=conf):
    response = _get_response(token, "token", None, None, config)
    return response


def get_card_number(card_number, expiration_date, config=conf):
    response = _get_response(card_number, "cardNumber", expiration_date, "expirationDate", config)
    return response


def get_arn(arn, config=conf):
    response = _get_response(arn, "arn", None, None, config)
    return response


def get_activity_date(activity_date, config=conf):
    response = _get_response(activity_date, "date", None, None, config)
    return response


def get_financial_impact(activity_date, financial_impact, config=conf):
    response = _get_response(activity_date, "date", financial_impact, "financialOnly", config)
    return response


def get_actionable(actionable, config=conf):
    response = _get_response(actionable, "actionable", None, None, config)
    return response

"""
Internal methods
"""


def _get_response(parameter_value1, parameter_key1, parameter_value2=None, parameter_key2=None, config=conf):
    """ generate response with request method  GET
    :param parameter_value1: the parameter value to be appended in url
    :param parameter_key1: the paramater to be appended in url
    :return: returns the response received
    """
    url = config.url

    if parameter_key1 != "":
        url = url + "?"
        parameter_key1 = parameter_key1 + "="
    request = url + parameter_key1 + str(parameter_value1)

    if parameter_value2 is not None:
        if parameter_key2 != "":
            parameter_key2 = parameter_key2 + "="
        request = request + "&" + parameter_key2 + str(parameter_value2)

    response = communication.http_get_request(request, config)
    return response