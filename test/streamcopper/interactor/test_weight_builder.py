import unittest
from datetime import datetime

from interactor import Message
from interactor.stream_analyzer.weight_builder import WeightBuilder
from test_helpers.message_builder import MessageBuilder


class WeightBuilderTest(unittest.TestCase):
    weightBuilder = WeightBuilder()
    msgBuilder = MessageBuilder()

    def test_weight(self):
        explosions = [
            [
                self.msgBuilder.create_message('0:0:15'),
                self.msgBuilder.create_message('0:0:16')
            ],
            [
                self.msgBuilder.create_message('0:0:32'),
                self.msgBuilder.create_message('0:0:34'),
                self.msgBuilder.create_message('0:0:35')
            ]
        ]
        stream_analyze = {
            'explosions': explosions,
            'info': {
                'first_message': Message(datetime(1996, 6, 25, 0, 0, 15), None, None)
            }
        }

        weights = self.weightBuilder.build(stream_analyze)

        self.assertEqual({'weight': 3, 'seconds_time': 17.0, 'time_delta': '0:00:17'}, weights[0])
        self.assertEqual({'weight': 2, 'seconds_time': 0.0, 'time_delta': '0:00:00'}, weights[1])
