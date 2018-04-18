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
import sys

import unittest2
from vantivsdk.utils import VantivException

from vantivsdk import chargeback_retrieval, utils, chargeback_update

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

conf = utils.Configuration()
conf.url = 'https://services.vantivprelive.com/services/chargebacks/'


class TestChargebackRetrieval(unittest2.TestCase):

    cycle_first_chargeback = "First Chargeback"
    cycle_pre_arb_chargback = "Pre-Arbitration"
    cycle_arbitration_chargeback = "VISA Pre-Arbitration/Arbitration"
    cycle_issuer_decline_presab = "Issuer Declined Pre-Arbitration"
    activity_merchant_represent = "Merchant Represent"
    activity_merchant_accepts_liability = "Merchant Accepts Liability"
    activity_add_note = "Add Note"

    def test_1(self):

        response = chargeback_retrieval.get_chargebacks_by_date("2013-01-01", config=conf)
        cases = response['chargebackCase']

        # test_chargeback_case(self, cases[0], "1111111111", self.cycle_first_chargeback)
        test_chargeback_case(self, cases[1], "2222222222", self.cycle_first_chargeback)
        test_chargeback_case(self, cases[2], "3333333333", self.cycle_first_chargeback)
        test_chargeback_case(self, cases[3], "4444444444", self.cycle_first_chargeback)
        test_chargeback_case(self, cases[4], "5555555550", self.cycle_pre_arb_chargback)
        test_chargeback_case(self, cases[5], "5555555551", self.cycle_pre_arb_chargback)
        test_chargeback_case(self, cases[6], "5555555552", self.cycle_pre_arb_chargback)
        test_chargeback_case(self, cases[7], "6666666660", self.cycle_arbitration_chargeback)
        test_chargeback_case(self, cases[8], "7777777770", self.cycle_issuer_decline_presab)
        test_chargeback_case(self, cases[9], "7777777771", self.cycle_issuer_decline_presab)
        test_chargeback_case(self, cases[10], "7777777772", self.cycle_issuer_decline_presab)

    def test_2(self):
        case_id = get_case_id_for_arn("1111111111")
        chargeback_update.add_note_to_case(case_id, "Cert test2", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_add_note, activity['activityType'])
        self.assertEqual("Cert test2", activity['notes'])

    def test_3_1(self):
        case_id = get_case_id_for_arn("2222222222")
        chargeback_update.represent_case(case_id, "Cert test3_1", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_represent, activity['activityType'])
        self.assertEqual("Cert test3_1", activity['notes'])

    def test_3_2(self):
        case_id = get_case_id_for_arn("3333333333")
        chargeback_update.represent_case(case_id, "Cert test3_2", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_represent, activity['activityType'])
        self.assertEqual("Cert test3_2", activity['notes'])

    def test_4_and_5_1(self):
        case_id = get_case_id_for_arn("4444444444")
        chargeback_update.assume_liability(case_id, "Cert test4", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_accepts_liability, activity['activityType'])
        self.assertEqual("Cert test4", activity['notes'])

        self.assertRaises(VantivException, chargeback_update.assume_liability, case_id, "Cert test5_1", config=conf)

    def test5_2(self):
        self.assertRaises(VantivException, chargeback_retrieval.get_chargeback_by_case_id, 12345, config=conf)

    def test_6_1(self):
        case_id = get_case_id_for_arn("5555555550")
        chargeback_update.represent_case(case_id, "Cert test6_1", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_represent, activity['activityType'])
        self.assertEqual("Cert test6_1", activity['notes'])

    def test_6_2(self):
        case_id = get_case_id_for_arn("5555555551")
        chargeback_update.represent_case(case_id, "Cert test6_2", representment_amount=10051, config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_represent, activity['activityType'])
        self.assertEqual(10051, activity['settlementAmount'])
        self.assertEqual("Cert test6_2", activity['notes'])

    def test_7(self):
        case_id = get_case_id_for_arn("5555555552")
        chargeback_update.assume_liability(case_id, "Cert test7", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_accepts_liability, activity['activityType'])
        self.assertEqual("Cert test7", activity['notes'])

    def test_8(self):
        case_id = get_case_id_for_arn("6666666660")
        chargeback_update.assume_liability(case_id, "Cert test8", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_accepts_liability, activity['activityType'])
        self.assertEqual("Cert test8", activity['notes'])

    def test_9_1(self):
        case_id = get_case_id_for_arn("7777777770")
        chargeback_update.represent_case(case_id, "Cert test9_1", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_represent, activity['activityType'])
        self.assertEqual("Cert test9_1", activity['notes'])

    def test_9_2(self):
        case_id = get_case_id_for_arn("7777777771")
        chargeback_update.represent_case(case_id, "Cert test9_2", representment_amount=10071, config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_represent, activity['activityType'])
        self.assertEqual(10071, activity['settlementAmount'])
        self.assertEqual("Cert test9_2", activity['notes'])

    def test_10(self):
        case_id = get_case_id_for_arn("7777777772")
        chargeback_update.assume_liability(case_id, "Cert test10", config=conf)
        activity = get_last_activity(case_id)

        self.assertEqual(self.activity_merchant_accepts_liability, activity['activityType'])
        self.assertEqual("Cert test10", activity['notes'])


def test_chargeback_case(obj, chargeback_case, arn, chargeback_cycle):
    obj.assertEqual(arn, chargeback_case['acquirerReferenceNumber'])
    obj.assertEqual(chargeback_cycle, chargeback_case['cycle'])


def get_case_id_for_arn(arn):
    response = chargeback_retrieval.get_chargebacks_by_arn(arn, config=conf)
    return response['chargebackCase'][0]['caseId']


def get_last_activity(case_id):
    response = chargeback_retrieval.get_chargeback_by_case_id(case_id, config=conf)
    case = response['chargebackCase'][0]
    print(case)
    return case['activity'][0]


if __name__ == '__main__':
    unittest2.main()
