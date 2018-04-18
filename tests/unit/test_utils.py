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

from vantivsdk import (utils, communication)

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)


class TestUtils(unittest2.TestCase):
    def test_not_load_save(self):
        conf_ori = utils.Configuration()
        conf = utils.Configuration()
        conf.proxy = 'TestCase %d' % random.randint(0,100)
        conf.url = 'TestCase %d' % random.randint(0,100)
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
        xml_string = "<user>test_user</user>"
        self.assertEqual("<user>****</user>", communication.neuter_xml(xml_string))

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

        document_id_dict = {'documentId': 'test_id'}
        utils._create_lists(document_id_dict)
        self.assertTrue(isinstance(document_id_dict['documentId'], list))
        self.assertEqual("test_id", document_id_dict['documentId'][0])


if __name__ == '__main__':
    unittest2.main()
