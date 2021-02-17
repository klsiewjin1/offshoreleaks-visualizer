from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    Relationship
)

from .nodeutils import NodeUtils


class INTERMEDIARY(StructuredNode, NodeUtils):
    sourceID = StringProperty()
    valid_until = StringProperty()
    name = StringProperty()
    country_codes = StringProperty()
    countries = StringProperty()
    node_id = StringProperty(index=True)
    status = StringProperty()
    note = StringProperty()
    entities = RelationshipTo('.entity.ENTITY', 'intermediary_of')
    addresses = RelationshipTo('.address.ADDRESS', 'registered_address')
    officers = Relationship('.officer.OFFICER', None)

    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'valid_until': self.valid_until,
                'name': self.name,
                'country_codes': self.country_codes,
                'countries': self.countries,
                'node_id': self.node_id,
                'status': self.status,
                'note': self.note
            },
            'node_type': self.__label__
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'ENTITY',
                'nodes_related': self.serialize_relationships(self.entities.all()),
            },
            {
                'nodes_type': 'ADDRESS',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
            {
                'nodes_type': 'OFFICER',
                'nodes_related': self.serialize_relationships(self.officers.all()),
            },
        ]
