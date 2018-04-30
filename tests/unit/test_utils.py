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
import random
import sys

import unittest2

from cnpsdk import (utils, communication)

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)


class TestUtils(unittest2.TestCase):
    def test_not_load_save(self):
        conf_ori = utils.Configuration()
        conf = utils.Configuration()
        conf.proxy = 'TestCase %d' % random.randint(0, 100)
        conf.url = 'TestCase %d' % random.randint(0, 100)
        conf.save()
        conf_new = utils.Configuration()
        conf_ori.save()
        self.assertEquals(conf.proxy, conf_new.proxy)
        self.assertEquals(conf.url, conf_new.url)
        self.assertNotEqual(conf_ori.url, conf_new.url)

    def test_get_file_content(self):
        test_file = package_root + "/tests/test.txt"
        with open(test_file, "w+") as f:
            f.write("this is a test!")

        data, content_type = communication.get_file_content(test_file)
        self.assertEqual("this is a test!", data)
        self.assertEqual("text/plain", content_type)
        os.remove(test_file)

    def test_neuter_xml(self):
        xml_string = "<token>test_user</token>"
        self.assertEqual("<token>****</token>", communication.neuter_xml(xml_string))

    def test_create_list(self):
        dict = {'test': 'value'}
        utils._create_list("test", dict)
        self.assertTrue(isinstance(dict['test'], list))
        self.assertEqual("value", dict['test'][0])

    def test_create_lists(self):
        activity_dict = {'activity': 'test_activity'}
        chargeback_dict = {'chargebackCase': activity_dict}

        utils._create_lists(chargeback_dict)
        self.assertTrue(isinstance(chargeback_dict['chargebackCase'], list))
        self.assertEqual(activity_dict, chargeback_dict['chargebackCase'][0])
        self.assertTrue(isinstance(activity_dict['activity'], list))
        self.assertEqual("test_activity", activity_dict['activity'][0])

    def test_convert_to_object(self):
        retrieval_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chargebackRetrievalResponse ' \
                             'xmlns="http://www.vantivcnp.com/chargebacks"><transactionId>1234567890</transactionId' \
                             '><chargebackCase><caseId>1333078000</caseId><merchantId>101</merchantId><activity' \
                             '><activityDate>2018-01-01</activityDate><activityType>Assign To ' \
                             'User</activityType><fromQueue>Vantiv</fromQueue><toQueue>Merchant</toQueue' \
                             '><settlementAmount>2002</settlementAmount><settlementCurrencyType>USD' \
                             '</settlementCurrencyType><notes>notes on ' \
                             'activity</notes></activity></chargebackCase></chargebackRetrievalResponse> '
        obj = utils.convert_to_obj(retrieval_response)
        self.assertEqual(obj.transactionId, 1234567890)
        self.assertEqual(obj.chargebackCase[0].caseId, 1333078000)
        self.assertEqual(obj.chargebackCase[0].merchantId, 101)
        self.assertEqual(obj.chargebackCase[0].activity[0].activityType, "Assign To User")

        update_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chargebackUpdateResponse ' \
                          'xmlns="http://www.vantivcnp.com/chargebacks"><transactionId>21260530003675</transactionId' \
                          '></chargebackUpdateResponse> '
        obj = utils.convert_to_obj(update_response)
        self.assertEqual(obj.transactionId, 21260530003675)

        document_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chargebackDocumentUploadResponse ' \
                            'xmlns="http://www.vantivcnp.com/chargebacks"><merchantId>999</merchantId><caseId>10000' \
                            '</caseId><documentId>logo.tiff</documentId><documentId>doc.tiff</documentId' \
                            '><responseCode>000</responseCode><responseMessage>Success</responseMessage' \
                            '></chargebackDocumentUploadResponse> '
        obj = utils.convert_to_obj(document_response)
        self.assertEqual(obj.caseId, 10000)
        self.assertEqual(obj.merchantId, 999)
        self.assertEqual(obj.documentId[0], "logo.tiff")
        self.assertEqual(obj.documentId[1], "doc.tiff")

    def test_convert_to_dict(self):
        retrieval_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chargebackRetrievalResponse ' \
                             'xmlns="http://www.vantivcnp.com/chargebacks"><transactionId>1234567890</transactionId' \
                             '><chargebackCase><caseId>1333078000</caseId><merchantId>01</merchantId><activity' \
                             '><activityDate>2018-01-01</activityDate><activityType>Assign To ' \
                             'User</activityType><fromQueue>Vantiv</fromQueue><toQueue>Merchant</toQueue' \
                             '><settlementAmount>2002</settlementAmount><settlementCurrencyType>USD' \
                             '</settlementCurrencyType><notes>notes on ' \
                             'activity</notes></activity></chargebackCase></chargebackRetrievalResponse> '
        response_dict = utils.convert_to_dict(retrieval_response, 'chargebackRetrievalResponse')
        self.assertEqual(response_dict['transactionId'], "1234567890")
        self.assertEqual(response_dict['chargebackCase'][0]['caseId'], "1333078000")
        self.assertEqual(response_dict['chargebackCase'][0]['merchantId'], "01")
        self.assertEqual(response_dict['chargebackCase'][0]['activity'][0]['activityType'], "Assign To User")

        update_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chargebackUpdateResponse ' \
                          'xmlns="http://www.vantivcnp.com/chargebacks"><transactionId>21260530003675</transactionId' \
                          '></chargebackUpdateResponse> '
        response_dict = utils.convert_to_dict(update_response, 'chargebackUpdateResponse')
        self.assertEqual(response_dict['transactionId'], "21260530003675")

        document_response = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><chargebackDocumentUploadResponse ' \
                            'xmlns="http://www.vantivcnp.com/chargebacks"><merchantId>999</merchantId><caseId>10000' \
                            '</caseId><documentId>logo.tiff</documentId><documentId>doc.tiff</documentId' \
                            '><responseCode>000</responseCode><responseMessage>Success</responseMessage' \
                            '></chargebackDocumentUploadResponse> '
        response_dict = utils.convert_to_dict(document_response, 'chargebackDocumentUploadResponse')
        self.assertEqual(response_dict['caseId'], "10000")
        self.assertEqual(response_dict['merchantId'], "999")
        self.assertEqual(response_dict['documentId'][0], "logo.tiff")
        self.assertEqual(response_dict['documentId'][1], "doc.tiff")


if __name__ == '__main__':
    unittest2.main()
