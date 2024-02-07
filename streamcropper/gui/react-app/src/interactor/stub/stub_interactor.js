import ShowAllStreamInfoStubCommand from "./show_all_stream_info_stub_command";
import ShowStreamStubCommand from "./show_stream_stub_command";

export default class StubInteractor {
    show_all_stream_info_command = new ShowAllStreamInfoStubCommand()
    show_stream_command = new ShowStreamStubCommand()
}

