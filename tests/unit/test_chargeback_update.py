# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os
import sys
import unittest
from collections import OrderedDict

import mock
import unittest2

from vantivsdk import (utils, chargeback_update)

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)
conf = utils.Configuration()


class TestChargebackRetrieval(unittest2.TestCase):

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_assign_case_to_user(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.assign_case_to_user(123, "test_user", "test_note")
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_add_note_to_case(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.add_note_to_case(123, "test_note")
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_assume_liability(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.assume_liability(123, "test_note")
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_represent_case(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.represent_case(123, "test_note", representment_amount=1234)
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_represent_case_full(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.represent_case(123, "test_note")
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_respond_to_retrieval_request(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.respond_to_retrieval_request(123, "test_note")
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_request_arbitration(self, mock_http_put_request):
        mock_http_put_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'21260530003675')])
        response = chargeback_update.request_arbitration(123, "test_note")
        self.assertRegex(response["transactionId"], "\d+")

    @mock.patch('vantivsdk.communication.http_put_request')
    def test_error_response(self, mock_http_put_request):
        mock_http_put_request.side_effect = utils.VantivException()
        self.assertRaises(utils.VantivException, chargeback_update.add_note_to_case, "00", "note")


if __name__ == '__main__':
    unittest.main()
