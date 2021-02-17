import React, {Component} from 'react';
import {ForceGraph2D} from "react-force-graph";
import NewEntityApi from "../api/entityApi";

class Graph2D extends Component {
    constructor(props) {
        super(props);

        this.state = {
            data: {nodes: [{node_id: "Joe"}, {node_id: "Jane"}], links: [{source: "Joe", target: "Jane"}]},
            isLoading: false,
            error: null
        }
    }

    loadData = async () => {
        let nodes = await NewEntityApi.getEntities();
        let links_holder = []
        let nodes_holder = []
        let index = 0;
        for (index; index < nodes.length; ++index) {
            let links_and_nodes = await NewEntityApi.getEntitiesByNodeId(nodes[index].node_id)
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
                              linkDirectionalArrowLength={2}/>
            </div>

        );
    }
}

export default Graph2D