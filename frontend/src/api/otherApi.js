import axios from "axios";
import {apiBaseURL} from "../config/settings";

export default class OtherApi {
    static getOthers() {
        return axios.get(apiBaseURL + "/others")
            .then(response => response.data)
    }

    static getOthersByNodeId(nodeId) {
        return axios.get(apiBaseURL + `/others/${nodeId}/react-force-graph`)
            .then(response => response.data)
    }
}