from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipFrom
)

from .nodeutils import NodeUtils


class ADDRESS(StructuredNode, NodeUtils):
    name = StringProperty()
    sourceID = StringProperty()
    country_codes = StringProperty()
    valid_until = StringProperty()
    address = StringProperty()
    countries = StringProperty()
    node_id = StringProperty(index=True)
    note = StringProperty()
    officers = RelationshipFrom('.officer.OFFICER', 'registered_address')
    intermediaries = RelationshipFrom('.intermediary.INTERMEDIARY', 'registered_address')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'name': self.name,
                'note': self.note,
                'sourceID': self.sourceID,
                'country_codes': self.country_codes,
                'valid_until': self.valid_until,
                'address': self.address,
                'countries': self.countries,
                'node_id': self.node_id,
            },
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'OFFICER',
                'nodes_related': self.serialize_relationships(self.officers.all()),
            },
            {
                'nodes_type': 'INTERMEDIARY',
                'nodes_related': self.serialize_relationships(self.intermediaries.all()),
            },
        ]
