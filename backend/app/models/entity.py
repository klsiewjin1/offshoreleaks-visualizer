from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship, RelationshipDefinition
)

from .nodeutils import NodeUtils


class ENTITY(StructuredNode, NodeUtils):
    sourceID = StringProperty()
    address = StringProperty()
    jurisdiction = StringProperty()
    service_provider = StringProperty()
    countries = StringProperty()
    jurisdiction_description = StringProperty()
    valid_until = StringProperty()
    ibcRUC = StringProperty()
    name = StringProperty()
    note = StringProperty()
    country_codes = StringProperty()
    incorporation_date = StringProperty()
    inactivation_date = StringProperty()
    struck_off_date = StringProperty()
    closed_date = StringProperty()
    node_id = StringProperty(index=True)
    status = StringProperty()
    company_type = StringProperty()
    officers = RelationshipFrom('.officer.OFFICER', 'officer_of')
    intermediaries = RelationshipFrom('.intermediary.INTERMEDIARY', 'intermediary_of')
    addresses = RelationshipTo('.address.ADDRESS', 'registered_address')
    others = RelationshipFrom('.other.OTHER', 'connected_to')
    entities = Relationship('.entity.ENTITY', None)

    @property
    def serialize(self):
        return {
            'node_properties': {
                'sourceID': self.sourceID,
                'address': self.address,
                'jurisdiction': self.jurisdiction,
                'service_provider': self.service_provider,
                'countries': self.countries,
                'jurisdiction_description': self.jurisdiction_description,
                'valid_until': self.valid_until,
                'ibcRUC': self.ibcRUC,
                'name': self.name,
                'note': self.note,
                'country_codes': self.country_codes,
                'incorporation_date': self.incorporation_date,
                'inactivation_date': self.inactivation_date,
                'struck_off_date': self.struck_off_date,
                'closed_date': self.closed_date,
                'node_id': self.node_id,
                'status': self.status,
                'company_type': self.company_type
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
            {
                'nodes_type': 'ADDRESS',
                'nodes_related': self.serialize_relationships(self.addresses.all()),
            },
            {
                'nodes_type': 'OTHER',
                'nodes_related': self.serialize_relationships(self.others.all()),
            },
            {
                'nodes_type': 'ENTITY',
                'nodes_related': self.serialize_relationships(self.entities.all())
            },
        ]
