import axios from "axios";
import {apiBaseURL} from "../config/settings";

export default class OfficerApi {
    static getOfficers() {
        return axios.get(apiBaseURL + "/officers")
            .then(response => response.data)
    }

    static getOfficersByNodeId(nodeId) {
        return axios.get(apiBaseURL + `/officers/${nodeId}/react-force-graph`)
            .then(response => response.data)
    }
}