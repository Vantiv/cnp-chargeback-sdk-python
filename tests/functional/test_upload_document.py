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

from vantivsdk import fields_chargebackDocument, utils, online, contentTypeEnum
import requests
from requests.auth import HTTPBasicAuth
package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

conf = utils.Configuration()


class TestUploadChargebackDocument(unittest2.TestCase):
    def test_upload_chargebackDocument(self):
        param = fields_chargebackDocument.Merchant();
        param.id = u'01333078'
        param1 = fields_chargebackDocument.ChargebackCase();
        param1.id = u'01333078001'
        param2 = fields_chargebackDocument.Document()
        param2.id = u'test6_8'

        path = package_root+"/samples/000_puppy_picture.jpg"
        headercontent = contentTypeEnum.ContentType.JPEG
        response = online._post_document(param.id, param1.id, param2.id, path, headercontent)

        self.assertEquals('000', response['ChargebackCase']['Document']['ResponseCode'])


if __name__ == '__main__':
    unittest2.main()
