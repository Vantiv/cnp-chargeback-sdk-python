# ./fields.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f03bd2be92cca0df00d3d054794f8a47756ec009
# Generated 2017-09-29 12:02:17.373335 by PyXB version 1.2.6 using Python 2.7.13.final.0
# Namespace http://www.litle.com/schema

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:90efcfb0-a52f-11e7-bbcf-001a4a01074d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.litle.com/schema', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
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
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
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

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cycleType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 72, 4)
    _Documentation = None
cycleType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=cycleType, enum_prefix=None)
cycleType.RETRIEVAL_REQUEST = cycleType._CF_enumeration.addEnumeration(unicode_value='RETRIEVAL_REQUEST', tag='RETRIEVAL_REQUEST')
cycleType.FIRST_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value='FIRST_CHARGEBACK', tag='FIRST_CHARGEBACK')
cycleType.REPRESENTMENT = cycleType._CF_enumeration.addEnumeration(unicode_value='REPRESENTMENT', tag='REPRESENTMENT')
cycleType.ARBITRATION_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value='ARBITRATION_CHARGEBACK', tag='ARBITRATION_CHARGEBACK')
cycleType.CHARGEBACK_REVERSAL = cycleType._CF_enumeration.addEnumeration(unicode_value='CHARGEBACK_REVERSAL', tag='CHARGEBACK_REVERSAL')
cycleType.PRE_ARB_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value='PRE_ARB_CHARGEBACK', tag='PRE_ARB_CHARGEBACK')
cycleType.ISSUER_ARB_CHARGEBACK = cycleType._CF_enumeration.addEnumeration(unicode_value='ISSUER_ARB_CHARGEBACK', tag='ISSUER_ARB_CHARGEBACK')
cycleType._InitializeFacetMap(cycleType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'cycleType', cycleType)
_module_typeBindings.cycleType = cycleType

# Atomic simple type: {http://www.litle.com/schema}chargebackType
class chargebackType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'chargebackType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 84, 4)
    _Documentation = None
chargebackType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=chargebackType, enum_prefix=None)
chargebackType.Deposit = chargebackType._CF_enumeration.addEnumeration(unicode_value='Deposit', tag='Deposit')
chargebackType.Refund = chargebackType._CF_enumeration.addEnumeration(unicode_value='Refund', tag='Refund')
chargebackType._InitializeFacetMap(chargebackType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'chargebackType', chargebackType)
_module_typeBindings.chargebackType = chargebackType

# Atomic simple type: {http://www.litle.com/schema}activityType
class activityType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'activityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 91, 4)
    _Documentation = None
activityType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=activityType, enum_prefix=None)
activityType.Add_Note = activityType._CF_enumeration.addEnumeration(unicode_value='Add Note', tag='Add_Note')
activityType.Assign_To_Litle = activityType._CF_enumeration.addEnumeration(unicode_value='Assign To Litle', tag='Assign_To_Litle')
activityType.Assign_To_Merchant = activityType._CF_enumeration.addEnumeration(unicode_value='Assign To Merchant', tag='Assign_To_Merchant')
activityType.Assign_To_Merchant_Automated = activityType._CF_enumeration.addEnumeration(unicode_value='Assign To Merchant Automated', tag='Assign_To_Merchant_Automated')
activityType.File_Arbitration = activityType._CF_enumeration.addEnumeration(unicode_value='File Arbitration', tag='File_Arbitration')
activityType.File_Pre_arbitration = activityType._CF_enumeration.addEnumeration(unicode_value='File Pre-arbitration', tag='File_Pre_arbitration')
activityType.Litle_Accepts_Liability = activityType._CF_enumeration.addEnumeration(unicode_value='Litle Accepts Liability', tag='Litle_Accepts_Liability')
activityType.Litle_Represent = activityType._CF_enumeration.addEnumeration(unicode_value='Litle Represent', tag='Litle_Represent')
activityType.Litle_Respond = activityType._CF_enumeration.addEnumeration(unicode_value='Litle Respond', tag='Litle_Respond')
activityType.Merchant_Accepts_Liability = activityType._CF_enumeration.addEnumeration(unicode_value='Merchant Accepts Liability', tag='Merchant_Accepts_Liability')
activityType.Merchant_Represent = activityType._CF_enumeration.addEnumeration(unicode_value='Merchant Represent', tag='Merchant_Represent')
activityType.Merchant_Requests_Arbitration = activityType._CF_enumeration.addEnumeration(unicode_value='Merchant Requests Arbitration', tag='Merchant_Requests_Arbitration')
activityType.Merchant_Respond = activityType._CF_enumeration.addEnumeration(unicode_value='Merchant Respond', tag='Merchant_Respond')
activityType.Merchant_Respond___Sent_Credit = activityType._CF_enumeration.addEnumeration(unicode_value='Merchant Respond - Sent Credit', tag='Merchant_Respond___Sent_Credit')
activityType.Merchant_Respond___Sent_Gift = activityType._CF_enumeration.addEnumeration(unicode_value='Merchant Respond - Sent Gift', tag='Merchant_Respond___Sent_Gift')
activityType.Move_To_Litle_Error_Queue = activityType._CF_enumeration.addEnumeration(unicode_value='Move To Litle Error Queue', tag='Move_To_Litle_Error_Queue')
activityType.Receive_Network_Transaction = activityType._CF_enumeration.addEnumeration(unicode_value='Receive Network Transaction', tag='Receive_Network_Transaction')
activityType.Request_Declined = activityType._CF_enumeration.addEnumeration(unicode_value='Request Declined', tag='Request_Declined')
activityType.Send_Representment = activityType._CF_enumeration.addEnumeration(unicode_value='Send Representment', tag='Send_Representment')
activityType.Send_Retrieval_Request_Response = activityType._CF_enumeration.addEnumeration(unicode_value='Send Retrieval Request Response', tag='Send_Retrieval_Request_Response')
activityType.Successful_Arbitration_Case = activityType._CF_enumeration.addEnumeration(unicode_value='Successful Arbitration Case', tag='Successful_Arbitration_Case')
activityType.Successful_Pre_arbitration_Case = activityType._CF_enumeration.addEnumeration(unicode_value='Successful Pre-arbitration Case', tag='Successful_Pre_arbitration_Case')
activityType.Successful_PayPal_Case = activityType._CF_enumeration.addEnumeration(unicode_value='Successful PayPal Case', tag='Successful_PayPal_Case')
activityType.Auto_Represent = activityType._CF_enumeration.addEnumeration(unicode_value='Auto Represent', tag='Auto_Represent')
activityType.Attach_Document = activityType._CF_enumeration.addEnumeration(unicode_value='Attach Document', tag='Attach_Document')
activityType.Delete_Document = activityType._CF_enumeration.addEnumeration(unicode_value='Delete Document', tag='Delete_Document')
activityType.Update_Document = activityType._CF_enumeration.addEnumeration(unicode_value='Update Document', tag='Update_Document')
activityType.Attempted_to_Attach_Document = activityType._CF_enumeration.addEnumeration(unicode_value='Attempted to Attach Document', tag='Attempted_to_Attach_Document')
activityType.Network_Decision = activityType._CF_enumeration.addEnumeration(unicode_value='Network Decision', tag='Network_Decision')
activityType.Network_Declined = activityType._CF_enumeration.addEnumeration(unicode_value='Network Declined', tag='Network_Declined')
activityType._InitializeFacetMap(activityType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'activityType', activityType)
_module_typeBindings.activityType = activityType

# Atomic simple type: {http://www.litle.com/schema}queueType
class queueType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'queueType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 126, 4)
    _Documentation = None
queueType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=queueType, enum_prefix=None)
queueType.New = queueType._CF_enumeration.addEnumeration(unicode_value='New', tag='New')
queueType.Litle = queueType._CF_enumeration.addEnumeration(unicode_value='Litle', tag='Litle')
queueType.Litle_Outgoing = queueType._CF_enumeration.addEnumeration(unicode_value='Litle Outgoing', tag='Litle_Outgoing')
queueType.Litle_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value='Litle Assumed', tag='Litle_Assumed')
queueType.Litle_Error = queueType._CF_enumeration.addEnumeration(unicode_value='Litle Error', tag='Litle_Error')
queueType.Merchant = queueType._CF_enumeration.addEnumeration(unicode_value='Merchant', tag='Merchant')
queueType.Merchant_Automated = queueType._CF_enumeration.addEnumeration(unicode_value='Merchant Automated', tag='Merchant_Automated')
queueType.Merchant_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value='Merchant Assumed', tag='Merchant_Assumed')
queueType.Network_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value='Network Assumed', tag='Network_Assumed')
queueType.Merchant_Arbitrate = queueType._CF_enumeration.addEnumeration(unicode_value='Merchant Arbitrate', tag='Merchant_Arbitrate')
queueType.Pre_arbitrate = queueType._CF_enumeration.addEnumeration(unicode_value='Pre-arbitrate', tag='Pre_arbitrate')
queueType.Arbitrate = queueType._CF_enumeration.addEnumeration(unicode_value='Arbitrate', tag='Arbitrate')
queueType.PayPal_Hold___Represent = queueType._CF_enumeration.addEnumeration(unicode_value='PayPal Hold - Represent', tag='PayPal_Hold___Represent')
queueType.PayPal_Hold___Assume = queueType._CF_enumeration.addEnumeration(unicode_value='PayPal Hold - Assume', tag='PayPal_Hold___Assume')
queueType.Decision_Pending = queueType._CF_enumeration.addEnumeration(unicode_value='Decision Pending', tag='Decision_Pending')
queueType.Merchant_Auto_Assumed = queueType._CF_enumeration.addEnumeration(unicode_value='Merchant Auto Assumed', tag='Merchant_Auto_Assumed')
queueType._InitializeFacetMap(queueType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'queueType', queueType)
_module_typeBindings.queueType = queueType

# Atomic simple type: {http://www.litle.com/schema}retrievalRequestType
class retrievalRequestType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'retrievalRequestType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 191, 4)
    _Documentation = None
retrievalRequestType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=retrievalRequestType, enum_prefix=None)
retrievalRequestType.INQUIRY = retrievalRequestType._CF_enumeration.addEnumeration(unicode_value='INQUIRY', tag='INQUIRY')
retrievalRequestType.DISPUTE = retrievalRequestType._CF_enumeration.addEnumeration(unicode_value='DISPUTE', tag='DISPUTE')
retrievalRequestType._InitializeFacetMap(retrievalRequestType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'retrievalRequestType', retrievalRequestType)
_module_typeBindings.retrievalRequestType = retrievalRequestType

# Atomic simple type: {http://www.litle.com/schema}fraudNotificationStatusType
class fraudNotificationStatusType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationStatusType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 198, 1)
    _Documentation = None
fraudNotificationStatusType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fraudNotificationStatusType, enum_prefix=None)
fraudNotificationStatusType.BEFORE = fraudNotificationStatusType._CF_enumeration.addEnumeration(unicode_value='BEFORE', tag='BEFORE')
fraudNotificationStatusType.AFTER = fraudNotificationStatusType._CF_enumeration.addEnumeration(unicode_value='AFTER', tag='AFTER')
fraudNotificationStatusType._InitializeFacetMap(fraudNotificationStatusType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'fraudNotificationStatusType', fraudNotificationStatusType)
_module_typeBindings.fraudNotificationStatusType = fraudNotificationStatusType

# Atomic simple type: {http://www.litle.com/schema}string20Type
class string20Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'string20Type')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 14, 4)
    _Documentation = None
string20Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
string20Type._InitializeFacetMap(string20Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'string20Type', string20Type)
_module_typeBindings.string20Type = string20Type

# Atomic simple type: {http://www.litle.com/schema}versionType
class versionType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'versionType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 20, 4)
    _Documentation = None
versionType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
versionType._InitializeFacetMap(versionType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'versionType', versionType)
_module_typeBindings.versionType = versionType

# Atomic simple type: {http://www.litle.com/schema}messageType
class messageType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'messageType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 26, 4)
    _Documentation = None
messageType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(512))
messageType._InitializeFacetMap(messageType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'messageType', messageType)
_module_typeBindings.messageType = messageType

# Atomic simple type: {http://www.litle.com/schema}string2Type
class string2Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'string2Type')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 32, 4)
    _Documentation = None
string2Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2))
string2Type._InitializeFacetMap(string2Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'string2Type', string2Type)
_module_typeBindings.string2Type = string2Type

# Atomic simple type: {http://www.litle.com/schema}responseType
class responseType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'responseType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 38, 4)
    _Documentation = None
responseType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
responseType._InitializeFacetMap(responseType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'responseType', responseType)
_module_typeBindings.responseType = responseType

# Atomic simple type: {http://www.litle.com/schema}litleIdType
class litleIdType (pyxb.binding.datatypes.long):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'litleIdType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 44, 4)
    _Documentation = None
litleIdType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(19))
litleIdType._InitializeFacetMap(litleIdType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'litleIdType', litleIdType)
_module_typeBindings.litleIdType = litleIdType

# Atomic simple type: {http://www.litle.com/schema}string25Type
class string25Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'string25Type')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 50, 4)
    _Documentation = None
string25Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(25))
string25Type._InitializeFacetMap(string25Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'string25Type', string25Type)
_module_typeBindings.string25Type = string25Type

# Atomic simple type: {http://www.litle.com/schema}cardNumberLast4Type
class cardNumberLast4Type (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cardNumberLast4Type')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 56, 4)
    _Documentation = None
cardNumberLast4Type._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
cardNumberLast4Type._InitializeFacetMap(cardNumberLast4Type._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'cardNumberLast4Type', cardNumberLast4Type)
_module_typeBindings.cardNumberLast4Type = cardNumberLast4Type

# Atomic simple type: {http://www.litle.com/schema}virtualAuthenticationKeyData
class virtualAuthenticationKeyData (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'virtualAuthenticationKeyData')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 61, 4)
    _Documentation = None
virtualAuthenticationKeyData._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
virtualAuthenticationKeyData._InitializeFacetMap(virtualAuthenticationKeyData._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'virtualAuthenticationKeyData', virtualAuthenticationKeyData)
_module_typeBindings.virtualAuthenticationKeyData = virtualAuthenticationKeyData

# Atomic simple type: {http://www.litle.com/schema}virtualAuthenticationKeyPresenceIndicator
class virtualAuthenticationKeyPresenceIndicator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'virtualAuthenticationKeyPresenceIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 67, 4)
    _Documentation = None
virtualAuthenticationKeyPresenceIndicator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
virtualAuthenticationKeyPresenceIndicator._InitializeFacetMap(virtualAuthenticationKeyPresenceIndicator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'virtualAuthenticationKeyPresenceIndicator', virtualAuthenticationKeyPresenceIndicator)
_module_typeBindings.virtualAuthenticationKeyPresenceIndicator = virtualAuthenticationKeyPresenceIndicator

# Atomic simple type: {http://www.litle.com/schema}authorizationSourcePlatform
class authorizationSourcePlatform (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authorizationSourcePlatform')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 72, 4)
    _Documentation = None
authorizationSourcePlatform._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
authorizationSourcePlatform._InitializeFacetMap(authorizationSourcePlatform._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'authorizationSourcePlatform', authorizationSourcePlatform)
_module_typeBindings.authorizationSourcePlatform = authorizationSourcePlatform

# Atomic simple type: {http://www.litle.com/schema}addressIndicator
class addressIndicator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressIndicator')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 77, 4)
    _Documentation = None
addressIndicator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
addressIndicator._InitializeFacetMap(addressIndicator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'addressIndicator', addressIndicator)
_module_typeBindings.addressIndicator = addressIndicator

# Atomic simple type: {http://www.litle.com/schema}authenticationResultType
class authenticationResultType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authenticationResultType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 82, 4)
    _Documentation = None
authenticationResultType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
authenticationResultType._InitializeFacetMap(authenticationResultType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'authenticationResultType', authenticationResultType)
_module_typeBindings.authenticationResultType = authenticationResultType

# Atomic simple type: {http://www.litle.com/schema}methodOfPaymentTypeEnum
class methodOfPaymentTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'methodOfPaymentTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 88, 4)
    _Documentation = None
methodOfPaymentTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=methodOfPaymentTypeEnum, enum_prefix=None)
methodOfPaymentTypeEnum.MC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
methodOfPaymentTypeEnum.VI = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
methodOfPaymentTypeEnum.AX = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
methodOfPaymentTypeEnum.DC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='DC', tag='DC')
methodOfPaymentTypeEnum.DI = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='DI', tag='DI')
methodOfPaymentTypeEnum.PP = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='PP', tag='PP')
methodOfPaymentTypeEnum.JC = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='JC', tag='JC')
methodOfPaymentTypeEnum.BL = methodOfPaymentTypeEnum._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
methodOfPaymentTypeEnum._InitializeFacetMap(methodOfPaymentTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'methodOfPaymentTypeEnum', methodOfPaymentTypeEnum)
_module_typeBindings.methodOfPaymentTypeEnum = methodOfPaymentTypeEnum

# Atomic simple type: {http://www.litle.com/schema}transactionAmountType
class transactionAmountType (pyxb.binding.datatypes.integer):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'transactionAmountType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 101, 4)
    _Documentation = None
transactionAmountType._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(8))
transactionAmountType._InitializeFacetMap(transactionAmountType._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'transactionAmountType', transactionAmountType)
_module_typeBindings.transactionAmountType = transactionAmountType

# Atomic simple type: {http://www.litle.com/schema}loanToValueEstimator
class loanToValueEstimator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'loanToValueEstimator')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 107, 4)
    _Documentation = None
loanToValueEstimator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
loanToValueEstimator._InitializeFacetMap(loanToValueEstimator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'loanToValueEstimator', loanToValueEstimator)
_module_typeBindings.loanToValueEstimator = loanToValueEstimator

# Atomic simple type: {http://www.litle.com/schema}riskEstimator
class riskEstimator (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'riskEstimator')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 112, 4)
    _Documentation = None
riskEstimator._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
riskEstimator._InitializeFacetMap(riskEstimator._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'riskEstimator', riskEstimator)
_module_typeBindings.riskEstimator = riskEstimator

# Atomic simple type: {http://www.litle.com/schema}riskQueueAssignment
class riskQueueAssignment (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'riskQueueAssignment')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 117, 4)
    _Documentation = None
riskQueueAssignment._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(8))
riskQueueAssignment._InitializeFacetMap(riskQueueAssignment._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'riskQueueAssignment', riskQueueAssignment)
_module_typeBindings.riskQueueAssignment = riskQueueAssignment

# Atomic simple type: {http://www.litle.com/schema}merchantIdentificationType
class merchantIdentificationType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'merchantIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 123, 4)
    _Documentation = None
merchantIdentificationType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
merchantIdentificationType._InitializeFacetMap(merchantIdentificationType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'merchantIdentificationType', merchantIdentificationType)
_module_typeBindings.merchantIdentificationType = merchantIdentificationType

# Atomic simple type: {http://www.litle.com/schema}currencyCodeEnum
class currencyCodeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'currencyCodeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 129, 4)
    _Documentation = None
currencyCodeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=currencyCodeEnum, enum_prefix=None)
currencyCodeEnum.AUD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='AUD', tag='AUD')
currencyCodeEnum.CAD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='CAD', tag='CAD')
currencyCodeEnum.CHF = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='CHF', tag='CHF')
currencyCodeEnum.DKK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='DKK', tag='DKK')
currencyCodeEnum.EUR = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='EUR', tag='EUR')
currencyCodeEnum.GBP = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='GBP', tag='GBP')
currencyCodeEnum.HKD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='HKD', tag='HKD')
currencyCodeEnum.JPY = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='JPY', tag='JPY')
currencyCodeEnum.NOK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='NOK', tag='NOK')
currencyCodeEnum.NZD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='NZD', tag='NZD')
currencyCodeEnum.SEK = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='SEK', tag='SEK')
currencyCodeEnum.SGD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='SGD', tag='SGD')
currencyCodeEnum.USD = currencyCodeEnum._CF_enumeration.addEnumeration(unicode_value='USD', tag='USD')
currencyCodeEnum._InitializeFacetMap(currencyCodeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'currencyCodeEnum', currencyCodeEnum)
_module_typeBindings.currencyCodeEnum = currencyCodeEnum

# Atomic simple type: {http://www.litle.com/schema}countryTypeEnum
class countryTypeEnum (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'countryTypeEnum')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 147, 4)
    _Documentation = None
countryTypeEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=countryTypeEnum, enum_prefix=None)
countryTypeEnum.USA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='USA', tag='USA')
countryTypeEnum.AF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AF', tag='AF')
countryTypeEnum.AX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AX', tag='AX')
countryTypeEnum.AL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
countryTypeEnum.DZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='DZ', tag='DZ')
countryTypeEnum.AS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AS', tag='AS')
countryTypeEnum.AD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AD', tag='AD')
countryTypeEnum.AO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AO', tag='AO')
countryTypeEnum.AI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AI', tag='AI')
countryTypeEnum.AQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AQ', tag='AQ')
countryTypeEnum.AG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AG', tag='AG')
countryTypeEnum.AR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AR', tag='AR')
countryTypeEnum.AM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
countryTypeEnum.AW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AW', tag='AW')
countryTypeEnum.AU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AU', tag='AU')
countryTypeEnum.AT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AT', tag='AT')
countryTypeEnum.AZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AZ', tag='AZ')
countryTypeEnum.BS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BS', tag='BS')
countryTypeEnum.BH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BH', tag='BH')
countryTypeEnum.BD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BD', tag='BD')
countryTypeEnum.BB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BB', tag='BB')
countryTypeEnum.BY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BY', tag='BY')
countryTypeEnum.BE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BE', tag='BE')
countryTypeEnum.BZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BZ', tag='BZ')
countryTypeEnum.BJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BJ', tag='BJ')
countryTypeEnum.BM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BM', tag='BM')
countryTypeEnum.BT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BT', tag='BT')
countryTypeEnum.BO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BO', tag='BO')
countryTypeEnum.BA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
countryTypeEnum.BW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BW', tag='BW')
countryTypeEnum.BV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BV', tag='BV')
countryTypeEnum.BR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BR', tag='BR')
countryTypeEnum.IO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IO', tag='IO')
countryTypeEnum.BN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BN', tag='BN')
countryTypeEnum.BG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BG', tag='BG')
countryTypeEnum.BF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BF', tag='BF')
countryTypeEnum.BI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BI', tag='BI')
countryTypeEnum.KH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KH', tag='KH')
countryTypeEnum.CM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CM', tag='CM')
countryTypeEnum.CA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CA', tag='CA')
countryTypeEnum.CV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CV', tag='CV')
countryTypeEnum.KY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KY', tag='KY')
countryTypeEnum.CF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CF', tag='CF')
countryTypeEnum.TD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TD', tag='TD')
countryTypeEnum.CL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CL', tag='CL')
countryTypeEnum.CN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CN', tag='CN')
countryTypeEnum.CX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CX', tag='CX')
countryTypeEnum.CC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CC', tag='CC')
countryTypeEnum.CO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CO', tag='CO')
countryTypeEnum.KM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KM', tag='KM')
countryTypeEnum.CG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CG', tag='CG')
countryTypeEnum.CD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CD', tag='CD')
countryTypeEnum.CK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CK', tag='CK')
countryTypeEnum.CR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CR', tag='CR')
countryTypeEnum.CI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CI', tag='CI')
countryTypeEnum.HR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='HR', tag='HR')
countryTypeEnum.CU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CU', tag='CU')
countryTypeEnum.CY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CY', tag='CY')
countryTypeEnum.CZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CZ', tag='CZ')
countryTypeEnum.DK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='DK', tag='DK')
countryTypeEnum.DJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='DJ', tag='DJ')
countryTypeEnum.DM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='DM', tag='DM')
countryTypeEnum.DO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='DO', tag='DO')
countryTypeEnum.TL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TL', tag='TL')
countryTypeEnum.EC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='EC', tag='EC')
countryTypeEnum.EG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='EG', tag='EG')
countryTypeEnum.SV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SV', tag='SV')
countryTypeEnum.GQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GQ', tag='GQ')
countryTypeEnum.ER = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ER', tag='ER')
countryTypeEnum.EE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='EE', tag='EE')
countryTypeEnum.ET = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ET', tag='ET')
countryTypeEnum.FK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='FK', tag='FK')
countryTypeEnum.FO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='FO', tag='FO')
countryTypeEnum.FJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='FJ', tag='FJ')
countryTypeEnum.FI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='FI', tag='FI')
countryTypeEnum.FR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='FR', tag='FR')
countryTypeEnum.GF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GF', tag='GF')
countryTypeEnum.PF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PF', tag='PF')
countryTypeEnum.TF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TF', tag='TF')
countryTypeEnum.GA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GA', tag='GA')
countryTypeEnum.GM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GM', tag='GM')
countryTypeEnum.GE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GE', tag='GE')
countryTypeEnum.DE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='DE', tag='DE')
countryTypeEnum.GH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GH', tag='GH')
countryTypeEnum.GI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GI', tag='GI')
countryTypeEnum.GR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GR', tag='GR')
countryTypeEnum.GL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GL', tag='GL')
countryTypeEnum.GD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GD', tag='GD')
countryTypeEnum.GP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GP', tag='GP')
countryTypeEnum.GU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GU', tag='GU')
countryTypeEnum.GT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GT', tag='GT')
countryTypeEnum.GG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GG', tag='GG')
countryTypeEnum.GN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GN', tag='GN')
countryTypeEnum.GW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GW', tag='GW')
countryTypeEnum.GY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GY', tag='GY')
countryTypeEnum.HT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='HT', tag='HT')
countryTypeEnum.HM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='HM', tag='HM')
countryTypeEnum.HN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='HN', tag='HN')
countryTypeEnum.HK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='HK', tag='HK')
countryTypeEnum.HU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='HU', tag='HU')
countryTypeEnum.IS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IS', tag='IS')
countryTypeEnum.IN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IN', tag='IN')
countryTypeEnum.ID = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ID', tag='ID')
countryTypeEnum.IR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IR', tag='IR')
countryTypeEnum.IQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IQ', tag='IQ')
countryTypeEnum.IE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IE', tag='IE')
countryTypeEnum.IM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IM', tag='IM')
countryTypeEnum.IL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IL', tag='IL')
countryTypeEnum.IT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='IT', tag='IT')
countryTypeEnum.JM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='JM', tag='JM')
countryTypeEnum.JP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='JP', tag='JP')
countryTypeEnum.JE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='JE', tag='JE')
countryTypeEnum.JO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='JO', tag='JO')
countryTypeEnum.KZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KZ', tag='KZ')
countryTypeEnum.KE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KE', tag='KE')
countryTypeEnum.KI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KI', tag='KI')
countryTypeEnum.KP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KP', tag='KP')
countryTypeEnum.KR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KR', tag='KR')
countryTypeEnum.KW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KW', tag='KW')
countryTypeEnum.KG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KG', tag='KG')
countryTypeEnum.LA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LA', tag='LA')
countryTypeEnum.LV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LV', tag='LV')
countryTypeEnum.LB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LB', tag='LB')
countryTypeEnum.LS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LS', tag='LS')
countryTypeEnum.LR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LR', tag='LR')
countryTypeEnum.LY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LY', tag='LY')
countryTypeEnum.LI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LI', tag='LI')
countryTypeEnum.LT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LT', tag='LT')
countryTypeEnum.LU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LU', tag='LU')
countryTypeEnum.MO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MO', tag='MO')
countryTypeEnum.MK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MK', tag='MK')
countryTypeEnum.MG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
countryTypeEnum.MW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MW', tag='MW')
countryTypeEnum.MY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MY', tag='MY')
countryTypeEnum.MV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MV', tag='MV')
countryTypeEnum.ML = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ML', tag='ML')
countryTypeEnum.MT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
countryTypeEnum.MH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MH', tag='MH')
countryTypeEnum.MQ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MQ', tag='MQ')
countryTypeEnum.MR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MR', tag='MR')
countryTypeEnum.MU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MU', tag='MU')
countryTypeEnum.YT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='YT', tag='YT')
countryTypeEnum.MX = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MX', tag='MX')
countryTypeEnum.FM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='FM', tag='FM')
countryTypeEnum.MD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MD', tag='MD')
countryTypeEnum.MC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MC', tag='MC')
countryTypeEnum.MN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MN', tag='MN')
countryTypeEnum.MS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
countryTypeEnum.MA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
countryTypeEnum.MZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MZ', tag='MZ')
countryTypeEnum.MM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MM', tag='MM')
countryTypeEnum.NA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NA', tag='NA')
countryTypeEnum.NR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NR', tag='NR')
countryTypeEnum.NP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NP', tag='NP')
countryTypeEnum.NL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NL', tag='NL')
countryTypeEnum.AN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AN', tag='AN')
countryTypeEnum.NC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NC', tag='NC')
countryTypeEnum.NZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NZ', tag='NZ')
countryTypeEnum.NI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NI', tag='NI')
countryTypeEnum.NE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NE', tag='NE')
countryTypeEnum.NG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NG', tag='NG')
countryTypeEnum.NU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NU', tag='NU')
countryTypeEnum.NF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NF', tag='NF')
countryTypeEnum.MP = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MP', tag='MP')
countryTypeEnum.NO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='NO', tag='NO')
countryTypeEnum.OM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='OM', tag='OM')
countryTypeEnum.PK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PK', tag='PK')
countryTypeEnum.PW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PW', tag='PW')
countryTypeEnum.PS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PS', tag='PS')
countryTypeEnum.PA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
countryTypeEnum.PG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PG', tag='PG')
countryTypeEnum.PY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PY', tag='PY')
countryTypeEnum.PE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
countryTypeEnum.PH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PH', tag='PH')
countryTypeEnum.PN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PN', tag='PN')
countryTypeEnum.PL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PL', tag='PL')
countryTypeEnum.PT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PT', tag='PT')
countryTypeEnum.PR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
countryTypeEnum.QA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='QA', tag='QA')
countryTypeEnum.RE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='RE', tag='RE')
countryTypeEnum.RO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
countryTypeEnum.RU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='RU', tag='RU')
countryTypeEnum.RW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='RW', tag='RW')
countryTypeEnum.BL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='BL', tag='BL')
countryTypeEnum.KN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='KN', tag='KN')
countryTypeEnum.LC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LC', tag='LC')
countryTypeEnum.MF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='MF', tag='MF')
countryTypeEnum.VC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VC', tag='VC')
countryTypeEnum.WS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='WS', tag='WS')
countryTypeEnum.SM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SM', tag='SM')
countryTypeEnum.ST = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ST', tag='ST')
countryTypeEnum.SA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SA', tag='SA')
countryTypeEnum.SN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SN', tag='SN')
countryTypeEnum.SC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
countryTypeEnum.SL = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SL', tag='SL')
countryTypeEnum.SG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SG', tag='SG')
countryTypeEnum.SK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SK', tag='SK')
countryTypeEnum.SI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SI', tag='SI')
countryTypeEnum.SB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SB', tag='SB')
countryTypeEnum.SO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SO', tag='SO')
countryTypeEnum.ZA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ZA', tag='ZA')
countryTypeEnum.GS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GS', tag='GS')
countryTypeEnum.ES = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
countryTypeEnum.LK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='LK', tag='LK')
countryTypeEnum.SH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SH', tag='SH')
countryTypeEnum.PM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='PM', tag='PM')
countryTypeEnum.SD = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SD', tag='SD')
countryTypeEnum.SR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SR', tag='SR')
countryTypeEnum.SJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SJ', tag='SJ')
countryTypeEnum.SZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SZ', tag='SZ')
countryTypeEnum.SE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
countryTypeEnum.CH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='CH', tag='CH')
countryTypeEnum.SY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='SY', tag='SY')
countryTypeEnum.TW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TW', tag='TW')
countryTypeEnum.TJ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TJ', tag='TJ')
countryTypeEnum.TZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TZ', tag='TZ')
countryTypeEnum.TH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TH', tag='TH')
countryTypeEnum.TG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TG', tag='TG')
countryTypeEnum.TK = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TK', tag='TK')
countryTypeEnum.TO = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
countryTypeEnum.TT = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TT', tag='TT')
countryTypeEnum.TN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TN', tag='TN')
countryTypeEnum.TR = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TR', tag='TR')
countryTypeEnum.TM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TM', tag='TM')
countryTypeEnum.TC = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TC', tag='TC')
countryTypeEnum.TV = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='TV', tag='TV')
countryTypeEnum.UG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='UG', tag='UG')
countryTypeEnum.UA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='UA', tag='UA')
countryTypeEnum.AE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='AE', tag='AE')
countryTypeEnum.GB = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='GB', tag='GB')
countryTypeEnum.US = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='US', tag='US')
countryTypeEnum.UM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='UM', tag='UM')
countryTypeEnum.UY = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='UY', tag='UY')
countryTypeEnum.UZ = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='UZ', tag='UZ')
countryTypeEnum.VU = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VU', tag='VU')
countryTypeEnum.VA = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VA', tag='VA')
countryTypeEnum.VE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VE', tag='VE')
countryTypeEnum.VN = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VN', tag='VN')
countryTypeEnum.VG = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VG', tag='VG')
countryTypeEnum.VI = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='VI', tag='VI')
countryTypeEnum.WF = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='WF', tag='WF')
countryTypeEnum.EH = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='EH', tag='EH')
countryTypeEnum.YE = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='YE', tag='YE')
countryTypeEnum.ZM = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ZM', tag='ZM')
countryTypeEnum.ZW = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ZW', tag='ZW')
countryTypeEnum.RS = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
countryTypeEnum.ME = countryTypeEnum._CF_enumeration.addEnumeration(unicode_value='ME', tag='ME')
countryTypeEnum._InitializeFacetMap(countryTypeEnum._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'countryTypeEnum', countryTypeEnum)
_module_typeBindings.countryTypeEnum = countryTypeEnum

# Atomic simple type: {http://www.litle.com/schema}addressLineType
class addressLineType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'addressLineType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 399, 4)
    _Documentation = None
addressLineType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
addressLineType._InitializeFacetMap(addressLineType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'addressLineType', addressLineType)
_module_typeBindings.addressLineType = addressLineType

# Atomic simple type: {http://www.litle.com/schema}cityType
class cityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 404, 4)
    _Documentation = None
cityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
cityType._InitializeFacetMap(cityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'cityType', cityType)
_module_typeBindings.cityType = cityType

# Atomic simple type: {http://www.litle.com/schema}customBillingCityType
class customBillingCityType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'customBillingCityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 409, 4)
    _Documentation = None
customBillingCityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
customBillingCityType._InitializeFacetMap(customBillingCityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'customBillingCityType', customBillingCityType)
_module_typeBindings.customBillingCityType = customBillingCityType

# Atomic simple type: {http://www.litle.com/schema}stateType
class stateType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stateType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 414, 4)
    _Documentation = None
stateType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stateType._InitializeFacetMap(stateType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stateType', stateType)
_module_typeBindings.stateType = stateType

# Atomic simple type: {http://www.litle.com/schema}zipType
class zipType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'zipType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 419, 4)
    _Documentation = None
zipType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
zipType._InitializeFacetMap(zipType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'zipType', zipType)
_module_typeBindings.zipType = zipType

# Atomic simple type: {http://www.litle.com/schema}emailType
class emailType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'emailType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 425, 4)
    _Documentation = None
emailType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
emailType._InitializeFacetMap(emailType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'emailType', emailType)
_module_typeBindings.emailType = emailType

# Atomic simple type: {http://www.litle.com/schema}phoneType
class phoneType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phoneType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 430, 4)
    _Documentation = None
phoneType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
phoneType._InitializeFacetMap(phoneType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'phoneType', phoneType)
_module_typeBindings.phoneType = phoneType

# Atomic simple type: {http://www.litle.com/schema}nameType
class nameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nameType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 435, 4)
    _Documentation = None
nameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100))
nameType._InitializeFacetMap(nameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'nameType', nameType)
_module_typeBindings.nameType = nameType

# Atomic simple type: {http://www.litle.com/schema}cvNumType
class cvNumType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cvNumType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 440, 4)
    _Documentation = None
cvNumType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
cvNumType._InitializeFacetMap(cvNumType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'cvNumType', cvNumType)
_module_typeBindings.cvNumType = cvNumType

# Atomic simple type: {http://www.litle.com/schema}authCodeType
class authCodeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'authCodeType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 445, 4)
    _Documentation = None
authCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6))
authCodeType._InitializeFacetMap(authCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'authCodeType', authCodeType)
_module_typeBindings.authCodeType = authCodeType

# Atomic simple type: {http://www.litle.com/schema}customerIdType
class customerIdType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'customerIdType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 450, 4)
    _Documentation = None
customerIdType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
customerIdType._InitializeFacetMap(customerIdType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'customerIdType', customerIdType)
_module_typeBindings.customerIdType = customerIdType

# Atomic simple type: {http://www.litle.com/schema}customBillingUrlType
class customBillingUrlType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'customBillingUrlType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 455, 4)
    _Documentation = None
customBillingUrlType._CF_pattern = pyxb.binding.facets.CF_pattern()
customBillingUrlType._CF_pattern.addPattern(pattern='[A-Z,a-z,0-9,/,\\-,_,.]*')
customBillingUrlType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
customBillingUrlType._InitializeFacetMap(customBillingUrlType._CF_pattern,
   customBillingUrlType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'customBillingUrlType', customBillingUrlType)
_module_typeBindings.customBillingUrlType = customBillingUrlType

# Complex type {http://www.litle.com/schema}caseActivityType with content type ELEMENT_ONLY
class caseActivityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.litle.com/schema}caseActivityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'caseActivityType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 37, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseId uses Python identifier caseId
    __caseId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseId'), 'caseId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacaseId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 39, 12), )

    
    caseId = property(__caseId.value, __caseId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantId uses Python identifier merchantId
    __merchantId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantId'), 'merchantId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemamerchantId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 40, 12), )

    
    merchantId = property(__merchantId.value, __merchantId.set, None, None)

    
    # Element {http://www.litle.com/schema}dayIssuedByBank uses Python identifier dayIssuedByBank
    __dayIssuedByBank = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dayIssuedByBank'), 'dayIssuedByBank', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemadayIssuedByBank', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 41, 12), )

    
    dayIssuedByBank = property(__dayIssuedByBank.value, __dayIssuedByBank.set, None, None)

    
    # Element {http://www.litle.com/schema}dayReceivedByLitle uses Python identifier dayReceivedByLitle
    __dayReceivedByLitle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dayReceivedByLitle'), 'dayReceivedByLitle', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemadayReceivedByLitle', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 42, 12), )

    
    dayReceivedByLitle = property(__dayReceivedByLitle.value, __dayReceivedByLitle.set, None, None)

    
    # Element {http://www.litle.com/schema}cycle uses Python identifier cycle
    __cycle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cycle'), 'cycle', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacycle', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 43, 12), )

    
    cycle = property(__cycle.value, __cycle.set, None, None)

    
    # Element {http://www.litle.com/schema}litleTxnId uses Python identifier litleTxnId
    __litleTxnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'litleTxnId'), 'litleTxnId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemalitleTxnId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 44, 12), )

    
    litleTxnId = property(__litleTxnId.value, __litleTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantTxnId uses Python identifier merchantTxnId
    __merchantTxnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantTxnId'), 'merchantTxnId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemamerchantTxnId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 45, 12), )

    
    merchantTxnId = property(__merchantTxnId.value, __merchantTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}orderId uses Python identifier orderId
    __orderId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'orderId'), 'orderId', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaorderId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 46, 12), )

    
    orderId = property(__orderId.value, __orderId.set, None, None)

    
    # Element {http://www.litle.com/schema}cardNumberLast4 uses Python identifier cardNumberLast4
    __cardNumberLast4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cardNumberLast4'), 'cardNumberLast4', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacardNumberLast4', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 47, 12), )

    
    cardNumberLast4 = property(__cardNumberLast4.value, __cardNumberLast4.set, None, None)

    
    # Element {http://www.litle.com/schema}cardType uses Python identifier cardType
    __cardType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cardType'), 'cardType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacardType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 48, 12), )

    
    cardType = property(__cardType.value, __cardType.set, None, None)

    
    # Element {http://www.litle.com/schema}chargebackAmount uses Python identifier chargebackAmount
    __chargebackAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chargebackAmount'), 'chargebackAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemachargebackAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 49, 12), )

    
    chargebackAmount = property(__chargebackAmount.value, __chargebackAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}chargebackCurrencyType uses Python identifier chargebackCurrencyType
    __chargebackCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chargebackCurrencyType'), 'chargebackCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemachargebackCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 50, 12), )

    
    chargebackCurrencyType = property(__chargebackCurrencyType.value, __chargebackCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}originalTransactionDay uses Python identifier originalTransactionDay
    __originalTransactionDay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'originalTransactionDay'), 'originalTransactionDay', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaoriginalTransactionDay', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 51, 12), )

    
    originalTransactionDay = property(__originalTransactionDay.value, __originalTransactionDay.set, None, None)

    
    # Element {http://www.litle.com/schema}chargebackType uses Python identifier chargebackType
    __chargebackType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chargebackType'), 'chargebackType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemachargebackType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 52, 12), )

    
    chargebackType = property(__chargebackType.value, __chargebackType.set, None, None)

    
    # Element {http://www.litle.com/schema}activityType uses Python identifier activityType
    __activityType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityType'), 'activityType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaactivityType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 53, 12), )

    
    activityType = property(__activityType.value, __activityType.set, None, None)

    
    # Element {http://www.litle.com/schema}representedAmount uses Python identifier representedAmount
    __representedAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'representedAmount'), 'representedAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemarepresentedAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12), )

    
    representedAmount = property(__representedAmount.value, __representedAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}representedCurrencyType uses Python identifier representedCurrencyType
    __representedCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'representedCurrencyType'), 'representedCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemarepresentedCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12), )

    
    representedCurrencyType = property(__representedCurrencyType.value, __representedCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}preArbAmount uses Python identifier preArbAmount
    __preArbAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'preArbAmount'), 'preArbAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemapreArbAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12), )

    
    preArbAmount = property(__preArbAmount.value, __preArbAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}preArbCurrencyType uses Python identifier preArbCurrencyType
    __preArbCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'preArbCurrencyType'), 'preArbCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemapreArbCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12), )

    
    preArbCurrencyType = property(__preArbCurrencyType.value, __preArbCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}reasonCode uses Python identifier reasonCode
    __reasonCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reasonCode'), 'reasonCode', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemareasonCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 58, 12), )

    
    reasonCode = property(__reasonCode.value, __reasonCode.set, None, None)

    
    # Element {http://www.litle.com/schema}reasonCodeDescription uses Python identifier reasonCodeDescription
    __reasonCodeDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'reasonCodeDescription'), 'reasonCodeDescription', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemareasonCodeDescription', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 59, 12), )

    
    reasonCodeDescription = property(__reasonCodeDescription.value, __reasonCodeDescription.set, None, None)

    
    # Element {http://www.litle.com/schema}fromQueue uses Python identifier fromQueue
    __fromQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fromQueue'), 'fromQueue', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemafromQueue', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 60, 12), )

    
    fromQueue = property(__fromQueue.value, __fromQueue.set, None, None)

    
    # Element {http://www.litle.com/schema}toQueue uses Python identifier toQueue
    __toQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'toQueue'), 'toQueue', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschematoQueue', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 61, 12), )

    
    toQueue = property(__toQueue.value, __toQueue.set, None, None)

    
    # Element {http://www.litle.com/schema}currentQueue uses Python identifier currentQueue
    __currentQueue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentQueue'), 'currentQueue', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemacurrentQueue', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 62, 12), )

    
    currentQueue = property(__currentQueue.value, __currentQueue.set, None, None)

    
    # Element {http://www.litle.com/schema}settlementAmount uses Python identifier settlementAmount
    __settlementAmount = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'settlementAmount'), 'settlementAmount', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemasettlementAmount', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12), )

    
    settlementAmount = property(__settlementAmount.value, __settlementAmount.set, None, None)

    
    # Element {http://www.litle.com/schema}settlementCurrencyType uses Python identifier settlementCurrencyType
    __settlementCurrencyType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrencyType'), 'settlementCurrencyType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemasettlementCurrencyType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12), )

    
    settlementCurrencyType = property(__settlementCurrencyType.value, __settlementCurrencyType.set, None, None)

    
    # Element {http://www.litle.com/schema}notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'notes'), 'notes', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemanotes', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudNotificationStatus uses Python identifier fraudNotificationStatus
    __fraudNotificationStatus = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationStatus'), 'fraudNotificationStatus', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemafraudNotificationStatus', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12), )

    
    fraudNotificationStatus = property(__fraudNotificationStatus.value, __fraudNotificationStatus.set, None, None)

    
    # Element {http://www.litle.com/schema}fraudNotificationDate uses Python identifier fraudNotificationDate
    __fraudNotificationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationDate'), 'fraudNotificationDate', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemafraudNotificationDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12), )

    
    fraudNotificationDate = property(__fraudNotificationDate.value, __fraudNotificationDate.set, None, None)

    
    # Element {http://www.litle.com/schema}retrievalRequestType uses Python identifier retrievalRequestType
    __retrievalRequestType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'retrievalRequestType'), 'retrievalRequestType', '__httpwww_litle_comschema_caseActivityType_httpwww_litle_comschemaretrievalRequestType', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12), )

    
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
_module_typeBindings.caseActivityType = caseActivityType
Namespace.addCategoryObject('typeBinding', 'caseActivityType', caseActivityType)


# Complex type {http://www.litle.com/schema}caseUpdateType with content type ELEMENT_ONLY
class caseUpdateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.litle.com/schema}caseUpdateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'caseUpdateType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseId uses Python identifier caseId
    __caseId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseId'), 'caseId', '__httpwww_litle_comschema_caseUpdateType_httpwww_litle_comschemacaseId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 162, 12), )

    
    caseId = property(__caseId.value, __caseId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantActivityId uses Python identifier merchantActivityId
    __merchantActivityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantActivityId'), 'merchantActivityId', '__httpwww_litle_comschema_caseUpdateType_httpwww_litle_comschemamerchantActivityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 163, 12), )

    
    merchantActivityId = property(__merchantActivityId.value, __merchantActivityId.set, None, None)

    
    # Element {http://www.litle.com/schema}activity uses Python identifier activity
    __activity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activity'), 'activity', '__httpwww_litle_comschema_caseUpdateType_httpwww_litle_comschemaactivity', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 164, 12), )

    
    activity = property(__activity.value, __activity.set, None, None)

    _ElementMap.update({
        __caseId.name() : __caseId,
        __merchantActivityId.name() : __merchantActivityId,
        __activity.name() : __activity
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.caseUpdateType = caseUpdateType
Namespace.addCategoryObject('typeBinding', 'caseUpdateType', caseUpdateType)


# Complex type {http://www.litle.com/schema}caseUpdateResponseType with content type ELEMENT_ONLY
class caseUpdateResponseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.litle.com/schema}caseUpdateResponseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'caseUpdateResponseType')
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 183, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}phoenixTxnId uses Python identifier phoenixTxnId
    __phoenixTxnId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'phoenixTxnId'), 'phoenixTxnId', '__httpwww_litle_comschema_caseUpdateResponseType_httpwww_litle_comschemaphoenixTxnId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 185, 12), )

    
    phoenixTxnId = property(__phoenixTxnId.value, __phoenixTxnId.set, None, None)

    
    # Element {http://www.litle.com/schema}caseId uses Python identifier caseId
    __caseId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseId'), 'caseId', '__httpwww_litle_comschema_caseUpdateResponseType_httpwww_litle_comschemacaseId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 186, 12), )

    
    caseId = property(__caseId.value, __caseId.set, None, None)

    
    # Element {http://www.litle.com/schema}merchantActivityId uses Python identifier merchantActivityId
    __merchantActivityId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'merchantActivityId'), 'merchantActivityId', '__httpwww_litle_comschema_caseUpdateResponseType_httpwww_litle_comschemamerchantActivityId', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 187, 12), )

    
    merchantActivityId = property(__merchantActivityId.value, __merchantActivityId.set, None, None)

    _ElementMap.update({
        __phoenixTxnId.name() : __phoenixTxnId,
        __caseId.name() : __caseId,
        __merchantActivityId.name() : __merchantActivityId
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.caseUpdateResponseType = caseUpdateResponseType
Namespace.addCategoryObject('typeBinding', 'caseUpdateResponseType', caseUpdateResponseType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 6, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}user uses Python identifier user
    __user = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'user'), 'user', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemauser', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 8, 16), )

    
    user = property(__user.value, __user.set, None, None)

    
    # Element {http://www.litle.com/schema}password uses Python identifier password
    __password = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'password'), 'password', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemapassword', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 9, 16), )

    
    password = property(__password.value, __password.set, None, None)

    _ElementMap.update({
        __user.name() : __user,
        __password.name() : __password
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Root element for request to export chargeback activities."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 12, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}activityDate uses Python identifier activityDate
    __activityDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityDate'), 'activityDate', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaactivityDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 15, 16), )

    
    activityDate = property(__activityDate.value, __activityDate.set, None, None)

    
    # Element {http://www.litle.com/schema}financialOnly uses Python identifier financialOnly
    __financialOnly = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'financialOnly'), 'financialOnly', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemafinancialOnly', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16), )

    
    financialOnly = property(__financialOnly.value, __financialOnly.set, None, None)

    
    # Element {http://www.litle.com/schema}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authentication'), 'authentication', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaauthentication', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4), )

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_litle_comschema_CTD_ANON__version', _module_typeBindings.versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 18, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 18, 12)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __activityDate.name() : __activityDate,
        __financialOnly.name() : __financialOnly,
        __authentication.name() : __authentication
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Root element for response containing chargeback activities."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 26, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}activityDate uses Python identifier activityDate
    __activityDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'activityDate'), 'activityDate', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaactivityDate', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 28, 16), )

    
    activityDate = property(__activityDate.value, __activityDate.set, None, None)

    
    # Element {http://www.litle.com/schema}caseActivity uses Python identifier caseActivity
    __caseActivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseActivity'), 'caseActivity', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemacaseActivity', True, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16), )

    
    caseActivity = property(__caseActivity.value, __caseActivity.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_2_version', _module_typeBindings.versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 31, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 31, 12)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_2_response', _module_typeBindings.responseType, required=True)
    __response._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 32, 12)
    __response._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 32, 12)
    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_2_message', _module_typeBindings.messageType, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 33, 12)
    __message._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 33, 12)
    
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
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Root element to update to chargeback cases."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 151, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseUpdate uses Python identifier caseUpdate
    __caseUpdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseUpdate'), 'caseUpdate', '__httpwww_litle_comschema_CTD_ANON_3_httpwww_litle_comschemacaseUpdate', True, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16), )

    
    caseUpdate = property(__caseUpdate.value, __caseUpdate.set, None, None)

    
    # Element {http://www.litle.com/schema}authentication uses Python identifier authentication
    __authentication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'authentication'), 'authentication', '__httpwww_litle_comschema_CTD_ANON_3_httpwww_litle_comschemaauthentication', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4), )

    
    authentication = property(__authentication.value, __authentication.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_3_version', _module_typeBindings.versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 156, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 156, 12)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __caseUpdate.name() : __caseUpdate,
        __authentication.name() : __authentication
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Root element to give responses to update requests."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 172, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}caseUpdateResponse uses Python identifier caseUpdateResponse
    __caseUpdateResponse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'caseUpdateResponse'), 'caseUpdateResponse', '__httpwww_litle_comschema_CTD_ANON_4_httpwww_litle_comschemacaseUpdateResponse', True, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16), )

    
    caseUpdateResponse = property(__caseUpdateResponse.value, __caseUpdateResponse.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_litle_comschema_CTD_ANON_4_version', _module_typeBindings.versionType, required=True)
    __version._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 177, 12)
    __version._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 177, 12)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'response'), 'response', '__httpwww_litle_comschema_CTD_ANON_4_response', _module_typeBindings.responseType, required=True)
    __response._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 178, 12)
    __response._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 178, 12)
    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute message uses Python identifier message
    __message = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'message'), 'message', '__httpwww_litle_comschema_CTD_ANON_4_message', _module_typeBindings.messageType, required=True)
    __message._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 179, 12)
    __message._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 179, 12)
    
    message = property(__message.value, __message.set, None, None)

    _ElementMap.update({
        __caseUpdateResponse.name() : __caseUpdateResponse
    })
    _AttributeMap.update({
        __version.name() : __version,
        __response.name() : __response,
        __message.name() : __message
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


authentication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authentication'), CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4))
Namespace.addCategoryObject('elementBinding', authentication.name().localName(), authentication)

litleChargebackActivitiesRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'litleChargebackActivitiesRequest'), CTD_ANON_, documentation='Root element for request to export chargeback activities.', location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 8, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackActivitiesRequest.name().localName(), litleChargebackActivitiesRequest)

litleChargebackActivitiesResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'litleChargebackActivitiesResponse'), CTD_ANON_2, documentation='Root element for response containing chargeback activities.', location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 22, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackActivitiesResponse.name().localName(), litleChargebackActivitiesResponse)

litleChargebackUpdateRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'litleChargebackUpdateRequest'), CTD_ANON_3, documentation='Root element to update to chargeback cases.', location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 147, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackUpdateRequest.name().localName(), litleChargebackUpdateRequest)

litleChargebackUpdateResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'litleChargebackUpdateResponse'), CTD_ANON_4, documentation='Root element to give responses to update requests.', location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 168, 4))
Namespace.addCategoryObject('elementBinding', litleChargebackUpdateResponse.name().localName(), litleChargebackUpdateResponse)



caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseId'), litleIdType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 39, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantId'), merchantIdentificationType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 40, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dayIssuedByBank'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 41, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dayReceivedByLitle'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 42, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cycle'), cycleType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 43, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'litleTxnId'), litleIdType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 44, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantTxnId'), string25Type, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 45, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orderId'), string25Type, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 46, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cardNumberLast4'), cardNumberLast4Type, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 47, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cardType'), methodOfPaymentTypeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 48, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chargebackAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 49, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chargebackCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 50, 12), unicode_default='USD'))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'originalTransactionDay'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 51, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chargebackType'), chargebackType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 52, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityType'), activityType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 53, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'representedAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'representedCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'preArbAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'preArbCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reasonCode'), pyxb.binding.datatypes.string, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 58, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'reasonCodeDescription'), pyxb.binding.datatypes.string, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 59, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fromQueue'), queueType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 60, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'toQueue'), queueType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 61, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentQueue'), queueType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 62, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'settlementAmount'), transactionAmountType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrencyType'), currencyCodeEnum, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'notes'), pyxb.binding.datatypes.string, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationStatus'), fraudNotificationStatusType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationDate'), pyxb.binding.datatypes.date, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12)))

caseActivityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'retrievalRequestType'), retrievalRequestType, scope=caseActivityType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 40, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dayIssuedByBank')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 41, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dayReceivedByLitle')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 42, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cycle')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 43, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'litleTxnId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 44, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantTxnId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 45, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'orderId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 46, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cardNumberLast4')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 47, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cardType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 48, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chargebackAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 49, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chargebackCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 50, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'originalTransactionDay')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 51, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chargebackType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 52, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 53, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'representedAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 54, 12))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'representedCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 55, 12))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'preArbAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 56, 12))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'preArbCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 57, 12))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reasonCode')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 58, 12))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'reasonCodeDescription')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 59, 12))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fromQueue')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 60, 12))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'toQueue')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 61, 12))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentQueue')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 62, 12))
    st_23 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'settlementAmount')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 63, 12))
    st_24 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'settlementCurrencyType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 64, 12))
    st_25 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'notes')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 65, 12))
    st_26 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationStatus')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 66, 12))
    st_27 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fraudNotificationDate')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 67, 12))
    st_28 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(caseActivityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'retrievalRequestType')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 68, 12))
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




caseUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseId'), litleIdType, scope=caseUpdateType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 162, 12)))

caseUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantActivityId'), string25Type, scope=caseUpdateType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 163, 12)))

caseUpdateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activity'), activityType, scope=caseUpdateType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 164, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 162, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantActivityId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 163, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(caseUpdateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activity')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 164, 12))
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




caseUpdateResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'phoenixTxnId'), litleIdType, scope=caseUpdateResponseType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 185, 12)))

caseUpdateResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseId'), litleIdType, scope=caseUpdateResponseType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 186, 12)))

caseUpdateResponseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'merchantActivityId'), string25Type, scope=caseUpdateResponseType, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 187, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'phoenixTxnId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 185, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(caseUpdateResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 186, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(caseUpdateResponseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'merchantActivityId')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 187, 12))
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




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'user'), string20Type, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 8, 16)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'password'), string20Type, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 9, 16)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'user')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 8, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'password')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 9, 16))
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




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 15, 16)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'financialOnly'), pyxb.binding.datatypes.boolean, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authentication'), CTD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authentication')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 14, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityDate')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 15, 16))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'financialOnly')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 16, 16))
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




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'activityDate'), pyxb.binding.datatypes.date, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 28, 16)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseActivity'), caseActivityType, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'activityDate')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 28, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseActivity')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 29, 16))
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




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseUpdate'), caseUpdateType, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16)))

CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'authentication'), CTD_ANON, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleCommon_v7.xsd', 5, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'authentication')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 153, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseUpdate')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 154, 16))
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




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'caseUpdateResponse'), caseUpdateResponseType, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'caseUpdateResponse')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargeback_v2.2.xsd', 174, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_7()

