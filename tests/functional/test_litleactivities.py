import os
import sys
import unittest

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

from vantivsdk import *

conf = utils.Configuration()

class TestActivity(unittest.TestCase):
    def test_simple_auth_with_card(self):
        authorization = fields.authorization()
        authorization.reportGroup = 'Planets'
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'
        authorization.id = 'thisisid'

        card = fields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1210'
        card.type = 'VI'

        authorization.card = card

        response = online.request(authorization, conf)
        self.assertEquals('000', response['authorizationResponse']['response'])
