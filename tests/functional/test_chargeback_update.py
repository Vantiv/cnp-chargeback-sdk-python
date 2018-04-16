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

from vantivsdk import utils, chargebackUpdate

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

conf = utils.Configuration()


class TestChargebackUpdate(unittest2.TestCase):
    def test_assign_case_to_user(self):
        response = chargebackUpdate.assign_case_to_user(10000, "jdeo@company.com", "Test note")
        self.assertRegex(response["transactionId"], "\d+")

    def test_add_not_to_case(self):
        response = chargebackUpdate.add_note_to_case(10000, "Test note")
        self.assertRegex(response["transactionId"], "\d+")

    def test_assume_liability(self):
        response = chargebackUpdate.assume_liability(10000, "Test note")
        self.assertRegex(response["transactionId"], "\d+")

    def test_represent_case(self):
        response = chargebackUpdate.represent_case(10000, "Test note", 12000)
        self.assertRegex(response["transactionId"], "\d+")

    def test_represent_case_full(self):
        response = chargebackUpdate.represent_case(10000, "Test note")
        self.assertRegex(response["transactionId"], "\d+")

    def test_respond_to_retrieval_request(self):
        response = chargebackUpdate.respond_to_retrieval_request(10000, "Test note")
        self.assertRegex(response["transactionId"], "\d+")

    def test_request_arbitration(self):
        response = chargebackUpdate.request_arbitration(10000, "Test note")
        self.assertRegex(response["transactionId"], "\d+")


if __name__ == '__main__':
    unittest2.main()
