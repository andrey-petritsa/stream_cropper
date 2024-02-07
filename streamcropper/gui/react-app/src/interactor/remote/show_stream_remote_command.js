import axios from "axios";
import {remote_address} from "./remote_address";

export default class ShowStreamRemoteCommand {
    async execute(streamId, momentRadius=2) {
        const response = await axios.get(remote_address + `/show-stream?streamId=${streamId}&momentRadius=${momentRadius}`)
        const stream = response.data

        return stream
    }
}
