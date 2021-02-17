import axios from "axios";
import {apiBaseURL} from "../config/settings";

export default class NewEntityApi {
    static getEntities() {
        return axios.get(apiBaseURL + "/entities")
            .then(response => response.data)
    }

    static getEntitiesByNodeId(nodeId) {
        return axios.get(apiBaseURL + `/entities/${nodeId}/react-force-graph`)
            .then(response => response.data)
    }
}