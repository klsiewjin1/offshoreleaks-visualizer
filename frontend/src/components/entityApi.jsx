import settings from '../config/settings';
import axios from 'axios';
import React, {Component} from 'react';
import {ForceGraph2D} from "react-force-graph";

const {apiBaseURL} = settings;


class EntityApi extends Component {
    constructor(props) {
        super(props);

        this.state = {
            hits: {},
            isLoading: false,
            error: null
        }
    }

    componentWillMount() {
        this.setState({isLoading: true});
        axios.get(apiBaseURL + "/entities/")
            .then(result => this.setState({hits: {"nodes":result.data, "links": []}, isLoading: false}))
            .catch(error => this.setState({error, isLoading: false}));
    }

    render() {
        const {hits, isLoading, error} = this.state;
        if (error) {
            return <p>{error.message}</p>
        }
        if (isLoading) {
            return <p>Loading ...</p>
        }
        return (
            <ForceGraph2D
                graphData={hits}
                nodeId={"node_id"}
            />
        );
    }
}

export default EntityApi;