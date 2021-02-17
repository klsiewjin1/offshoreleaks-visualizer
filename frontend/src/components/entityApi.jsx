import settings from '../config/settings';
import axios from 'axios';
import React, {Component} from 'react';

const {apiBaseURL} = settings;


class EntityApi extends Component {
    constructor(props) {
        super(props);

        this.state = {
            hits: [],
            isLoading: false,
            error: null
        }
    }

    componentWillMount() {
        this.setState({isLoading: true});
        axios.get(apiBaseURL + "/entities/")
            .then(result => this.setState({hits: result.data, isLoading: false}))
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
            <ul>
                {hits.map(hit =>
                    <li key={hit.node_id}>
                        {hit.name}
                    </li>
                )}
            </ul>
        );
    }
}

export default EntityApi;