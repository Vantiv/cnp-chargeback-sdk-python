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
from unittest import mock
from vantivsdk import (utils, online, fields)
import six

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)


class TestOnline(unittest.TestCase):




    # @mock.patch.object(online, '_get_response')
    def test_request_return_format(self):
        param = fields.chargebackApiCase()
        self.assertRaises(utils.VantivException, online._get_response,  param.caseId, "caseId")

#         mock__http_request.return_value = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
# <chargebackRetrievalResponse xmlns="http://www.vantivcnp.com/chargebacks">
#     <transactionId>2111145419</transactionId>
#     <chargebackCase>
#         <caseId>1304283003</caseId>l
#         <merchantId>1304283</merchantId>
#         <dayIssuedByBank>2002-01-01</dayIssuedByBank>
#         <dateReceivedByVantivCnp>2017-10-02</dateReceivedByVantivCnp>
#         <vantivCnpTxnId>219016511913</vantivCnpTxnId>
#         <cycle>First Chargeback</cycle>
#         <orderId>12345</orderId>
#         <cardNumberLast4>0001</cardNumberLast4>
#         <cardType>VISA</cardType>
#         <chargebackAmount>20000</chargebackAmount>
#         <chargebackCurrencyType>USD</chargebackCurrencyType>
#         <originalTxnDay>2002-01-01</originalTxnDay>
#         <chargebackType>D</chargebackType>
#         <representedAmount>111</representedAmount>
#         <representedCurrencyType>USD</representedCurrencyType>
#         <reasonCode>0028</reasonCode>
#         <reasonCodeDescription>T&amp;E-Account Number Verification</reasonCodeDescription>
#         <currentQueue>Vantiv Outgoing</currentQueue>
#         <acquirerReferenceNumber>2222222222</acquirerReferenceNumber>
#         <chargebackReferenceNumber>bbbbbbbbbb</chargebackReferenceNumber>
#         <bin>410000</bin>
#         <paymentAmount>1010</paymentAmount>
#         <replyByDay>2002-02-05</replyByDay>
#         <activity>
#             <activityDate>2017-10-02</activityDate>
#             <activityType>Assign To Merchant</activityType>
#             <fromQueue>Litle</fromQueue>
#             <toQueue>Merchant Automated</toQueue>
#             <notes>Please work this case</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-02</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Merchant</fromQueue>
#             <toQueue>Merchant</toQueue>
#             <notes>testing chargebacks</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Merchant Represent</activityType>
#             <fromQueue>Merchant</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent 0000000011</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent 0000000011</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-06</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent testing</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>note333</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>note3773</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>Represent test5</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>sample test note</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>note333</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>sample test note3gfhhdghgh3</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-10</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>note333</notes>
#         </activity>
#         <activity>
#             <activityDate>2017-10-11</activityDate>
#             <activityType>Add Note</activityType>
#             <fromQueue>Litle Outgoing</fromQueue>
#             <toQueue>Litle Outgoing</toQueue>
#             <settlementAmount>111</settlementAmount>
#             <notes>jgsggsfd</notes>
#         </activity>
#     </chargebackCase>
# </chargebackRetrievalResponse>
#                 """
#         conf = utils.Configuration()
#         # return dict
#         response = online.request(request_type, request_body, param, conf)
#         self.assertEquals('1304283003', response['chargebackCase']['caseId'])
#         # self.assertIsInstance(response, dict)
#
#         # return xml string
#         response = online.request(request_type, request_body, param, conf, 'xml')
#         # self.assertIsInstance(response, str)
#
#         # return fields object.
#         # response = online.request(request_type, request_body, param, conf, 'object')
#         # self.assertEquals('0', response.response)


if __name__ == '__main__':
    unittest.main()
