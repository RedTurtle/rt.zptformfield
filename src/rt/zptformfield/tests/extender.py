# -*- coding: utf-8 -*-

from Products.ATContentTypes.interfaces import IATContentType
from Products.Archetypes import atapi
from archetypes.referencebrowserwidget import ReferenceBrowserWidget
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.component import adapts
from zope.interface import implements


class BlobLinesField(ExtensionField, atapi.LinesField):
     """A trivial field."""

class BlobStringField(ExtensionField, atapi.StringField):
     """A trivial field."""


class FooExtender(object):
    adapts(IATContentType)
    implements(ISchemaExtender)

    fields = [
        BlobStringField("foo_field",
            widget = ReferenceBrowserWidget(
                label="Useless, invisible field",
                visible={'view': 'invisible', 'edit': 'invisible'},
            ),
        ),
        BlobLinesField("foo_multivalued_field",
            multiValued=True,
            widget = ReferenceBrowserWidget(
                label="Useless, invisible multivalued field",
                visible={'view': 'invisible', 'edit': 'invisible'},
            ),
        ),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
