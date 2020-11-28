import unittest
from database import *


class DatabaseTest(unittest.TestCase):
    def test_source_name(self):
        df = connect()
        self.assertEqual(source_name(df, ""), "")
        self.assertEqual(source_name(df, "random text"), "")
        self.assertEqual(source_name(df, "https://twitter.com/post/exampletwitter"), "")
        # self.assertEqual()

    def test_source_bias(self):
        df = connect()
        self.assertEqual(source_bias(df, ""), "")
        self.assertEqual(source_bias(df, "random text"), "")
        self.assertEqual(source_bias(df, "https://twitter.com/post/exampletwitter"), "")

if __name__ == '__main__':
    unittest.main()
