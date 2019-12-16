#!/usr/bin/env python

def join_strings(strings):
  result = ""
  i = 0
  while (i < len(strings)):
    result = result + strings[i] + " "
    i = i + 1
  result = result[:-1]
  return result


