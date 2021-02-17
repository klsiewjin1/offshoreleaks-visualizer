from fastapi import HTTPException


def get_node_from_neomodel(model, **kwargs):
    node = model.nodes.get_or_none(**kwargs)
    if not node:
        raise HTTPException(status_code=404, detail=f"{model.__label__.title()} not found")

    return node


def get_nodes_and_relationships(model, **kwargs):
    """Instead of having to do the transformations on front-end, do it here and create a custom endpoint"""
    node = get_node_from_neomodel(model, **kwargs)
    # We can do a BFS here with depth to run order-level traversals
    connected_nodes = node.serialize_connections
    serialized = node.serialize
    tmp = serialized.get("node_properties")
    tmp["node_type"] = serialized.get("node_type")
    nodes = [tmp]
    relationships = []
    for relationship_type in connected_nodes:
        if len(relationship_type.get("nodes_related")) > 0:
            rel_type = relationship_type.get("nodes_type")
            for connected_node in relationship_type.get("nodes_related"):
                tmp = connected_node.get("node_properties")
                tmp["node_type"] = connected_node.get("node_type")
                nodes.append(tmp)
                relationships.append(
                    {"source": node.node_id, "target": connected_node.get("node_properties").get("node_id"),
                     "type": rel_type, "name": connected_node.get("node_type")})
    return {"nodes": nodes, "links": relationships}
