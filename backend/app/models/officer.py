from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    Relationship
)

from .nodeutils import NodeUtils


class OFFICER(StructuredNode, NodeUtils):
    sourceID = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    valid_until = StringProperty()
    countries = StringProperty()
    node_id = StringProperty(index=True)
    note = StringProperty()
    addresses = RelationshipTo('.address.ADDRESS', 'registered_address')
    entities = RelationshipTo('.entity.ENTITY', 'officer_of')
    officers = Relationship('.officer.OFFICER', None)

    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'name': self.name,
                'country_codes': self.country_codes,
                'valid_until': self.valid_until,
                'countries': self.countries,
                'node_id': self.node_id,
                'note': self.note
            },
            'node_type': self.__label__
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'ADDRESS',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
            {
                'nodes_type': 'ENTITY',
                'nodes_related': self.serialize_relationships(self.entities.all()),
            },
            {
                'nodes_type': 'OFFICER',
                'nodes_related': self.serialize_relationships(self.officers.all()),
            },
        ]
