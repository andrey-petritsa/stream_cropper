import {useEffect, useState} from "react";
import './Stream.css'
import {Link} from "react-router-dom";

export default function IndexPage(props) {
    const [streams, setStreams] = useState([]);

    useEffect(() => {
        global.interactor.show_all_stream_info_command.execute().then(streams => setStreams(streams))
    }, []);

    return (
        <div className={'index-page'}>
            <div className={'streams-container'}>
                {
                    streams.map((stream) => {
                        return (
                            <div className={'stream-info'}>
                                <div className={'stream-info__streamer'}>{stream.streamer.name}</div>
                                <div className={'stream-info__name'}>{stream.name}</div>
                                <div className={'stream-info__date'}>{stream.started_at}</div>
                                <Link to={`stream/${stream.id}`}>Посмотреть</Link>

                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
}