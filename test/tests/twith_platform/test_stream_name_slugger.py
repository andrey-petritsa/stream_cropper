import unittest

from twith_platform.stream_name_slugger import StreamNameSlugger


class TestStreamNameSlugger(unittest.TestCase):
    def setUp(self):
        self.stream_name_slugger = StreamNameSlugger()

    def tearDown(self):
        pass

    def test_slug(self):
        slugger = StreamNameSlugger()

        self.assertEqual("Название_стрима", slugger.slug("Название стрима"), )
        self.assertEqual("Название_стрима", slugger.slug("Название стрима!"),)
        self.assertEqual("Название_стрима_2", slugger.slug("Название стрима! 2"),)
        self.assertEqual("Название_стрима_2", slugger.slug("Название, стрима! 2"),)
        self.assertEqual("GOOD_Название_стрима_2", slugger.slug("GOOD Название, стрима! 2"),)
