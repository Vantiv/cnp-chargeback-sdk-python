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

from vantivsdk import (utils, communication)

conf = utils.Configuration()

"""
/////////////////////////////////////////////////////
            ChargebackRetrieval API:
/////////////////////////////////////////////////////
"""


def get_chargeback_by_case_id(case_id, config=conf):
    response = _get_retrieval_response(case_id, "", config=config)
    return response


def get_chargebacks_by_token(token, config=conf):
    response = _get_retrieval_response(token, "token", config=config)
    return response


def get_chargebacks_by_card_number(card_number, expiration_date, config=conf):
    response = _get_retrieval_response(card_number, "cardNumber", expiration_date, "expirationDate", config=config)
    return response


def get_chargebacks_by_arn(arn, config=conf):
    response = _get_retrieval_response(arn, "arn", config=config)
    return response


def get_chargebacks_by_date(activity_date, config=conf):
    response = _get_retrieval_response(activity_date, "date", config=config)
    return response


def get_chargebacks_by_financial_impact(activity_date, financial_impact, config=conf):
    response = _get_retrieval_response(activity_date, "date", financial_impact, "financialOnly", config=config)
    return response


def get_actionable_chargebacks(actionable, config=conf):
    response = _get_retrieval_response(actionable, "actionable", config=config)
    return response


"""
/////////////////////////////////////////////////////
"""


def _get_retrieval_response(parameter_value1, parameter_key1, parameter_value2=None, parameter_key2=None, config=conf):
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

    response = communication.http_get_retrieval_request(request, config)
    return response