import React, {Component} from 'react';
import {ForceGraph2D} from "react-force-graph";
import EntityApi from "../api/entityApi";
import AddressApi from "../api/addressApi";
import OfficerApi from "../api/officerApi";
import IntermediaryApi from "../api/intermediaryApi";
import OtherApi from "../api/otherApi";

class Graph2D extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: {nodes: [{node_id: "Joe"}, {node_id: "Jane"}], links: [{source: "Joe", target: "Jane"}]},
            isLoading: false,
            error: null
        }
    }

    getNodeData = async (node) => {
        //TODO Handle duplicates
        console.log("forcegraph click on ", node)
        if (node) {
            let current_data = this.state.data
            let existing_node = current_data.nodes.filter(n =>
                n.node_id === node.node_id
            )[0]
            // Nodes with more than 1 relationship have already been traversed
            let node_relationships = current_data.links.filter(r => r.source.node_id === existing_node.node_id || r.target.node_id === existing_node.node_id)
            if (node_relationships.length > 1) {
                return
            }
            let links_holder = []
            let nodes_holder = []
            if (node.node_type === "ENTITY") {
                let links_and_nodes = await EntityApi.getEntitiesByNodeId(node.node_id)
                links_holder.push(...links_and_nodes.links)
                nodes_holder.push(...links_and_nodes.nodes.filter(new_node => new_node.node_id !== node.node_id))
            } else if (node.node_type === "ADDRESS") {
                let links_and_nodes = await AddressApi.getAddressesByNodeId(node.node_id)
                links_holder.push(...links_and_nodes.links)
                nodes_holder.push(...links_and_nodes.nodes.filter(new_node => new_node.node_id !== node.node_id))
            } else if (node.node_type === "OFFICER") {
                let links_and_nodes = await OfficerApi.getOfficersByNodeId(node.node_id)
                links_holder.push(...links_and_nodes.links)
                nodes_holder.push(...links_and_nodes.nodes.filter(new_node => new_node.node_id !== node.node_id))
            } else if (node.node_type === "INTERMEDIARY") {
                let links_and_nodes = await IntermediaryApi.getIntermediariesByNodeId(node.node_id)
                links_holder.push(...links_and_nodes.links)
                nodes_holder.push(...links_and_nodes.nodes.filter(new_node => new_node.node_id !== node.node_id))
            } else if (node.node_type === "OTHER") {
                let links_and_nodes = await OtherApi.getOthersByNodeId(node.node_id)
                links_holder.push(...links_and_nodes.links)
                nodes_holder.push(...links_and_nodes.nodes.filter(new_node => new_node.node_id !== node.node_id))
            }
            let nodes = [...current_data.nodes, ...nodes_holder]
            let links = [...current_data.links, ...links_holder]
            this.setState({data: {nodes: nodes, links: links}})
        }
    }

    loadData = async () => {
        let nodes = await EntityApi.getEntities();
        let links_holder = []
        let nodes_holder = []
        let index = 0;
        for (index; index < nodes.length; ++index) {
            //This is really inefficient. Instead, pass all the node ids to the backend to be processed in a go,
            // or parallelize this with some passing to some event loop and gather at the end
            let links_and_nodes = await EntityApi.getEntitiesByNodeId(nodes[index].node_id)
            links_holder.push(...links_and_nodes.links)
            nodes_holder.push(...links_and_nodes.nodes)
        }
        let holder = {links: links_holder, nodes: nodes_holder}
        this.setState({
            isLoading: false,
            data: holder
        })
    }

    render() {
        const {data, isLoading, error} = this.state;
        if (error) {
            return <p>{error.message}</p>
        }
        if (isLoading) {
            return <p>Loading ...</p>
        }
        return (
            <div>
                <button onClick={this.loadData}>Reload</button>
                <ForceGraph2D graphData={this.state.data}
                              nodeId={"node_id"}
                              nodeLabel={"name"}
                              nodeAutoColorBy={"node_type"}
                              linkCurvature={0.2}
                              linkDirectionalArrowRelPos={1}
                              linkDirectionalArrowLength={2}
                              onNodeClick={this.getNodeData}
                />
            </div>

        );
    }
}

export default Graph2D