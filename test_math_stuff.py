#!/usr/bin/env python

import unittest
import math_stuff

class TestSum(unittest.TestCase):

  def test_sum_numbers_works(self):
    result = math_stuff.sum_numbers([15,5])
    self.assertEqual(20, result)

  def test_sum_numbers_works_with_one_element(self):
    result = math_stuff.sum_numbers([15])
    self.assertEqual(15, result)

  def test_sum_numbers_works_with_no_elements(self):
    result = math_stuff.sum_numbers([])
    self.assertEqual(0, result)

class TestMultiply(unittest.TestCase):

  def test_multiply_numbers_works(self):
    expected = 10
    result = math_stuff.multiply_numbers([2, 5])
    self.assertEqual(expected, result)

  def test_multiply_numbers_one_number(self):
    expected = 5
    result = math_stuff.multiply_numbers([5])
    self.assertEqual(expected, result)

  def test_multiply_numbers_no_numbers(self):
    expected = 0
    result = math_stuff.multiply_numbers([])
    self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
