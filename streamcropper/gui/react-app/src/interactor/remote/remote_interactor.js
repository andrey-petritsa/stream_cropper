import ShowAllStreamInfoRemoteCommand from "./show_all_stream_info_remote_command";
import ShowStreamRemoteCommand from "./show_stream_remote_command";

export default class RemoteInteractor {
    show_all_stream_info_command = new ShowAllStreamInfoRemoteCommand()
    show_stream_command = new ShowStreamRemoteCommand()
}