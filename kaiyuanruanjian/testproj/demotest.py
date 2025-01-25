#!/usr/bin/env python
# coding: utf-8

import unittest
import re

class MyFirstTest(unittest.TestCase):
    def test_3(self):
        self.assertEqual("hello" " world", "hello world")

    def test_1(self):
        self.assertTrue(3 > 2)

    def test_2(self):
        self.assertRegex("abb", re.compile(r"b{2}"))

if __name__ == "__main__":
    unittest.main()
