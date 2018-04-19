Vantiv eCommerce Python Chargeback SDK
=====================

About Vantiv eCommerce
------------
[Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Vantiv eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Vantiv eCommerce Python Chargeback SDK is a Python implementation of the [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) Chargeback API. This SDK was created to make it as easy as possible to manage your chargebacks using Vantiv eCommerce API. This SDK utilizes the HTTPS protocol to securely connect to Vantiv eCommerce. Using the SDK requires coordination with the Vantiv eCommerce team in order to be provided with credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated Vantiv eCommerce Chargeback API version (e.g., SDK v2.1.0 supports Vantiv eCommerce Chargeback API v2.1). Please see the Chargeback API reference guide to get more details on what the Vantiv eCommerce chargeback engine supports.

This SDK was implemented to support the Python programming language and was created by Vantiv eCommerce. Its intended use is for online and batch transaction processing utilizing your account on the Vantiv eCommerce payments engine.

See LICENSE file for details on using this software.

Please contact [Vantiv eCommerce](https://developer.vantiv.com/community/ecommerce) to receive valid merchant credentials in order to run tests successfully or if you require assistance in any way.  We are reachable at sdksupport@Vantiv.com

Dependencies
------------
* pyxb v1.2.5 : http://pyxb.sourceforge.net/
* paramiko v1.14.0: http://www.paramiko.org/
* requests v2.13.0: http://docs.python-requests.org/en/master/
* six v1.10.0: https://github.com/benjaminp/six
* xmltodict 0.10.2: https://github.com/martinblech/xmltodict

Setup
-----
1) To download and install:

Using pip 

>pip install CnpChargebackSdk

Without Pip

>git clone https://github.com/Vantiv/cnp-chargeback-sdk-python.git

>cd cnp-chargeback-sdk-python

checkout branch master for XML v2.x
>git checkout master

>python setup.py install

2) setup configurations

>chargeback_sdk_setup

3) Create a python file similar to:

```python
#Example for Chargeback SDK
from __future__ import print_function, unicode_literals

from vantivsdk import *

# Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
# variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
conf = utils.Configuration()

# Configuration need following attributes for online request:
# attributes = default value
# user = ''
# password = ''
# merchantId = ''
# reportGroup = 'Default Report Group'
# url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
# proxy = ''
# print_xml = False

# Initial Transaction.
transaction = fields.authorization()
transaction.orderId = '1'
transaction.amount = 10010
transaction.orderSource = 'ecommerce'
transaction.id = 'ThisIsRequiredby11'

# Create contact object
contact = fields.contact()
contact.name = 'John & Mary Smith'
contact.addressLine1 = '1 Main St.'
contact.city = 'Burlington'
contact.state = 'MA'
contact.zip = '01803-3747'
contact.country = 'USA'
# The type of billToAddress is contact
transaction.billToAddress = contact

# Create cardType object
card = fields.cardType()
card.number = '4100000000000000'
card.expDate = '1215'
card.cardValidationNum = '349'
card.type = 'VI'
# The type of card is cardType
transaction.card = card

# detail tax
detailTaxList = list()

detailTax = fields.detailTax()
detailTax.taxAmount = 100
detailTaxList.append(detailTax)

detailTax2 = fields.detailTax()
detailTax2.taxAmount = 200
detailTaxList.append(detailTax2)

enhancedData = fields.enhancedData()
enhancedData.detailTax = detailTaxList

transaction.enhancedData = enhancedData

# Send request to server and get response as dict
response = online.request(transaction, conf)

print('Message: %s' % response['authorizationResponse']['message'])
print('cnpTransaction ID: %s' % response['authorizationResponse']['cnpTxnId'])

# Configuration need following attributes for batch request:
# attributes = default value
# sftp_username = ''
# sftp_password = ''
# sftp_url = ''
# batch_requests_path = '/tmp/vantiv_sdk_batch_request'
# batch_response_path = '/tmp/vantiv_sdk_batch_response'
# fast_url = ''
# fast_ssl = True
# fast_port = ''
# id = ''

# Initial batch transactions container class
transactions = batch.Transactions()

# Add transaction to batch transactions container
transactions.add(transaction)

# Sent batch to server via socket and get response as dict
response = batch.stream(transactions, conf)

print('Message: %s' % response['batchResponse']['authorizationResponse']['message'])
print('cnpTransaction ID: %s' % response['batchResponse']['authorizationResponse']['cnpTxnId'])
```

```python
#Example for SDK, transaction presented by dict
from __future__ import print_function, unicode_literals

from vantivsdk import *

# Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
# variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
conf = utils.Configuration()

# Configuration need following attributes for online request:
# attributes = default value
# user = ''
# password = ''
# merchantId = ''
# reportGroup = 'Default Report Group'
# url = 'https://www.testvantivcnp.com/sandbox/communicator/online'
# proxy = ''
# print_xml = False

# Transaction presented by dict
txn_dict ={
    'authorization':{
        'orderId': '1',
        'amount': 10010,
        'orderSource': 'ecommerce',
        'id': 'ThisIsRequiredby11',
        'billToAddress': {
            'name': 'John & Mary Smith',
            'addressLine1': '1 Main St.',
            'city': 'Burlington',
            'state': 'MA',
            'zip': '01803-3747',
            'country': 'USA'
        },
        'card': {
            'number': '4100000000000000',
            'expDate': '1215',
            'cardValidationNum' : '349',
            'type': 'VI'
        },
        'enhancedData':{
            'detailTax': [
                {'taxAmount':100},
                {'taxAmount':200},
            ],
        }
    }
}

# Send request to server and get response as object
response = online.request(txn_dict, conf)

print('Message: %s' % response['batchResponse']['authorizationResponse']['message'])
print('cnpTransaction ID: %s' % response['batchResponse']['authorizationResponse']['cnpTxnId'])
```

Please contact Vantiv eCommerce with any further questions. You can reach us at SDKSupport@Vantiv.com
