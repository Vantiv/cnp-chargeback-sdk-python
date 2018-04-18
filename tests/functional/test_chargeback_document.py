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
    document_to_upload1 = package_root + "/tests/doc.tiff"
    document_to_upload2 = package_root + "/tests/000_puppy_picture.jpg"
    document_to_upload3 = package_root + "/tests/index.jpeg"

    def setUp(self):
        # create documents
        open(self.document_to_upload1, "w+").close()
        open(self.document_to_upload2, "w+").close()
        open(self.document_to_upload3, "w+").close()

    def tearDown(self):
        # delete documents
        os.remove(self.document_to_upload1)
        os.remove(self.document_to_upload2)
        os.remove(self.document_to_upload3)

    def test_retrieve_chargebackDocument(self):
        chargebackDocument.retrieve_document("10000000", "document.jpg", package_root+"/tests/doc.tiff")
        self.assertTrue(os.path.exists(package_root+"/tests/doc.tiff"))

    def test_upload_chargebackDocument(self):
        path = package_root+"/tests/000_puppy_picture.jpg"
        response = chargebackDocument.upload_document("10000", path)
        self.assertEquals('000', response['responseCode'])

    def test_update_chargebackDocument(self):
        path = package_root + "/tests/index.jpeg"
        response = chargebackDocument.replace_document("10000", "logo.tiff", path)
        self.assertEquals('000', response['responseCode'])

    def test_delete_chargebackDocument(self):
        response = chargebackDocument.remove_document("10000", "logo.tiff")
        self.assertEquals('000', response['responseCode'])

    def test_list_chargebackDocument(self):
        response = chargebackDocument.list_documents("1000000")
        self.assertEquals("000", response['responseCode'])

    def test_upload_chargebackDocument(self):
        path = package_root + "/tests/000_puppy_picture.jpg"
        response = chargebackDocument.upload_document("10001", path)
        self.assertEquals('001', response['responseCode'])

if __name__ == '__main__':
    unittest2.main()
