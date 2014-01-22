import unittest
import nlpbot


class TestSimple(unittest.TestCase):
    def test_simple_learn_and_gen(self):
        nlpbot.learn('This is a test sentence.')
        self.assertEqual(nlpbot.generate_output(), 'This is a test sentence')
