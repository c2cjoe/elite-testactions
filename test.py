#!/usr/bin/env python3

import unittest
from main import decide_response

class TestChatResponse(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(decide_response("hello"), "Hello, how are you!")

    def test_bye(self):
        self.assertEqual(decide_response("bye"), "Goodbye")

    def test_howareyou(self):
        self.assertEqual(decide_response("how are you"), "I am fine, thank you.")

if __name__ == "__main__":
    unittest.main()
