export default class ShowStreamStubCommand {
    async execute(streamId, moment_radius=2) {
        return {
            'id': '1',
            'name': 'Стрим программиста acrosspaper',
            'streamer': {
                'name': 'acrosspaper'
            },
            'started_at': '2011-11-04 12:00:00',
            'messages': [
                {
                    'datetime': '2011-11-04 12:05:23',
                    'text': 'привет мир',
                    'user': {
                        'role': 'anon',
                        'name': 'andry'
                    }
                },
                {
                    'datetime': '2011-11-04 12:05:25',
                    'text': 'и тебе привет! @andry',
                    'user': {
                        'role': 'anon',
                        'name': 'vasya'
                    }
                }
            ],
            'moments': [
                {
                    "delta": {
                      "start": "0:00:23",
                      "end": "0:00:28",
                    },
                    "delta_sec": {
                        "start": "23",
                        "end": "28",
                    },
                    'start': '2011-11-04 12:00:00',
                    'weight': 2,
                },
                {
                    "delta": {
                        "start": "0:01:00",
                        "end": "0:01:20",
                    },
                    "delta_sec": {
                        "start": "60",
                        "end": "80",
                    },
                    'start': '2011-11-04 12:00:00',
                    'weight': 8,
                },
            ]
        }
    }
}