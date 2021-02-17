import axios from "axios";
import {apiBaseURL} from "../config/settings";

export default class AddressApi {
    static getAddresses() {
        return axios.get(apiBaseURL + "/addresses")
            .then(response => response.data)
    }

    static getAddressesByNodeId(nodeId) {
        return axios.get(apiBaseURL + `/addresses/${nodeId}/react-force-graph`)
            .then(response => response.data)
    }
}