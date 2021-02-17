from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    Relationship
)

from .nodeutils import NodeUtils


class OTHER(StructuredNode, NodeUtils):
    sourceID = StringProperty()
    name = StringProperty()
    valid_until = StringProperty()
    node_id = StringProperty(index=True)
    countries = StringProperty()
    country_codes = StringProperty()
    note = StringProperty()

    addresses = RelationshipTo('.address.ADDRESS', 'registered_address')
    officers = Relationship('.officer.OFFICER', None)
    entities = Relationship('.entity.ENTITY', None)

    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'name': self.name,
                'countries': self.countries,
                'valid_until': self.valid_until,
                'node_id': self.node_id,
                'country_codes': self.country_codes,
                'note': self.note
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
                'nodes_type': 'ENTITY',
                'nodes_related': self.serialize_relationships(self.entities.all()),
            },
            {
                'nodes_type': 'ADDRESS',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
        ]
