# # -*- coding: utf-8 -*-
# # Copyright (c) 2017 Vantiv eCommerce
# #
# # Permission is hereby granted, free of charge, to any person
# # obtaining a copy of this software and associated documentation
# # files (the 'Software'), to deal in the Software without
# # restriction, including without limitation the rights to use,
# # copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the
# # Software is furnished to do so, subject to the following
# # conditions:
# #
# # The above copyright notice and this permission notice shall be
# # included in all copies or substantial portions of the Software.
# #
# # THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# # EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# # OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# # NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# # HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# # OTHER DEALINGS IN THE SOFTWARE.
#

import os
import sys

import unittest2

from vantivsdk import chargebackRetrieval, utils

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

conf = utils.Configuration()


class TestChargebackRetrieval(unittest2.TestCase):

    def test_activity_date(self):
        response = chargebackRetrieval.get_activity_date("2018-01-01")
        self.assertRegex(response["transactionId"], "\d+")
        self.assertEqual("2018-01-01", response["chargebackCase"][0]["dateReceivedByVantivCnp"])

    def test_activity_date_financial_impact(self):
        response = chargebackRetrieval.get_financial_impact("2018-01-01", "true")
        self.assertRegex(response["transactionId"], "\d+")

    def test_actionable(self):
        response = chargebackRetrieval.get_actionable("true")
        self.assertRegex(response["transactionId"], "\d+")

    def test_get_case_id(self):
        response = chargebackRetrieval.get_case_id("1333078000")
        self.assertEquals("1333078000", response["chargebackCase"][0]["caseId"])

    def test_get_token(self):
        response = chargebackRetrieval.get_token("1000000")
        self.assertRegex(response["transactionId"], "\d+")

    def test_card_number(self):
        response = chargebackRetrieval.get_card_number("1111000011110000", "0118")
        self.assertRegex(response["transactionId"], "\d+")

    def test_arn(self):
        response = chargebackRetrieval.get_arn("1111111111")
        self.assertRegex(response["transactionId"], "\d+")


if __name__ == '__main__':
    unittest2.main()
