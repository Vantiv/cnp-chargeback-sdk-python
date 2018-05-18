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

from cnpsdk import (utils, chargeback_document)

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)
conf = utils.Configuration()
document_to_upload = package_root + "/tests/doc.tiff"
document_to_retrieve = package_root + "/tests/test.tiff"


class TestChargebackRetrieval(unittest.TestCase):

    def setUp(self):
        # create documents
        open(document_to_upload, "w+").close()

    def tearDown(self):
        # delete documents
        os.remove(document_to_upload)

    @mock.patch('cnpsdk.communication.http_post_document_request')
    def test_upload_document(self, mock_http_post_document_request):
        mock_http_post_document_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', u'doc.tiff'), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargeback_document.upload_document("10000", document_to_upload)
        args = mock_http_post_document_request.call_args
        self.assertEquals(args[0][0], "/services/chargebacks/upload/10000/doc.tiff")
        self.assertEquals(response['responseCode'], '000')
        self.assertEquals(response['responseMessage'], 'Success')
        self.assertEquals(response['caseId'], '10000')
        self.assertEquals(response['documentId'], 'doc.tiff')

    @mock.patch('cnpsdk.communication.http_get_document_request')
    def test_retrieve_document(self, mock_http_get_document_request):
        mock_http_get_document_request.side_effect = open(document_to_retrieve, "w+").close()
        chargeback_document.retrieve_document(123, "doc.pdf", "test.tiff")
        args = mock_http_get_document_request.call_args
        self.assertEquals(args[0][0], "/services/chargebacks/retrieve/123/doc.pdf")
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

    @mock.patch('cnpsdk.communication.http_put_document_request')
    def test_replace_document(self, mock_http_put_document_request):
        mock_http_put_document_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', u'doc.tiff'), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargeback_document.replace_document("10000", "doc.pdf", document_to_upload)
        args = mock_http_put_document_request.call_args
        self.assertEquals(args[0][0], "/services/chargebacks/replace/10000/doc.pdf")
        self.assertEquals(response['responseCode'], '000')
        self.assertEquals(response['responseMessage'], 'Success')
        self.assertEquals(response['caseId'], '10000')
        self.assertEquals(response['documentId'], 'doc.tiff')

    @mock.patch('cnpsdk.communication.http_delete_document_response')
    def test_delete_document(self, mock_http_delete_document_response):
        mock_http_delete_document_response.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', u'logo.tiff'), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargeback_document.delete_document("10000", "logo.tiff")
        args = mock_http_delete_document_response.call_args
        self.assertEquals(args[0][0], "/services/chargebacks/delete/10000/logo.tiff")
        self.assertEquals(response['responseCode'], '000')
        self.assertEquals(response['responseMessage'], 'Success')
        self.assertEquals(response['caseId'], '10000')
        self.assertEquals(response['documentId'], 'logo.tiff')

    @mock.patch('cnpsdk.communication.http_get_document_list_request')
    def test_list_documents(self, mock_http_get_document_list_request):
        mock_http_get_document_list_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'merchantId', u'999'), (u'caseId', u'10000'),
             (u'documentId', [u'logo.tiff', u'doc.tiff']), (u'responseCode', u'000'), (u'responseMessage', u'Success')])
        response = chargeback_document.list_documents("10000")
        args = mock_http_get_document_list_request.call_args
        self.assertEquals(args[0][0], "/services/chargebacks/list/10000")
        self.assertEquals(response['responseCode'], '000')
        self.assertEquals(response['responseMessage'], 'Success')
        self.assertEquals(response['caseId'], '10000')
        document_list = response['documentId']
        self.assertIn("logo.tiff", document_list)
        self.assertIn("doc.tiff", document_list)

    @mock.patch('cnpsdk.communication.http_get_document_request')
    def test_error_response(self, mock_http_get_document_request):
        mock_http_get_document_request.side_effect = utils.ChargebackError("Error")
        self.assertRaises(utils.ChargebackError, chargeback_document.retrieve_document, 0, "doc.pdf", "test.tiff")


if __name__ == '__main__':
    unittest.main()
