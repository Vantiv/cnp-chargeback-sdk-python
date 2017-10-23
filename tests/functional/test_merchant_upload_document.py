import os
import sys
import unittest
from vantivsdk import fields_chargebackDocument
import requests
from requests.auth import HTTPBasicAuth


class merchant_upload(unittest.TestCase):

        param = fields_chargebackDocument.Merchant();
        param.id = u'01333078'
        param1 = fields_chargebackDocument.ChargebackCase();
        param1.id = u'01333078001'
        param2 = fields_chargebackDocument.Document()
        param2.id = u'test1'
        url = "http://prelive-pl-app1.litle.com:8048/services/chargebacks/documents/"
        files = {'media': open('000_puppy_picture.jpg', 'rb')}
        http_response = requests.post(url=url+param.id+"/"+param1.id, headers={"Content-Type": "image/jpeg"},
                                      auth=HTTPBasicAuth("GPGTWYPF", "p5Ky4r9W"), files = files)
        print("hellooo")
        print("Response :", http_response)



if __name__ == '__main__':
    unittest.main()
