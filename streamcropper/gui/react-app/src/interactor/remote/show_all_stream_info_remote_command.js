import axios from "axios";
import {remote_address} from "./remote_address";

export default class ShowAllStreamInfoRemoteCommand {
    async execute() {
        const response = await axios.get(remote_address + '/show-all-stream-info')
        const streams = response.data

        return streams
    }
}
