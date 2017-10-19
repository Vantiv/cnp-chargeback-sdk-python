import os
import sys
import unittest2
from vantivsdk import fields
from vantivsdk import *

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

conf = utils.Configuration()


class merchant_upload(unittest2.TestCase):
    def upload_doc(self):
        param=fields.CTD_ANON_3()
        te=fields.Merchant()





if __name__ == '__main__':
    unittest2.main()
