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

import unittest2

from vantivsdk import utils, chargebackDocument

# sys.path.insert(0, package_root)

conf = utils.Configuration()
package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class TestChargebackDocument(unittest2.TestCase):
    def test_retrieve_chargebackDocument(self):
        chargebackDocument.retrieve_document("10000000", "document.jpg", package_root+"/samples/doc.tiff")
        self.assertTrue(os.path.exists(package_root+"/samples/doc.pdf"))

    def test_upload_chargebackDocument(self):
        path = package_root+"/samples/000_puppy_picture.jpg"
        response = chargebackDocument.upload_document("10000", path)
        self.assertEquals('000', response['ChargebackCase']['Document']['ResponseCode'])

    def test_update_chargebackDocument(self):
        path = package_root + "/samples/index.jpeg"
        response = chargebackDocument.replace_document("10000", "logo.tiff", path)
        self.assertEquals('000', response['ChargebackCase']['Document']['ResponseCode'])

    def test_delete_chargebackDocument(self):
        response = chargebackDocument.remove_document("10000", "logo.tiff")
        self.assertEquals('000', response['ChargebackCase']['Document']['ResponseCode'])

    def test_list_chargebackDocument(self):
        response = chargebackDocument.list_documents("1000000")
        self.assertEquals("1000000", response['ChargebackCase']['@id'])




if __name__ == '__main__':
    unittest2.main()
