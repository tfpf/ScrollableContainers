import unittest

from ScrollableContainers import ScrollableFrameTk


class TestTk(unittest.TestCase):
    def setUp(self):
        self.scrollable_frame = ScrollableFrameTk()

    def test_trivial(self):
        assert True
