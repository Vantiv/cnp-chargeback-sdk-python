# ./fields.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f03bd2be92cca0df00d3d054794f8a47756ec009
# Generated 2017-10-03 10:02:09.415545 by PyXB version 1.2.2
# Namespace http://www.litle.com/schema

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:724388ba-a843-11e7-9b90-001a4a010704')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.2'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.litle.com/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.litle.com/schema}cycleType
class cycleType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cycleType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 72, 4)
    _Documentation = None
cycleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cycleType, enum_prefix=None)
cycleType.RETRIEVAL_REQUEST = cycleType._CF_enumeration.addEnumeration(unicode_value=u'RETRIEVAL_REQUEST', tag=u'RETRIEVAL_REQUEST')
cycleType.FIRST_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value=u'FIRST_CHARGEBACK', tag=u'FIRST_CHARGEBACK')
cycleType.REPRESENTMENT = cycleType._CF_enumeration.addEnumeration(unicode_value=u'REPRESENTMENT', tag=u'REPRESENTMENT')
cycleType.ARBITRATION_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value=u'ARBITRATION_CHARGEBACK', tag=u'ARBITRATION_CHARGEBACK')
cycleType.CHARGEBACK_REVERSAL = cycleType._CF_enumeration.addEnumeration(unicode_value=u'CHARGEBACK_REVERSAL', tag=u'CHARGEBACK_REVERSAL')
cycleType.PRE_ARB_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value=u'PRE_ARB_CHARGEBACK', tag=u'PRE_ARB_CHARGEBACK')
cycleType.ISSUER_ARB_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value=u'ISSUER_ARB_CHARGEBACK', tag=u'ISSUER_ARB_CHARGEBACK')
cycleType._InitializeFacetMap(cycleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'cycleType', cycleType)

# Atomic simple type: {http://www.litle.com/schema}chargebackType
class chargebackType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'chargebackType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 84, 4)
    _Documentation = None
chargebackType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=chargebackType, enum_prefix=None)
chargebackType.Deposit = chargebackType._CF_enumeration.addEnumeration(unicode_value=u'Deposit', tag=u'Deposit')
chargebackType.Refund = chargebackType._CF_enumeration.addEnumeration(unicode_value=u'Refund', tag=u'Refund')
chargebackType._InitializeFacetMap(chargebackType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'chargebackType', chargebackType)

# Atomic simple type: {http://www.litle.com/schema}activityType
class activityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'activityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 91, 4)
    _Documentation = None
activityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=activityType, enum_prefix=None)
activityType.Add_Note = activityType._CF_enumeration.addEnumeration(unicode_value=u'Add Note', tag=u'Add_Note')
activityType.Assign_To_Litle = activityType._CF_enumeration.addEnumeration(unicode_value=u'Assign To Litle', tag=u'Assign_To_Litle')
activityType.Assign_To_Merchant = activityType._CF_enumeration.addEnumeration(unicode_value=u'Assign To Merchant', tag=u'Assign_To_Merchant')
activityType.Assign_To_Merchant_Automated = activityType._CF_enumeration.addEnumeration(unicode_value=u'Assign To Merchant Automated', tag=u'Assign_To_Merchant_Automated')
activityType.File_Arbitration = activityType._CF_enumeration.addEnumeration(unicode_value=u'File Arbitration', tag=u'File_Arbitration')
activityType.File_Pre_arbitration = activityType._CF_enumeration.addEnumeration(unicode_value=u'File Pre-arbitration', tag=u'File_Pre_arbitration')
activityType.Litle_Accepts_Liability = activityType._CF_enumeration.addEnumeration(unicode_value=u'Litle Accepts Liability', tag=u'Litle_Accepts_Liability')
activityType.Litle_Represent = activityType._CF_enumeration.addEnumeration(unicode_value=u'Litle Represent', tag=u'Litle_Represent')
activityType.Litle_Respond = activityType._CF_enumeration.addEnumeration(unicode_value=u'Litle Respond', tag=u'Litle_Respond')
activityType.Merchant_Accepts_Liability = activityType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Accepts Liability', tag=u'Merchant_Accepts_Liability')
activityType.Merchant_Represent = activityType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Represent', tag=u'Merchant_Represent')
activityType.Merchant_Requests_Arbitration = activityType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Requests Arbitration', tag=u'Merchant_Requests_Arbitration')
activityType.Merchant_Respond = activityType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Respond', tag=u'Merchant_Respond')
activityType.Merchant_Respond___Sent_Credit = activityType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Respond - Sent Credit', tag=u'Merchant_Respond___Sent_Credit')
activityType.Merchant_Respond___Sent_Gift = activityType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Respond - Sent Gift', tag=u'Merchant_Respond___Sent_Gift')
activityType.Move_To_Litle_Error_Queue = activityType._CF_enumeration.addEnumeration(unicode_value=u'Move To Litle Error Queue', tag=u'Move_To_Litle_Error_Queue')
activityType.Receive_Network_Transaction = activityType._CF_enumeration.addEnumeration(unicode_value=u'Receive Network Transaction', tag=u'Receive_Network_Transaction')
activityType.Request_Declined = activityType._CF_enumeration.addEnumeration(unicode_value=u'Request Declined', tag=u'Request_Declined')
activityType.Send_Representment = activityType._CF_enumeration.addEnumeration(unicode_value=u'Send Representment', tag=u'Send_Representment')
activityType.Send_Retrieval_Request_Response = activityType._CF_enumeration.addEnumeration(unicode_value=u'Send Retrieval Request Response', tag=u'Send_Retrieval_Request_Response')
activityType.Successful_Arbitration_Case = activityType._CF_enumeration.addEnumeration(unicode_value=u'Successful Arbitration Case', tag=u'Successful_Arbitration_Case')
activityType.Successful_Pre_arbitration_Case = activityType._CF_enumeration.addEnumeration(unicode_value=u'Successful Pre-arbitration Case', tag=u'Successful_Pre_arbitration_Case')
activityType.Successful_PayPal_Case = activityType._CF_enumeration.addEnumeration(unicode_value=u'Successful PayPal Case', tag=u'Successful_PayPal_Case')
activityType.Auto_Represent = activityType._CF_enumeration.addEnumeration(unicode_value=u'Auto Represent', tag=u'Auto_Represent')
activityType.Attach_Document = activityType._CF_enumeration.addEnumeration(unicode_value=u'Attach Document', tag=u'Attach_Document')
activityType.Delete_Document = activityType._CF_enumeration.addEnumeration(unicode_value=u'Delete Document', tag=u'Delete_Document')
activityType.Update_Document = activityType._CF_enumeration.addEnumeration(unicode_value=u'Update Document', tag=u'Update_Document')
activityType.Attempted_to_Attach_Document = activityType._CF_enumeration.addEnumeration(unicode_value=u'Attempted to Attach Document', tag=u'Attempted_to_Attach_Document')
activityType.Network_Decision = activityType._CF_enumeration.addEnumeration(unicode_value=u'Network Decision', tag=u'Network_Decision')
activityType.Network_Declined = activityType._CF_enumeration.addEnumeration(unicode_value=u'Network Declined', tag=u'Network_Declined')
activityType._InitializeFacetMap(activityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'activityType', activityType)

# Atomic simple type: {http://www.litle.com/schema}queueType
class queueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'queueType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 126, 4)
    _Documentation = None
queueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=queueType, enum_prefix=None)
queueType.New = queueType._CF_enumeration.addEnumeration(unicode_value=u'New', tag=u'New')
queueType.Litle = queueType._CF_enumeration.addEnumeration(unicode_value=u'Litle', tag=u'Litle')
queueType.Litle_Outgoing = queueType._CF_enumeration.addEnumeration(unicode_value=u'Litle Outgoing', tag=u'Litle_Outgoing')
queueType.Litle_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value=u'Litle Assumed', tag=u'Litle_Assumed')
queueType.Litle_Error = queueType._CF_enumeration.addEnumeration(unicode_value=u'Litle Error', tag=u'Litle_Error')
queueType.Merchant = queueType._CF_enumeration.addEnumeration(unicode_value=u'Merchant', tag=u'Merchant')
queueType.Merchant_Automated = queueType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Automated', tag=u'Merchant_Automated')
queueType.Merchant_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Assumed', tag=u'Merchant_Assumed')
queueType.Network_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value=u'Network Assumed', tag=u'Network_Assumed')
queueType.Merchant_Arbitrate = queueType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Arbitrate', tag=u'Merchant_Arbitrate')
queueType.Pre_arbitrate = queueType._CF_enumeration.addEnumeration(unicode_value=u'Pre-arbitrate', tag=u'Pre_arbitrate')
queueType.Arbitrate = queueType._CF_enumeration.addEnumeration(unicode_value=u'Arbitrate', tag=u'Arbitrate')
queueType.PayPal_Hold___Represent = queueType._CF_enumeration.addEnumeration(unicode_value=u'PayPal Hold - Represent', tag=u'PayPal_Hold___Represent')
queueType.PayPal_Hold___Assume = queueType._CF_enumeration.addEnumeration(unicode_value=u'PayPal Hold - Assume', tag=u'PayPal_Hold___Assume')
queueType.Decision_Pending = queueType._CF_enumeration.addEnumeration(unicode_value=u'Decision Pending', tag=u'Decision_Pending')
queueType.Merchant_Auto_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value=u'Merchant Auto Assumed', tag=u'Merchant_Auto_Assumed')
queueType._InitializeFacetMap(queueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'queueType', queueType)

# Atomic simple type: {http://www.litle.com/schema}retrievalRequestType
class retrievalRequestType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'retrievalRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 191, 4)
    _Documentation = None
retrievalRequestType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=retrievalRequestType, enum_prefix=None)
retrievalRequestType.INQUIRY = retrievalRequestType._CF_enumeration.addEnumeration(unicode_value=u'INQUIRY', tag=u'INQUIRY')
retrievalRequestType.DISPUTE = retrievalRequestType._CF_enumeration.addEnumeration(unicode_value=u'DISPUTE', tag=u'DISPUTE')
retrievalRequestType._InitializeFacetMap(retrievalRequestType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'retrievalRequestType', retrievalRequestType)

# Atomic simple type: {http://www.litle.com/schema}fraudNotificationStatusType
class fraudNotificationStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 198, 1)
    _Documentation = None
fraudNotificationStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fraudNotificationStatusType, enum_prefix=None)
fraudNotificationStatusType.BEFORE = fraudNotificationStatusType._CF_enumeration.addEnumeration(unicode_value=u'BEFORE', tag=u'BEFORE')
fraudNotificationStatusType.AFTER = fraudNotificationStatusType._CF_enumeration.addEnumeration(unicode_value=u'AFTER', tag=u'AFTER')
fraudNotificationStatusType._InitializeFacetMap(fraudNotificationStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'fraudNotificationStatusType', fraudNotificationStatusType)

# Atomic simple type: {http://www.litle.com/schema}string20Type
class string20Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string20Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 14, 4)
    _Documentation = None
string20Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
string20Type._InitializeFacetMap(string20Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string20Type', string20Type)

# Atomic simple type: {http://www.litle.com/schema}versionType
class versionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'versionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 20, 4)
    _Documentation = None
versionType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
versionType._InitializeFacetMap(versionType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'versionType', versionType)

# Atomic simple type: {http://www.litle.com/schema}messageType
class messageType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'messageType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 26, 4)
    _Documentation = None
messageType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(512L))
messageType._InitializeFacetMap(messageType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'messageType', messageType)

# Atomic simple type: {http://www.litle.com/schema}string2Type
class string2Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string2Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 32, 4)
    _Documentation = None
string2Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
string2Type._InitializeFacetMap(string2Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string2Type', string2Type)

# Atomic simple type: {http://www.litle.com/schema}responseType
class responseType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'responseType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 38, 4)
    _Documentation = None
responseType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3L))
responseType._InitializeFacetMap(responseType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'responseType', responseType)

# Atomic simple type: {http://www.litle.com/schema}litleIdType
class litleIdType (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'litleIdType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 44, 4)
    _Documentation = None
litleIdType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(19L))
litleIdType._InitializeFacetMap(litleIdType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'litleIdType', litleIdType)

# Atomic simple type: {http://www.litle.com/schema}string25Type
class string25Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'string25Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 50, 4)
    _Documentation = None
string25Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25L))
string25Type._InitializeFacetMap(string25Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'string25Type', string25Type)

# Atomic simple type: {http://www.litle.com/schema}cardNumberLast4Type
class cardNumberLast4Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cardNumberLast4Type')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 56, 4)
    _Documentation = None
cardNumberLast4Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
cardNumberLast4Type._InitializeFacetMap(cardNumberLast4Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cardNumberLast4Type', cardNumberLast4Type)

# Atomic simple type: {http://www.litle.com/schema}virtualAuthenticationKeyData
class virtualAuthenticationKeyData (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyData')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 61, 4)
    _Documentation = None
virtualAuthenticationKeyData._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
virtualAuthenticationKeyData._InitializeFacetMap(virtualAuthenticationKeyData._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'virtualAuthenticationKeyData', virtualAuthenticationKeyData)

# Atomic simple type: {http://www.litle.com/schema}virtualAuthenticationKeyPresenceIndicator
class virtualAuthenticationKeyPresenceIndicator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'virtualAuthenticationKeyPresenceIndicator')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 67, 4)
    _Documentation = None
virtualAuthenticationKeyPresenceIndicator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
virtualAuthenticationKeyPresenceIndicator._InitializeFacetMap(virtualAuthenticationKeyPresenceIndicator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'virtualAuthenticationKeyPresenceIndicator', virtualAuthenticationKeyPresenceIndicator)

# Atomic simple type: {http://www.litle.com/schema}authorizationSourcePlatform
class authorizationSourcePlatform (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authorizationSourcePlatform')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 72, 4)
    _Documentation = None
authorizationSourcePlatform._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
authorizationSourcePlatform._InitializeFacetMap(authorizationSourcePlatform._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authorizationSourcePlatform', authorizationSourcePlatform)

# Atomic simple type: {http://www.litle.com/schema}addressIndicator
class addressIndicator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressIndicator')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 77, 4)
    _Documentation = None
addressIndicator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
addressIndicator._InitializeFacetMap(addressIndicator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'addressIndicator', addressIndicator)

# Atomic simple type: {http://www.litle.com/schema}authenticationResultType
class authenticationResultType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authenticationResultType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 82, 4)
    _Documentation = None
authenticationResultType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1L))
authenticationResultType._InitializeFacetMap(authenticationResultType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authenticationResultType', authenticationResultType)

# Atomic simple type: {http://www.litle.com/schema}methodOfPaymentTypeEnum
class methodOfPaymentTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'methodOfPaymentTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 88, 4)
    _Documentation = None
methodOfPaymentTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=methodOfPaymentTypeEnum, enum_prefix=None)
methodOfPaymentTypeEnum.MC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MC', tag=u'MC')
methodOfPaymentTypeEnum.VI = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VI', tag=u'VI')
methodOfPaymentTypeEnum.AX = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AX', tag=u'AX')
methodOfPaymentTypeEnum.DC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DC', tag=u'DC')
methodOfPaymentTypeEnum.DI = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DI', tag=u'DI')
methodOfPaymentTypeEnum.PP = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PP', tag=u'PP')
methodOfPaymentTypeEnum.JC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JC', tag=u'JC')
methodOfPaymentTypeEnum.BL = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BL', tag=u'BL')
methodOfPaymentTypeEnum._InitializeFacetMap(methodOfPaymentTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'methodOfPaymentTypeEnum', methodOfPaymentTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}transactionAmountType
class transactionAmountType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'transactionAmountType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 101, 4)
    _Documentation = None
transactionAmountType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(8L))
transactionAmountType._InitializeFacetMap(transactionAmountType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', u'transactionAmountType', transactionAmountType)

# Atomic simple type: {http://www.litle.com/schema}loanToValueEstimator
class loanToValueEstimator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'loanToValueEstimator')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 107, 4)
    _Documentation = None
loanToValueEstimator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
loanToValueEstimator._InitializeFacetMap(loanToValueEstimator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'loanToValueEstimator', loanToValueEstimator)

# Atomic simple type: {http://www.litle.com/schema}riskEstimator
class riskEstimator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'riskEstimator')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 112, 4)
    _Documentation = None
riskEstimator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
riskEstimator._InitializeFacetMap(riskEstimator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'riskEstimator', riskEstimator)

# Atomic simple type: {http://www.litle.com/schema}riskQueueAssignment
class riskQueueAssignment (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'riskQueueAssignment')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 117, 4)
    _Documentation = None
riskQueueAssignment._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8L))
riskQueueAssignment._InitializeFacetMap(riskQueueAssignment._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'riskQueueAssignment', riskQueueAssignment)

# Atomic simple type: {http://www.litle.com/schema}merchantIdentificationType
class merchantIdentificationType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'merchantIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 123, 4)
    _Documentation = None
merchantIdentificationType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
merchantIdentificationType._InitializeFacetMap(merchantIdentificationType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'merchantIdentificationType', merchantIdentificationType)

# Atomic simple type: {http://www.litle.com/schema}currencyCodeEnum
class currencyCodeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'currencyCodeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 129, 4)
    _Documentation = None
currencyCodeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=currencyCodeEnum, enum_prefix=None)
currencyCodeEnum.AUD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'AUD', tag=u'AUD')
currencyCodeEnum.CAD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'CAD', tag=u'CAD')
currencyCodeEnum.CHF = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'CHF', tag=u'CHF')
currencyCodeEnum.DKK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'DKK', tag=u'DKK')
currencyCodeEnum.EUR = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'EUR', tag=u'EUR')
currencyCodeEnum.GBP = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'GBP', tag=u'GBP')
currencyCodeEnum.HKD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'HKD', tag=u'HKD')
currencyCodeEnum.JPY = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'JPY', tag=u'JPY')
currencyCodeEnum.NOK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'NOK', tag=u'NOK')
currencyCodeEnum.NZD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'NZD', tag=u'NZD')
currencyCodeEnum.SEK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'SEK', tag=u'SEK')
currencyCodeEnum.SGD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'SGD', tag=u'SGD')
currencyCodeEnum.USD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value=u'USD', tag=u'USD')
currencyCodeEnum._InitializeFacetMap(currencyCodeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'currencyCodeEnum', currencyCodeEnum)

# Atomic simple type: {http://www.litle.com/schema}countryTypeEnum
class countryTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'countryTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 147, 4)
    _Documentation = None
countryTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=countryTypeEnum, enum_prefix=None)
countryTypeEnum.USA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'USA', tag=u'USA')
countryTypeEnum.AF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AF', tag=u'AF')
countryTypeEnum.AX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AX', tag=u'AX')
countryTypeEnum.AL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AL', tag=u'AL')
countryTypeEnum.DZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DZ', tag=u'DZ')
countryTypeEnum.AS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AS', tag=u'AS')
countryTypeEnum.AD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AD', tag=u'AD')
countryTypeEnum.AO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AO', tag=u'AO')
countryTypeEnum.AI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AI', tag=u'AI')
countryTypeEnum.AQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AQ', tag=u'AQ')
countryTypeEnum.AG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AG', tag=u'AG')
countryTypeEnum.AR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AR', tag=u'AR')
countryTypeEnum.AM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AM', tag=u'AM')
countryTypeEnum.AW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AW', tag=u'AW')
countryTypeEnum.AU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AU', tag=u'AU')
countryTypeEnum.AT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AT', tag=u'AT')
countryTypeEnum.AZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AZ', tag=u'AZ')
countryTypeEnum.BS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BS', tag=u'BS')
countryTypeEnum.BH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BH', tag=u'BH')
countryTypeEnum.BD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BD', tag=u'BD')
countryTypeEnum.BB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BB', tag=u'BB')
countryTypeEnum.BY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BY', tag=u'BY')
countryTypeEnum.BE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BE', tag=u'BE')
countryTypeEnum.BZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BZ', tag=u'BZ')
countryTypeEnum.BJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BJ', tag=u'BJ')
countryTypeEnum.BM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BM', tag=u'BM')
countryTypeEnum.BT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BT', tag=u'BT')
countryTypeEnum.BO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BO', tag=u'BO')
countryTypeEnum.BA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BA', tag=u'BA')
countryTypeEnum.BW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BW', tag=u'BW')
countryTypeEnum.BV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BV', tag=u'BV')
countryTypeEnum.BR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BR', tag=u'BR')
countryTypeEnum.IO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IO', tag=u'IO')
countryTypeEnum.BN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BN', tag=u'BN')
countryTypeEnum.BG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BG', tag=u'BG')
countryTypeEnum.BF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BF', tag=u'BF')
countryTypeEnum.BI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BI', tag=u'BI')
countryTypeEnum.KH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KH', tag=u'KH')
countryTypeEnum.CM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CM', tag=u'CM')
countryTypeEnum.CA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CA', tag=u'CA')
countryTypeEnum.CV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CV', tag=u'CV')
countryTypeEnum.KY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KY', tag=u'KY')
countryTypeEnum.CF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CF', tag=u'CF')
countryTypeEnum.TD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TD', tag=u'TD')
countryTypeEnum.CL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CL', tag=u'CL')
countryTypeEnum.CN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CN', tag=u'CN')
countryTypeEnum.CX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CX', tag=u'CX')
countryTypeEnum.CC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CC', tag=u'CC')
countryTypeEnum.CO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CO', tag=u'CO')
countryTypeEnum.KM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KM', tag=u'KM')
countryTypeEnum.CG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CG', tag=u'CG')
countryTypeEnum.CD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CD', tag=u'CD')
countryTypeEnum.CK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CK', tag=u'CK')
countryTypeEnum.CR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CR', tag=u'CR')
countryTypeEnum.CI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CI', tag=u'CI')
countryTypeEnum.HR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HR', tag=u'HR')
countryTypeEnum.CU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CU', tag=u'CU')
countryTypeEnum.CY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CY', tag=u'CY')
countryTypeEnum.CZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CZ', tag=u'CZ')
countryTypeEnum.DK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DK', tag=u'DK')
countryTypeEnum.DJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DJ', tag=u'DJ')
countryTypeEnum.DM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DM', tag=u'DM')
countryTypeEnum.DO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DO', tag=u'DO')
countryTypeEnum.TL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TL', tag=u'TL')
countryTypeEnum.EC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EC', tag=u'EC')
countryTypeEnum.EG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EG', tag=u'EG')
countryTypeEnum.SV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SV', tag=u'SV')
countryTypeEnum.GQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GQ', tag=u'GQ')
countryTypeEnum.ER = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ER', tag=u'ER')
countryTypeEnum.EE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EE', tag=u'EE')
countryTypeEnum.ET = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ET', tag=u'ET')
countryTypeEnum.FK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FK', tag=u'FK')
countryTypeEnum.FO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FO', tag=u'FO')
countryTypeEnum.FJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FJ', tag=u'FJ')
countryTypeEnum.FI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FI', tag=u'FI')
countryTypeEnum.FR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FR', tag=u'FR')
countryTypeEnum.GF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GF', tag=u'GF')
countryTypeEnum.PF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PF', tag=u'PF')
countryTypeEnum.TF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TF', tag=u'TF')
countryTypeEnum.GA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GA', tag=u'GA')
countryTypeEnum.GM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GM', tag=u'GM')
countryTypeEnum.GE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GE', tag=u'GE')
countryTypeEnum.DE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'DE', tag=u'DE')
countryTypeEnum.GH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GH', tag=u'GH')
countryTypeEnum.GI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GI', tag=u'GI')
countryTypeEnum.GR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GR', tag=u'GR')
countryTypeEnum.GL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GL', tag=u'GL')
countryTypeEnum.GD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GD', tag=u'GD')
countryTypeEnum.GP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GP', tag=u'GP')
countryTypeEnum.GU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GU', tag=u'GU')
countryTypeEnum.GT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GT', tag=u'GT')
countryTypeEnum.GG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GG', tag=u'GG')
countryTypeEnum.GN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GN', tag=u'GN')
countryTypeEnum.GW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GW', tag=u'GW')
countryTypeEnum.GY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GY', tag=u'GY')
countryTypeEnum.HT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HT', tag=u'HT')
countryTypeEnum.HM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HM', tag=u'HM')
countryTypeEnum.HN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HN', tag=u'HN')
countryTypeEnum.HK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HK', tag=u'HK')
countryTypeEnum.HU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'HU', tag=u'HU')
countryTypeEnum.IS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IS', tag=u'IS')
countryTypeEnum.IN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IN', tag=u'IN')
countryTypeEnum.ID = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ID', tag=u'ID')
countryTypeEnum.IR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IR', tag=u'IR')
countryTypeEnum.IQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IQ', tag=u'IQ')
countryTypeEnum.IE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IE', tag=u'IE')
countryTypeEnum.IM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IM', tag=u'IM')
countryTypeEnum.IL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IL', tag=u'IL')
countryTypeEnum.IT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'IT', tag=u'IT')
countryTypeEnum.JM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JM', tag=u'JM')
countryTypeEnum.JP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JP', tag=u'JP')
countryTypeEnum.JE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JE', tag=u'JE')
countryTypeEnum.JO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'JO', tag=u'JO')
countryTypeEnum.KZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KZ', tag=u'KZ')
countryTypeEnum.KE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KE', tag=u'KE')
countryTypeEnum.KI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KI', tag=u'KI')
countryTypeEnum.KP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KP', tag=u'KP')
countryTypeEnum.KR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KR', tag=u'KR')
countryTypeEnum.KW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KW', tag=u'KW')
countryTypeEnum.KG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KG', tag=u'KG')
countryTypeEnum.LA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LA', tag=u'LA')
countryTypeEnum.LV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LV', tag=u'LV')
countryTypeEnum.LB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LB', tag=u'LB')
countryTypeEnum.LS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LS', tag=u'LS')
countryTypeEnum.LR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LR', tag=u'LR')
countryTypeEnum.LY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LY', tag=u'LY')
countryTypeEnum.LI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LI', tag=u'LI')
countryTypeEnum.LT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LT', tag=u'LT')
countryTypeEnum.LU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LU', tag=u'LU')
countryTypeEnum.MO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MO', tag=u'MO')
countryTypeEnum.MK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MK', tag=u'MK')
countryTypeEnum.MG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MG', tag=u'MG')
countryTypeEnum.MW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MW', tag=u'MW')
countryTypeEnum.MY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MY', tag=u'MY')
countryTypeEnum.MV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MV', tag=u'MV')
countryTypeEnum.ML = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ML', tag=u'ML')
countryTypeEnum.MT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MT', tag=u'MT')
countryTypeEnum.MH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MH', tag=u'MH')
countryTypeEnum.MQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MQ', tag=u'MQ')
countryTypeEnum.MR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MR', tag=u'MR')
countryTypeEnum.MU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MU', tag=u'MU')
countryTypeEnum.YT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'YT', tag=u'YT')
countryTypeEnum.MX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MX', tag=u'MX')
countryTypeEnum.FM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'FM', tag=u'FM')
countryTypeEnum.MD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MD', tag=u'MD')
countryTypeEnum.MC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MC', tag=u'MC')
countryTypeEnum.MN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MN', tag=u'MN')
countryTypeEnum.MS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MS', tag=u'MS')
countryTypeEnum.MA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MA', tag=u'MA')
countryTypeEnum.MZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MZ', tag=u'MZ')
countryTypeEnum.MM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MM', tag=u'MM')
countryTypeEnum.NA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NA', tag=u'NA')
countryTypeEnum.NR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NR', tag=u'NR')
countryTypeEnum.NP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NP', tag=u'NP')
countryTypeEnum.NL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NL', tag=u'NL')
countryTypeEnum.AN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AN', tag=u'AN')
countryTypeEnum.NC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NC', tag=u'NC')
countryTypeEnum.NZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NZ', tag=u'NZ')
countryTypeEnum.NI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NI', tag=u'NI')
countryTypeEnum.NE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NE', tag=u'NE')
countryTypeEnum.NG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NG', tag=u'NG')
countryTypeEnum.NU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NU', tag=u'NU')
countryTypeEnum.NF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NF', tag=u'NF')
countryTypeEnum.MP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MP', tag=u'MP')
countryTypeEnum.NO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'NO', tag=u'NO')
countryTypeEnum.OM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'OM', tag=u'OM')
countryTypeEnum.PK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PK', tag=u'PK')
countryTypeEnum.PW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PW', tag=u'PW')
countryTypeEnum.PS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PS', tag=u'PS')
countryTypeEnum.PA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PA', tag=u'PA')
countryTypeEnum.PG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PG', tag=u'PG')
countryTypeEnum.PY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PY', tag=u'PY')
countryTypeEnum.PE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PE', tag=u'PE')
countryTypeEnum.PH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PH', tag=u'PH')
countryTypeEnum.PN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PN', tag=u'PN')
countryTypeEnum.PL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PL', tag=u'PL')
countryTypeEnum.PT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PT', tag=u'PT')
countryTypeEnum.PR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PR', tag=u'PR')
countryTypeEnum.QA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'QA', tag=u'QA')
countryTypeEnum.RE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RE', tag=u'RE')
countryTypeEnum.RO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RO', tag=u'RO')
countryTypeEnum.RU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RU', tag=u'RU')
countryTypeEnum.RW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RW', tag=u'RW')
countryTypeEnum.BL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'BL', tag=u'BL')
countryTypeEnum.KN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'KN', tag=u'KN')
countryTypeEnum.LC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LC', tag=u'LC')
countryTypeEnum.MF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'MF', tag=u'MF')
countryTypeEnum.VC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VC', tag=u'VC')
countryTypeEnum.WS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'WS', tag=u'WS')
countryTypeEnum.SM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SM', tag=u'SM')
countryTypeEnum.ST = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ST', tag=u'ST')
countryTypeEnum.SA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SA', tag=u'SA')
countryTypeEnum.SN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SN', tag=u'SN')
countryTypeEnum.SC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SC', tag=u'SC')
countryTypeEnum.SL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SL', tag=u'SL')
countryTypeEnum.SG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SG', tag=u'SG')
countryTypeEnum.SK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SK', tag=u'SK')
countryTypeEnum.SI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SI', tag=u'SI')
countryTypeEnum.SB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SB', tag=u'SB')
countryTypeEnum.SO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SO', tag=u'SO')
countryTypeEnum.ZA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ZA', tag=u'ZA')
countryTypeEnum.GS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GS', tag=u'GS')
countryTypeEnum.ES = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ES', tag=u'ES')
countryTypeEnum.LK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'LK', tag=u'LK')
countryTypeEnum.SH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SH', tag=u'SH')
countryTypeEnum.PM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'PM', tag=u'PM')
countryTypeEnum.SD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SD', tag=u'SD')
countryTypeEnum.SR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SR', tag=u'SR')
countryTypeEnum.SJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SJ', tag=u'SJ')
countryTypeEnum.SZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SZ', tag=u'SZ')
countryTypeEnum.SE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SE', tag=u'SE')
countryTypeEnum.CH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'CH', tag=u'CH')
countryTypeEnum.SY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'SY', tag=u'SY')
countryTypeEnum.TW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TW', tag=u'TW')
countryTypeEnum.TJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TJ', tag=u'TJ')
countryTypeEnum.TZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TZ', tag=u'TZ')
countryTypeEnum.TH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TH', tag=u'TH')
countryTypeEnum.TG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TG', tag=u'TG')
countryTypeEnum.TK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TK', tag=u'TK')
countryTypeEnum.TO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TO', tag=u'TO')
countryTypeEnum.TT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TT', tag=u'TT')
countryTypeEnum.TN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TN', tag=u'TN')
countryTypeEnum.TR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TR', tag=u'TR')
countryTypeEnum.TM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TM', tag=u'TM')
countryTypeEnum.TC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TC', tag=u'TC')
countryTypeEnum.TV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'TV', tag=u'TV')
countryTypeEnum.UG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UG', tag=u'UG')
countryTypeEnum.UA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UA', tag=u'UA')
countryTypeEnum.AE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'AE', tag=u'AE')
countryTypeEnum.GB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'GB', tag=u'GB')
countryTypeEnum.US = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'US', tag=u'US')
countryTypeEnum.UM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UM', tag=u'UM')
countryTypeEnum.UY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UY', tag=u'UY')
countryTypeEnum.UZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'UZ', tag=u'UZ')
countryTypeEnum.VU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VU', tag=u'VU')
countryTypeEnum.VA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VA', tag=u'VA')
countryTypeEnum.VE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VE', tag=u'VE')
countryTypeEnum.VN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VN', tag=u'VN')
countryTypeEnum.VG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VG', tag=u'VG')
countryTypeEnum.VI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'VI', tag=u'VI')
countryTypeEnum.WF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'WF', tag=u'WF')
countryTypeEnum.EH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'EH', tag=u'EH')
countryTypeEnum.YE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'YE', tag=u'YE')
countryTypeEnum.ZM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ZM', tag=u'ZM')
countryTypeEnum.ZW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ZW', tag=u'ZW')
countryTypeEnum.RS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'RS', tag=u'RS')
countryTypeEnum.ME = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value=u'ME', tag=u'ME')
countryTypeEnum._InitializeFacetMap(countryTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'countryTypeEnum', countryTypeEnum)

# Atomic simple type: {http://www.litle.com/schema}addressLineType
class addressLineType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressLineType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 399, 4)
    _Documentation = None
addressLineType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35L))
addressLineType._InitializeFacetMap(addressLineType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'addressLineType', addressLineType)

# Atomic simple type: {http://www.litle.com/schema}cityType
class cityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cityType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 404, 4)
    _Documentation = None
cityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35L))
cityType._InitializeFacetMap(cityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cityType', cityType)

# Atomic simple type: {http://www.litle.com/schema}customBillingCityType
class customBillingCityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customBillingCityType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 409, 4)
    _Documentation = None
customBillingCityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35L))
customBillingCityType._InitializeFacetMap(customBillingCityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'customBillingCityType', customBillingCityType)

# Atomic simple type: {http://www.litle.com/schema}stateType
class stateType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'stateType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 414, 4)
    _Documentation = None
stateType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30L))
stateType._InitializeFacetMap(stateType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'stateType', stateType)

# Atomic simple type: {http://www.litle.com/schema}zipType
class zipType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'zipType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 419, 4)
    _Documentation = None
zipType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
zipType._InitializeFacetMap(zipType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'zipType', zipType)

# Atomic simple type: {http://www.litle.com/schema}emailType
class emailType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'emailType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 425, 4)
    _Documentation = None
emailType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
emailType._InitializeFacetMap(emailType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'emailType', emailType)

# Atomic simple type: {http://www.litle.com/schema}phoneType
class phoneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'phoneType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 430, 4)
    _Documentation = None
phoneType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
phoneType._InitializeFacetMap(phoneType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'phoneType', phoneType)

# Atomic simple type: {http://www.litle.com/schema}nameType
class nameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'nameType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 435, 4)
    _Documentation = None
nameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
nameType._InitializeFacetMap(nameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'nameType', nameType)

# Atomic simple type: {http://www.litle.com/schema}cvNumType
class cvNumType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'cvNumType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 440, 4)
    _Documentation = None
cvNumType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4L))
cvNumType._InitializeFacetMap(cvNumType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'cvNumType', cvNumType)

# Atomic simple type: {http://www.litle.com/schema}authCodeType
class authCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'authCodeType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 445, 4)
    _Documentation = None
authCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6L))
authCodeType._InitializeFacetMap(authCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'authCodeType', authCodeType)

# Atomic simple type: {http://www.litle.com/schema}customerIdType
class customerIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customerIdType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 450, 4)
    _Documentation = None
customerIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
customerIdType._InitializeFacetMap(customerIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'customerIdType', customerIdType)

# Atomic simple type: {http://www.litle.com/schema}customBillingUrlType
class customBillingUrlType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'customBillingUrlType')
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 455, 4)
    _Documentation = None
customBillingUrlType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13L))
customBillingUrlType._CF_pattern = pyxb.binding.facets.CF_pattern()
customBillingUrlType._CF_pattern.addPattern(pattern=u'[A-Z,a-z,0-9,/,\\-,_,.]*')
customBillingUrlType._InitializeFacetMap(customBillingUrlType._CF_maxLength,
   customBillingUrlType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'customBillingUrlType', customBillingUrlType)

# Complex type {http://www.litle.com/schema}caseActivityType with content type ELEMENT_ONLY
class caseActivityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.litle.com/schema}caseActivityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'caseActivityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseId uses Python identifier caseId
    __caseId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseId'), 'caseId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacaseId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 39, 12), )

    
    caseId = property(__caseId.value, __caseId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantId uses Python identifier merchantId
    __merchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'merchantId'), 'merchantId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemamerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 40, 12), )

    
    merchantId = property(__merchantId.value, __merchantId.set, None, None)

    
    # Element {http://www.litle.com/schema}dayIssuedByBank uses Python identifier dayIssuedByBank
    __dayIssuedByBank = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dayIssuedByBank'), 'dayIssuedByBank', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemadayIssuedByBank', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 41, 12), )

    
    dayIssuedByBank = property(__dayIssuedByBank.value, __dayIssuedByBank.set, None, None)

    
    # Element {http://www.litle.com/schema}dayReceivedByLitle uses Python identifier dayReceivedByLitle
    __dayReceivedByLitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dayReceivedByLitle'), 'dayReceivedByLitle', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemadayReceivedByLitle', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 42, 12), )

    
    dayReceivedByLitle = property(__dayReceivedByLitle.value, __dayReceivedByLitle.set, None, None)

    
    # Element {http://www.litle.com/schema}cycle uses Python identifier cycle
    __cycle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cycle'), 'cycle', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacycle', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 43, 12), )

    
    cycle = property(__cycle.value, __cycle.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemalitleTxnId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 44, 12), )

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantTxnId uses Python identifier merchantTxnId
    __merchantTxnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'merchantTxnId'), 'merchantTxnId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemamerchantTxnId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 45, 12), )

    
    merchantTxnId = property(__merchantTxnId.value, __merchantTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'orderId'), 'orderId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaorderId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 46, 12), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}cardNumberLast4 uses Python identifier cardNumberLast4
    __cardNumberLast4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cardNumberLast4'), 'cardNumberLast4', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacardNumberLast4', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 47, 12), )

    
    cardNumberLast4 = property(__cardNumberLast4.value, __cardNumberLast4.set, None, None)

    
    # Element {http://www.litle.com/schema}cardType uses Python identifier cardType
    __cardType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'cardType'), 'cardType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacardType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 48, 12), )

    
    cardType = property(__cardType.value, __cardType.set, None, None)

    
    # Element {http://www.litle.com/schema}chargebackAmount uses Python identifier chargebackAmount
    __chargebackAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'chargebackAmount'), 'chargebackAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemachargebackAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 49, 12), )

    
    chargebackAmount = property(__chargebackAmount.value, __chargebackAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}chargebackCurrencyType uses Python identifier chargebackCurrencyType
    __chargebackCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'chargebackCurrencyType'), 'chargebackCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemachargebackCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 50, 12), )

    
    chargebackCurrencyType = property(__chargebackCurrencyType.value, __chargebackCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}originalTransactionDay uses Python identifier originalTransactionDay
    __originalTransactionDay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'originalTransactionDay'), 'originalTransactionDay', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaoriginalTransactionDay', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 51, 12), )

    
    originalTransactionDay = property(__originalTransactionDay.value, __originalTransactionDay.set, None, None)

    
    # Element {http://www.litle.com/schema}chargebackType uses Python identifier chargebackType
    __chargebackType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'chargebackType'), 'chargebackType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemachargebackType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 52, 12), )

    
    chargebackType = property(__chargebackType.value, __chargebackType.set, None, None)

    
    # Element {http://www.litle.com/schema}activityType uses Python identifier activityType
    __activityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'activityType'), 'activityType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaactivityType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 53, 12), )

    
    activityType = property(__activityType.value, __activityType.set, None, None)

    
    # Element {http://www.litle.com/schema}representedAmount uses Python identifier representedAmount
    __representedAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'representedAmount'), 'representedAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemarepresentedAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12), )

    
    representedAmount = property(__representedAmount.value, __representedAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}representedCurrencyType uses Python identifier representedCurrencyType
    __representedCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'representedCurrencyType'), 'representedCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemarepresentedCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12), )

    
    representedCurrencyType = property(__representedCurrencyType.value, __representedCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}preArbAmount uses Python identifier preArbAmount
    __preArbAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'preArbAmount'), 'preArbAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemapreArbAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12), )

    
    preArbAmount = property(__preArbAmount.value, __preArbAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}preArbCurrencyType uses Python identifier preArbCurrencyType
    __preArbCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'preArbCurrencyType'), 'preArbCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemapreArbCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12), )

    
    preArbCurrencyType = property(__preArbCurrencyType.value, __preArbCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}reasonCode uses Python identifier reasonCode
    __reasonCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reasonCode'), 'reasonCode', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemareasonCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 58, 12), )

    
    reasonCode = property(__reasonCode.value, __reasonCode.set, None, None)

    
    # Element {http://www.litle.com/schema}reasonCodeDescription uses Python identifier reasonCodeDescription
    __reasonCodeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'reasonCodeDescription'), 'reasonCodeDescription', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemareasonCodeDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 59, 12), )

    
    reasonCodeDescription = property(__reasonCodeDescription.value, __reasonCodeDescription.set, None, None)

    
    # Element {http://www.litle.com/schema}fromQueue uses Python identifier fromQueue
    __fromQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fromQueue'), 'fromQueue', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemafromQueue', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 60, 12), )

    
    fromQueue = property(__fromQueue.value, __fromQueue.set, None, None)

    
    # Element {http://www.litle.com/schema}toQueue uses Python identifier toQueue
    __toQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'toQueue'), 'toQueue', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschematoQueue', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 61, 12), )

    
    toQueue = property(__toQueue.value, __toQueue.set, None, None)

    
    # Element {http://www.litle.com/schema}currentQueue uses Python identifier currentQueue
    __currentQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'currentQueue'), 'currentQueue', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacurrentQueue', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 62, 12), )

    
    currentQueue = property(__currentQueue.value, __currentQueue.set, None, None)

    
    # Element {http://www.litle.com/schema}settlementAmount uses Python identifier settlementAmount
    __settlementAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'settlementAmount'), 'settlementAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemasettlementAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12), )

    
    settlementAmount = property(__settlementAmount.value, __settlementAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}settlementCurrencyType uses Python identifier settlementCurrencyType
    __settlementCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'settlementCurrencyType'), 'settlementCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemasettlementCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12), )

    
    settlementCurrencyType = property(__settlementCurrencyType.value, __settlementCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'notes'), 'notes', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemanotes', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudNotificationStatus uses Python identifier fraudNotificationStatus
    __fraudNotificationStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationStatus'), 'fraudNotificationStatus', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemafraudNotificationStatus', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12), )

    
    fraudNotificationStatus = property(__fraudNotificationStatus.value, __fraudNotificationStatus.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudNotificationDate uses Python identifier fraudNotificationDate
    __fraudNotificationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationDate'), 'fraudNotificationDate', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemafraudNotificationDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12), )

    
    fraudNotificationDate = property(__fraudNotificationDate.value, __fraudNotificationDate.set, None, None)

    
    # Element {http://www.litle.com/schema}retrievalRequestType uses Python identifier retrievalRequestType
    __retrievalRequestType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'retrievalRequestType'), 'retrievalRequestType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaretrievalRequestType', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12), )

    
    retrievalRequestType = property(__retrievalRequestType.value, __retrievalRequestType.set, None, None)

    _ElementMap.update({
        __caseId.name() : __caseId,
        __merchantId.name() : __merchantId,
        __dayIssuedByBank.name() : __dayIssuedByBank,
        __dayReceivedByLitle.name() : __dayReceivedByLitle,
        __cycle.name() : __cycle,
        __litleTxnId.name() : __litleTxnId,
        __merchantTxnId.name() : __merchantTxnId,
        __orderId.name() : __orderId,
        __cardNumberLast4.name() : __cardNumberLast4,
        __cardType.name() : __cardType,
        __chargebackAmount.name() : __chargebackAmount,
        __chargebackCurrencyType.name() : __chargebackCurrencyType,
        __originalTransactionDay.name() : __originalTransactionDay,
        __chargebackType.name() : __chargebackType,
        __activityType.name() : __activityType,
        __representedAmount.name() : __representedAmount,
        __representedCurrencyType.name() : __representedCurrencyType,
        __preArbAmount.name() : __preArbAmount,
        __preArbCurrencyType.name() : __preArbCurrencyType,
        __reasonCode.name() : __reasonCode,
        __reasonCodeDescription.name() : __reasonCodeDescription,
        __fromQueue.name() : __fromQueue,
        __toQueue.name() : __toQueue,
        __currentQueue.name() : __currentQueue,
        __settlementAmount.name() : __settlementAmount,
        __settlementCurrencyType.name() : __settlementCurrencyType,
        __notes.name() : __notes,
        __fraudNotificationStatus.name() : __fraudNotificationStatus,
        __fraudNotificationDate.name() : __fraudNotificationDate,
        __retrievalRequestType.name() : __retrievalRequestType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'caseActivityType', caseActivityType)


# Complex type {http://www.litle.com/schema}caseUpdateType with content type ELEMENT_ONLY
class caseUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.litle.com/schema}caseUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'caseUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseId uses Python identifier caseId
    __caseId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseId'), 'caseId', '__httpwww_litle_comschema_caseUpdateType_httpwww_litle_comschemacaseId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 162, 12), )

    
    caseId = property(__caseId.value, __caseId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantActivityId uses Python identifier merchantActivityId
    __merchantActivityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'merchantActivityId'), 'merchantActivityId', '__httpwww_litle_comschema_caseUpdateType_httpwww_litle_comschemamerchantActivityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 163, 12), )

    
    merchantActivityId = property(__merchantActivityId.value, __merchantActivityId.set, None, None)

    
    # Element {http://www.litle.com/schema}activity uses Python identifier activity
    __activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'activity'), 'activity', '__httpwww_litle_comschema_caseUpdateType_httpwww_litle_comschemaactivity', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 164, 12), )

    
    activity = property(__activity.value, __activity.set, None, None)

    _ElementMap.update({
        __caseId.name() : __caseId,
        __merchantActivityId.name() : __merchantActivityId,
        __activity.name() : __activity
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'caseUpdateType', caseUpdateType)


# Complex type {http://www.litle.com/schema}caseUpdateResponseType with content type ELEMENT_ONLY
class caseUpdateResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.litle.com/schema}caseUpdateResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'caseUpdateResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 183, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}phoenixTxnId uses Python identifier phoenixTxnId
    __phoenixTxnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'phoenixTxnId'), 'phoenixTxnId', '__httpwww_litle_comschema_caseUpdateResponseType_httpwww_litle_comschemaphoenixTxnId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 185, 12), )

    
    phoenixTxnId = property(__phoenixTxnId.value, __phoenixTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}caseId uses Python identifier caseId
    __caseId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseId'), 'caseId', '__httpwww_litle_comschema_caseUpdateResponseType_httpwww_litle_comschemacaseId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 186, 12), )

    
    caseId = property(__caseId.value, __caseId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantActivityId uses Python identifier merchantActivityId
    __merchantActivityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'merchantActivityId'), 'merchantActivityId', '__httpwww_litle_comschema_caseUpdateResponseType_httpwww_litle_comschemamerchantActivityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 187, 12), )

    
    merchantActivityId = property(__merchantActivityId.value, __merchantActivityId.set, None, None)

    _ElementMap.update({
        __phoenixTxnId.name() : __phoenixTxnId,
        __caseId.name() : __caseId,
        __merchantActivityId.name() : __merchantActivityId
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'caseUpdateResponseType', caseUpdateResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'user'), 'user', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemauser', False, pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 8, 16), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Element {http://www.litle.com/schema}password uses Python identifier password
    __password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'password'), 'password', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemapassword', False, pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 9, 16), )

    
    password = property(__password.value, __password.set, None, None)

    _ElementMap.update({
        __user.name() : __user,
        __password.name() : __password
    })
    _AttributeMap.update({
        
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Root element for request to export chargeback activities."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 12, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}activityDate uses Python identifier activityDate
    __activityDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'activityDate'), 'activityDate', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaactivityDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 15, 16), )

    
    activityDate = property(__activityDate.value, __activityDate.set, None, None)

    
    # Element {http://www.litle.com/schema}financialOnly uses Python identifier financialOnly
    __financialOnly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'financialOnly'), 'financialOnly', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemafinancialOnly', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16), )

    
    financialOnly = property(__financialOnly.value, __financialOnly.set, None, None)

    
    # Element {http://www.litle.com/schema}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authentication'), 'authentication', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaauthentication', False, pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4), )

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON__version', versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 18, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 18, 12)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __activityDate.name() : __activityDate,
        __financialOnly.name() : __financialOnly,
        __authentication.name() : __authentication
    })
    _AttributeMap.update({
        __version.name() : __version
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Root element for response containing chargeback activities."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 26, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}activityDate uses Python identifier activityDate
    __activityDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'activityDate'), 'activityDate', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaactivityDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 28, 16), )

    
    activityDate = property(__activityDate.value, __activityDate.set, None, None)

    
    # Element {http://www.litle.com/schema}caseActivity uses Python identifier caseActivity
    __caseActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseActivity'), 'caseActivity', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemacaseActivity', True, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16), )

    
    caseActivity = property(__caseActivity.value, __caseActivity.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_2_version', versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 31, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 31, 12)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_2_response', responseType, required=True)
    __response._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 32, 12)
    __response._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 32, 12)
    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_2_message', messageType, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 33, 12)
    __message._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 33, 12)
    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        __activityDate.name() : __activityDate,
        __caseActivity.name() : __caseActivity
    })
    _AttributeMap.update({
        __version.name() : __version,
        __response.name() : __response,
        __message.name() : __message
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Root element to update to chargeback cases."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 151, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseUpdate uses Python identifier caseUpdate
    __caseUpdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseUpdate'), 'caseUpdate', '__httpwww_litle_comschema_CTD_ANON_3_httpwww_litle_comschemacaseUpdate', True, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16), )

    
    caseUpdate = property(__caseUpdate.value, __caseUpdate.set, None, None)

    
    # Element {http://www.litle.com/schema}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'authentication'), 'authentication', '__httpwww_litle_comschema_CTD_ANON_3_httpwww_litle_comschemaauthentication', False, pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4), )

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_3_version', versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 156, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 156, 12)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __caseUpdate.name() : __caseUpdate,
        __authentication.name() : __authentication
    })
    _AttributeMap.update({
        __version.name() : __version
    })



# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Root element to give responses to update requests."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 172, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseUpdateResponse uses Python identifier caseUpdateResponse
    __caseUpdateResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'caseUpdateResponse'), 'caseUpdateResponse', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemacaseUpdateResponse', True, pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16), )

    
    caseUpdateResponse = property(__caseUpdateResponse.value, __caseUpdateResponse.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_4_version', versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 177, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 177, 12)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_4_response', responseType, required=True)
    __response._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 178, 12)
    __response._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 178, 12)
    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_4_message', messageType, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 179, 12)
    __message._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 179, 12)
    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        __caseUpdateResponse.name() : __caseUpdateResponse
    })
    _AttributeMap.update({
        __version.name() : __version,
        __response.name() : __response,
        __message.name() : __message
    })



authentication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON, location=pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', authentication.name().localName(), authentication)

litleChargebackActivitiesRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleChargebackActivitiesRequest'), CTD_ANON_, documentation=u'Root element for request to export chargeback activities.', location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackActivitiesRequest.name().localName(), litleChargebackActivitiesRequest)

litleChargebackActivitiesResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleChargebackActivitiesResponse'), CTD_ANON_2, documentation=u'Root element for response containing chargeback activities.', location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 22, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackActivitiesResponse.name().localName(), litleChargebackActivitiesResponse)

litleChargebackUpdateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleChargebackUpdateRequest'), CTD_ANON_3, documentation=u'Root element to update to chargeback cases.', location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 147, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackUpdateRequest.name().localName(), litleChargebackUpdateRequest)

litleChargebackUpdateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleChargebackUpdateResponse'), CTD_ANON_4, documentation=u'Root element to give responses to update requests.', location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 168, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackUpdateResponse.name().localName(), litleChargebackUpdateResponse)



caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseId'), litleIdType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 39, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantId'), merchantIdentificationType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 40, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dayIssuedByBank'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 41, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dayReceivedByLitle'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 42, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cycle'), cycleType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 43, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId'), litleIdType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 44, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantTxnId'), string25Type, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 45, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'orderId'), string25Type, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 46, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardNumberLast4'), cardNumberLast4Type, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 47, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'cardType'), methodOfPaymentTypeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 48, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chargebackAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 49, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chargebackCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 50, 12), unicode_default=u'USD'))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'originalTransactionDay'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 51, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'chargebackType'), chargebackType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 52, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activityType'), activityType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 53, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'representedAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'representedCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'preArbAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'preArbCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reasonCode'), pyxb.binding.datatypes.string, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 58, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reasonCodeDescription'), pyxb.binding.datatypes.string, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 59, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fromQueue'), queueType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 60, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'toQueue'), queueType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 61, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'currentQueue'), queueType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 62, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'settlementAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'settlementCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'notes'), pyxb.binding.datatypes.string, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationStatus'), fraudNotificationStatusType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationDate'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'retrievalRequestType'), retrievalRequestType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 40, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dayIssuedByBank')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 41, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dayReceivedByLitle')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 42, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cycle')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 43, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'litleTxnId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 44, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantTxnId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 45, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'orderId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 46, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardNumberLast4')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 47, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'cardType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 48, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chargebackAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 49, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chargebackCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 50, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'originalTransactionDay')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 51, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'chargebackType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 52, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'activityType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 53, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'representedAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'representedCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'preArbAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'preArbCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reasonCode')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 58, 12))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'reasonCodeDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 59, 12))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fromQueue')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 60, 12))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'toQueue')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 61, 12))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'currentQueue')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 62, 12))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'settlementAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'settlementCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'notes')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationStatus')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'fraudNotificationDate')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'retrievalRequestType')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12))
    st_29 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
         ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
         ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
         ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
         ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
         ]))
    transitions.append(fac.Transition(st_25, [
         ]))
    transitions.append(fac.Transition(st_26, [
         ]))
    transitions.append(fac.Transition(st_27, [
         ]))
    transitions.append(fac.Transition(st_28, [
         ]))
    transitions.append(fac.Transition(st_29, [
         ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_29._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
caseActivityType._Automaton = _BuildAutomaton()




caseUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseId'), litleIdType, scope=caseUpdateType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 162, 12)))

caseUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantActivityId'), string25Type, scope=caseUpdateType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 163, 12)))

caseUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activity'), activityType, scope=caseUpdateType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 164, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 162, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantActivityId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 163, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(caseUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'activity')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 164, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
caseUpdateType._Automaton = _BuildAutomaton_()




caseUpdateResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'phoenixTxnId'), litleIdType, scope=caseUpdateResponseType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 185, 12)))

caseUpdateResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseId'), litleIdType, scope=caseUpdateResponseType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 186, 12)))

caseUpdateResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'merchantActivityId'), string25Type, scope=caseUpdateResponseType, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 187, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'phoenixTxnId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 185, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 186, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(caseUpdateResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'merchantActivityId')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 187, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
caseUpdateResponseType._Automaton = _BuildAutomaton_2()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'user'), string20Type, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 8, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'password'), string20Type, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 9, 16)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'user')), pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'password')), pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 9, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_3()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activityDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 15, 16)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'financialOnly'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 14, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'activityDate')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 15, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'financialOnly')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_4()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'activityDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 28, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseActivity'), caseActivityType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'activityDate')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 28, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseActivity')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_5()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseUpdate'), caseUpdateType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'authentication'), CTD_ANON, scope=CTD_ANON_3, location=pyxb.utils.utility.Location(u'/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'authentication')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 153, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseUpdate')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_6()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'caseUpdateResponse'), caseUpdateResponseType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'caseUpdateResponse')), pyxb.utils.utility.Location('/usr/local/litle-home/rchabhad/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_7()

