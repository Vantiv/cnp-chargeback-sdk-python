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

from cnpsdk import utils, chargeback_document

# sys.path.insert(0, package_root)

conf = utils.Configuration()
conf.url = 'https://services.vantivprelive.com/services/chargebacks/'
package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class TestChargebackDocument(unittest2.TestCase):
    document_to_upload1 = package_root + "/tests/test.jpg"
    document_to_upload2 = package_root + "/tests/test.gif"
    document_to_upload3 = package_root + "/tests/test.pdf"
    document_to_upload4 = package_root + "/tests/test.tiff"

    def setUp(self):
        # create documents
        open(self.document_to_upload1, "w+").close()
        open(self.document_to_upload2, "w+").close()
        open(self.document_to_upload3, "w+").close()
        open(self.document_to_upload4, "w+").close()

    def tearDown(self):
        # delete documents
        os.remove(self.document_to_upload1)
        os.remove(self.document_to_upload2)
        os.remove(self.document_to_upload3)
        os.remove(self.document_to_upload4)

    def test_1(self):
        case_id = conf.merchant_id + "001"
        response = chargeback_document.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargeback_document.upload_document(case_id, self.document_to_upload2, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargeback_document.upload_document(case_id, self.document_to_upload3, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargeback_document.list_documents(case_id, config=conf)
        document_list = response['documentIds']
        self.assertIn("test.jpg", document_list)
        self.assertIn("test.gif", document_list)
        self.assertIn("test.pdf", document_list)

        document_to_retrieve = package_root + "/tests/test1.tiff"
        chargeback_document.retrieve_document(case_id, "test.jpg", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        chargeback_document.retrieve_document(case_id, "test.gif", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        chargeback_document.retrieve_document(case_id, "test.pdf", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        response = chargeback_document.replace_document(case_id, "test.jpg", self.document_to_upload4, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        chargeback_document.retrieve_document(case_id, "test.tiff", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        response = chargeback_document.delete_document(case_id, "test.gif", config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargeback_document.list_documents(case_id, config=conf)
        document_list = response['documentIds']
        self.assertIn("test.pdf", document_list)
        self.assertIn("test.tiff", document_list)

    def test_2(self):
        case_id = conf.merchant_id + "002"

        response = chargeback_document.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('010', response['responseCode'])
        self.assertEquals('Case not in valid cycle', response['responseMessage'])

    def test_3(self):
        case_id = conf.merchant_id + "003"

        response = chargeback_document.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('004', response['responseCode'])
        self.assertEquals('Case Not In Merchant Queue', response['responseMessage'])

    def test_4(self):
        case_id = conf.merchant_id + "004"

        document_maxsize = package_root + "/tests/maxsize.tif"
        open(document_maxsize, "w+").close()

        response = chargeback_document.upload_document(case_id, document_maxsize, config=conf)
        self.assertEquals('005', response['responseCode'])
        self.assertEquals('Document already exists', response['responseMessage'])
        os.remove(document_maxsize)

        document_maxsize = package_root + "/tests/maxsize1.tif"
        with open(document_maxsize, "w+") as f:
            f.seek(2100000)
            f.write("\0")

        response = chargeback_document.upload_document(case_id, document_maxsize, config=conf)
        self.assertEquals('012', response['responseCode'])
        self.assertEquals('Filesize exceeds limit of 1MB', response['responseMessage'])
        os.remove(document_maxsize)

        response = chargeback_document.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('008', response['responseCode'])
        self.assertEquals('Max Document Limit Per Case Reached', response['responseMessage'])


if __name__ == '__main__':
    unittest2.main()
