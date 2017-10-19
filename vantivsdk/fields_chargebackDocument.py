# ./fields_chargebackDocument.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f03bd2be92cca0df00d3d054794f8a47756ec009
# Generated 2017-10-19 11:55:28.900736 by PyXB version 1.2.5 using Python 3.6.1.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:edaac942-b4e5-11e7-8b3f-001a4a01074d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
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


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 11, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemaResponseCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 5, 12), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {http://www.litle.com/schema}ResponseMessage uses Python identifier ResponseMessage
    __ResponseMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseMessage'), 'ResponseMessage', '__httpwww_litle_comschema_CTD_ANON_httpwww_litle_comschemaResponseMessage', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 6, 12), )

    
    ResponseMessage = property(__ResponseMessage.value, __ResponseMessage.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 13, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 13, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __ResponseMessage.name() : __ResponseMessage
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 18, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}ChargebackCase uses Python identifier ChargebackCase
    __ChargebackCase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChargebackCase'), 'ChargebackCase', '__httpwww_litle_comschema_CTD_ANON__httpwww_litle_comschemaChargebackCase', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 26, 4), )

    
    ChargebackCase = property(__ChargebackCase.value, __ChargebackCase.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_litle_comschema_CTD_ANON__id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 22, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 22, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __ChargebackCase.name() : __ChargebackCase
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 27, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.litle.com/schema}ResponseCode uses Python identifier ResponseCode
    __ResponseCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), 'ResponseCode', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaResponseCode', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 5, 12), )

    
    ResponseCode = property(__ResponseCode.value, __ResponseCode.set, None, None)

    
    # Element {http://www.litle.com/schema}ResponseMessage uses Python identifier ResponseMessage
    __ResponseMessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResponseMessage'), 'ResponseMessage', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaResponseMessage', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 6, 12), )

    
    ResponseMessage = property(__ResponseMessage.value, __ResponseMessage.set, None, None)

    
    # Element {http://www.litle.com/schema}Document uses Python identifier Document
    __Document = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Document'), 'Document', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaDocument', False, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 10, 4), )

    
    Document = property(__Document.value, __Document.set, None, None)

    
    # Element {http://www.litle.com/schema}DocumentEntry uses Python identifier DocumentEntry
    __DocumentEntry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DocumentEntry'), 'DocumentEntry', '__httpwww_litle_comschema_CTD_ANON_2_httpwww_litle_comschemaDocumentEntry', True, pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 30, 16), )

    
    DocumentEntry = property(__DocumentEntry.value, __DocumentEntry.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_2_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 37, 12)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 37, 12)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __ResponseCode.name() : __ResponseCode,
        __ResponseMessage.name() : __ResponseMessage,
        __Document.name() : __Document,
        __DocumentEntry.name() : __DocumentEntry
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 31, 20)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_litle_comschema_CTD_ANON_3_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 32, 24)
    __id._UseLocation = pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 32, 24)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Document'), CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 10, 4))
Namespace.addCategoryObject('elementBinding', Document.name().localName(), Document)

Merchant = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Merchant'), CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 17, 4))
Namespace.addCategoryObject('elementBinding', Merchant.name().localName(), Merchant)

ChargebackCase = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargebackCase'), CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 26, 4))
Namespace.addCategoryObject('elementBinding', ChargebackCase.name().localName(), ChargebackCase)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 5, 12)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseMessage'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 6, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 5, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseMessage')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 6, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChargebackCase'), CTD_ANON_2, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 26, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChargebackCase')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 20, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 5, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResponseMessage'), pyxb.binding.datatypes.string, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 6, 12)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Document'), CTD_ANON, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 10, 4)))

CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DocumentEntry'), CTD_ANON_3, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 30, 16)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseCode')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 5, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResponseMessage')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 6, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DocumentEntry')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 30, 16))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Document')), pyxb.utils.utility.Location('/usr/local/litle-home/nmerchan/git/cnp-chargeback-sdk-python/schema/litleChargebackWebService_v1.0.xsd', 35, 16))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()

