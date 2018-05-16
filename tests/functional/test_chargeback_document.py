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

import unittest2

from cnpsdk import utils, chargeback_document

conf = utils.Configuration()
package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
document_to_upload1 = package_root + "/tests/doc.tiff"
document_to_upload2 = package_root + "/tests/test.jpg"
document_to_upload3 = package_root + "/tests/index.jpeg"


class TestChargebackDocument(unittest2.TestCase):

    def setUp(self):
        # create documents
        open(document_to_upload1, "w+").close()
        open(document_to_upload2, "w+").close()
        open(document_to_upload3, "w+").close()

    def tearDown(self):
        # delete documents
        os.remove(document_to_upload1)
        os.remove(document_to_upload2)
        os.remove(document_to_upload3)

    def test_retrieve_chargebackDocument(self):
        chargeback_document.retrieve_document("10000000", "document.jpg", "test.tiff")
        self.assertTrue(os.path.exists("test.tiff"))
        os.remove("test.tiff")

    def test_upload_chargebackDocument(self):
        response = chargeback_document.upload_document("10000", document_to_upload2)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('test.jpg', response['documentId'])
        self.assertEquals('10000', response['caseId'])

    def test_replace_chargebackDocument(self):
        response = chargeback_document.replace_document("10000", "logo.tiff", document_to_upload3)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('logo.tiff', response['documentId'])
        self.assertEquals('10000', response['caseId'])

    def test_delete_chargebackDocument(self):
        response = chargeback_document.delete_document("10000", "logo.tiff")
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('logo.tiff', response['documentId'])
        self.assertEquals('10000', response['caseId'])

    def test_list_chargebackDocument(self):
        response = chargeback_document.list_documents("10000")
        self.assertEquals("000", response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('10000', response['caseId'])
        document_list = response['documentId']
        self.assertIn("logo.tiff", document_list)
        self.assertIn("doc.tiff", document_list)

    def test_error_response(self):
        response = chargeback_document.upload_document("10001", document_to_upload1)
        self.assertEquals('001', response['responseCode'])
        self.assertEquals('Invalid Merchant', response['responseMessage'])

        try:
            chargeback_document.retrieve_document(123009, "logo.tiff", "test.tiff")
        except utils.ChargebackDocumentError as e:
            self.assertEquals("Document Not Found", e.message)
            self.assertEquals("009", e.code)

        try:
            chargeback_document.retrieve_document(123404, "logo.tiff", "test.tiff")
        except utils.ChargebackWebError as e:
            self.assertEquals("Could not find requested object.", e.message)
            self.assertEquals("404", e.code)


if __name__ == '__main__':
    unittest2.main()
