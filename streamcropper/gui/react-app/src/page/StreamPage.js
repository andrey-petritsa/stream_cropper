import {useParams} from "react-router-dom";
import {createRef, useEffect, useState} from "react";
import Hls from 'hls.js';

export default function StreamPage(props) {
    const [stream, setStream] = useState({'messages': [], "moments": []});
    const { streamId } = useParams();
    const videoRef = createRef();

    useEffect(() => {
        global.interactor.show_stream_command.execute(streamId).then(stream => setStream(stream))
        var hls = new Hls()
        hls.loadSource(`http://80.68.156.108:7000/${streamId}/video.m3u8`)
        hls.attachMedia(videoRef.current)
    }, []);

    function onMomentClick(e) {
        e.preventDefault()
        const secDelta = Number(e.target.dataset.deltasec)
        videoRef.current.currentTime = secDelta
    }

    return (
        <div className={'stream-page'}>
            <div className={'stream'}>
                <div className={'stream__name'}>{stream.name}</div>
                <div className={'stream__date'}>{stream.started_at}</div>
                <video
                    className={'stream__video'}
                    autoPlay
                    controls
                    ref={videoRef}
                ></video>
                <div className={'stream__moments'}>
                    {stream.moments.map(moment => {return (
                        <div className={'stream__moment'}>
                            <div>{moment.weight} | {moment.delta.start}</div>
                            <button onClick={onMomentClick} data-deltasec={moment.delta_sec.start}>Посмотреть</button>
                        </div>
                    )})}
                </div>
                <div className={'stream__chat'}>
                    {stream.messages.map(message => {return (
                        <div className={'stream__message'}>
                            <div>{message.user.name} | {message.text}</div>
                        </div>
                    )})}
                </div>
            </div>
        </div>
    )
}