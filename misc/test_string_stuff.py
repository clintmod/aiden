#!/usr/bin/env python

import unittest
import string_stuff

class TestJoin(unittest.TestCase):

  def test_join_strings_works(self):
    result = string_stuff.join_strings(['aiden', 'is', 'cool'])
    self.assertEqual("aiden is cool", result)

  def test_join_strings_works_with_one_element(self):
    result = string_stuff.join_strings(["15"])
    self.assertEqual("15", result)

  def test_join_strings_works_with_no_elements(self):
    result = string_stuff.join_strings([])
    self.assertEqual("", result)

if __name__ == '__main__':
    unittest.main()
