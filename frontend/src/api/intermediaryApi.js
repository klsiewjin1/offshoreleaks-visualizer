import axios from "axios";
import {apiBaseURL} from "../config/settings";

export default class IntermediaryApi {
    static getIntermediaries() {
        return axios.get(apiBaseURL + "/intermediaries")
            .then(response => response.data)
    }

    static getIntermediariesByNodeId(nodeId) {
        return axios.get(apiBaseURL + `/intermediaries/${nodeId}/react-force-graph`)
            .then(response => response.data)
    }
}