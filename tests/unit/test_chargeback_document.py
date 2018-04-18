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

from vantivsdk import (utils, chargebackDocument)

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)
conf = utils.Configuration()


class TestChargebackRetrieval(unittest.TestCase):
    document_to_upload = package_root + "/tests/doc.tiff"
    document_to_retrieve = package_root + "/tests/test.tiff"

    def setUp(self):
        # create documents
        open(self.document_to_upload, "w+").close()

    def tearDown(self):
        # delete documents
        os.remove(self.document_to_upload)

    @mock.patch('vantivsdk.communication.post_document_request')
    def test_upload_document(self, mock_post_document_request):
        mock_post_document_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', u'doc.tiff'), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargebackDocument.upload_document("10000", self.document_to_upload)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('10000', response['caseId'])
        self.assertEquals('doc.tiff', response['documentId'])

    @mock.patch('vantivsdk.communication.get_document_request')
    def test_retrieve_document(self, mock_get_document_request):
        mock_get_document_request.side_effect = open(self.document_to_retrieve, "w+").close()
        chargebackDocument.retrieve_document(123, "doc.pdf", "test.tiff")
        self.assertTrue(os.path.exists(self.document_to_retrieve))
        os.remove(self.document_to_retrieve)

    @mock.patch('vantivsdk.communication.put_document_request')
    def test_replace_document(self, mock_put_document_request):
        mock_put_document_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', u'doc.tiff'), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargebackDocument.replace_document("10000", "doc.pdf", self.document_to_upload)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('10000', response['caseId'])
        self.assertEquals('doc.tiff', response['documentId'])

    @mock.patch('vantivsdk.communication.delete_document_response')
    def test_remove_document(self, mock_delete_document_response):
        mock_delete_document_response.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', u'logo.tiff'), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargebackDocument.remove_document("10000", "logo.tiff")
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('10000', response['caseId'])
        self.assertEquals('logo.tiff', response['documentId'])

    @mock.patch('vantivsdk.communication.get_document_list_request')
    def test_list_documents(self, mock_get_document_list_request):
        mock_get_document_list_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', [u'logo.tiff', u'doc.tiff']), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargebackDocument.list_documents("10000")
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])
        self.assertEquals('10000', response['caseId'])
        document_list = response['documentId']
        self.assertIn("logo.tiff", document_list)
        self.assertIn("doc.tiff", document_list)

    @mock.patch('vantivsdk.communication.get_document_request')
    def test_error_response(self, mock_get_document_request):
        mock_get_document_request.side_effect = utils.VantivException()
        self.assertRaises(utils.VantivException, chargebackDocument.retrieve_document, 0, "doc.pdf", "test.tiff")


if __name__ == '__main__':
    unittest.main()
