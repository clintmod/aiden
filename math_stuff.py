#!/usr/bin/env python
import sys

def sum_numbers(numbers):
  result = 0
  i = 0
  while (i < len (numbers)):
    result = result + int(numbers[i])
    i = i + 1
  return result

def multiply_numbers(numbers):
  if len(numbers) == 0: return 0
  result = 1
  i = 0
  while (i < len (numbers)):
    result = result * int(numbers[i])
    i = i + 1
  return result


if __name__ == "__main__":
  del sys.argv[0]
  print sum_numbers(sys.argv)
