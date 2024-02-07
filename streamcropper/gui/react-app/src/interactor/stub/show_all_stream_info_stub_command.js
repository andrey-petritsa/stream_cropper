export default class ShowAllStreamInfoStubCommand {
    async execute() {
        return [
            {
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
                ]
            },
            {
                'id': '2',
                'name': 'Стрим juice gta 6',
                'streamer': {
                    'name': 'juice'
                },
                'started_at': '2011-11-04 12:00:00',
                'messages': [
                    {
                        'datetime': '2011-11-04 12:05:23',
                        'text': 'привет из чата',
                        'user': {
                            'role': 'anon',
                            'name': 'andry'
                        }
                    },
                    {
                        'datetime': '2011-11-04 12:05:25',
                        'text': 'привет из чата 2',
                        'user': {
                            'role': 'anon',
                            'name': 'vasya'
                        }
                    }
                ]
            }

        ]
    }
}
