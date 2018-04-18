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
        case_id = conf.merchantId + "001"
        response = chargebackDocument.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargebackDocument.upload_document(case_id, self.document_to_upload2, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargebackDocument.upload_document(case_id, self.document_to_upload3, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargebackDocument.list_documents(case_id, config=conf)
        document_list = response['documentIds']
        self.assertIn(self.document_to_upload1, document_list)
        self.assertIn(self.document_to_upload2, document_list)
        self.assertIn(self.document_to_upload3, document_list)

        document_to_retrieve = package_root + "/tests/test1.tiff"
        chargebackDocument.retrieve_document(case_id, "test.jpg", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        chargebackDocument.retrieve_document(case_id, "test.gif", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        chargebackDocument.retrieve_document(case_id, "test.pdf", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        response = chargebackDocument.replace_document(case_id, "test.jpg", self.document_to_upload4, config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        chargebackDocument.retrieve_document(case_id, "test.tiff", document_to_retrieve, config=conf)
        self.assertTrue(os.path.exists(document_to_retrieve))
        os.remove(document_to_retrieve)

        response = chargebackDocument.remove_document(case_id, "test.gif", config=conf)
        self.assertEquals('000', response['responseCode'])
        self.assertEquals('Success', response['responseMessage'])

        response = chargebackDocument.list_documents(case_id, config=conf)
        document_list = response['documentIds']
        self.assertIn(self.document_to_upload3, document_list)
        self.assertIn(self.document_to_upload4, document_list)

    def test_2(self):
        case_id = conf.merchantId + "002"

        response = chargebackDocument.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('010', response['responseCode'])
        self.assertEquals('Case not in valid cycle', response['responseMessage'])

    def test_3(self):
        case_id = conf.merchantId + "003"

        response = chargebackDocument.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('004', response['responseCode'])
        self.assertEquals('Case Not In Merchant Queue', response['responseMessage'])

    def test_4(self):
        case_id = conf.merchantId + "004"

        document_maxsize = package_root + "/tests/maxsize.tif"
        open(document_maxsize, "w+").close()

        response = chargebackDocument.upload_document(case_id, document_maxsize, config=conf)
        self.assertEquals('005', response['responseCode'])
        self.assertEquals('Document already exists', response['responseMessage'])
        os.remove(document_maxsize)

        document_maxsize = package_root + "/tests/maxsize1.tif"
        f = open(document_maxsize, "w+")
        f.seek(2050)
        f.write("\0")
        f.close()
        print(os.stat(document_maxsize).st_size)

        response = chargebackDocument.upload_document(case_id, document_maxsize, config=conf)
        self.assertEquals('005', response['responseCode'])
        self.assertEquals('Filesize exceeds limit of 1MB', response['responseMessage'])
        os.remove(document_maxsize)

        response = chargebackDocument.upload_document(case_id, self.document_to_upload1, config=conf)
        self.assertEquals('008', response['responseCode'])
        self.assertEquals('Max Document Limit Per Case Reached', response['responseMessage'])


if __name__ == '__main__':
    unittest2.main()
