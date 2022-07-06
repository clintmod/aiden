#!/usr/bin/env python
from unittest import mock
import unittest
import guessing_game

class TestGuessingGame(unittest.TestCase):

  @mock.patch('guessing_game.print')
  def test_end_game_works(self, mock_print):
    result = guessing_game.end_game()
    self.assertTrue(result)
    mock_print.assert_called()
  
  @mock.patch('guessing_game.sleep')
  @mock.patch('guessing_game.Popen')
  def test_say_works(self,  mock_popen, mock_sleep):
    result = guessing_game.say("hi", 2)
    mock_popen.assert_called_with(["say","hi"])
    mock_sleep.assert_called_with(2)
    self.assertTrue(guessing_game.last_say is not None)
    self.assertTrue(result)


  @mock.patch('guessing_game.last_say.terminate')
  @mock.patch('guessing_game.last_say')
  @mock.patch('guessing_game.sleep')
  @mock.patch('guessing_game.Popen')
  def test_say_calls_terminate(self,  mock_popen, mock_sleep, mock_last_say, mock_terminate):
    result = guessing_game.say("hi", 2)
    mock_terminate.assert_called()
    mock_popen.assert_called_with(["say","hi"])
    mock_sleep.assert_called_with(2)
    self.assertTrue(guessing_game.last_say is not None)
    self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
