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
import pyxb
from vantivsdk import utils, fields, online, parameters

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

conf = utils.Configuration()


class TestCardNumber(unittest2.TestCase):
    def test_get_token(self):
        param = parameters.Parameters()
        param.expiration_date = u'0150'
        param.card_number = u'6500102010004006'
        # request_type = 'GET'
        # request_body = ''
        response = online._get_card_number(param.card_number, param.expiration_date)
        # response = online.request(request_type, request_body, param, conf)
        #self.assertEquals('1304283001', response['chargebackCase']['caseId'])


if __name__ == '__main__':
    unittest2.main()
