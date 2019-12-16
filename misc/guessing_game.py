#!/usr/bin/env python
import os
import random
import operator
from time import sleep
from subprocess import Popen

last_say = None

upper_bound = 1000
lower_bound = 1

def say(message, wait_time=0):
  global last_say
  if last_say is not None:
    last_say.terminate()
  last_say = Popen(["say", message])
  sleep(wait_time)
  return True

def say_and_print(message, wait_time=0):
  print(message)
  say(message, wait_time)


def prompt_yes_no(message):
  say(message, 0)
  return raw_input("%s y/n: " % message)

def prompt(message):
  say(message, 0)
  return raw_input("%s\n" % message)

def start_game():
  show_high_scores()
  prompt_to_play()

def show_high_scores():
  entries = []
  with open("highscores.txt") as f:
    for line in f:
      entry = line.split(",")
      entries.append((entry[0], int(entry[1]))) 
  print_high_scores(entries)

def print_high_scores(entries):
  entries = set(entries)
  sorted_entries = sorted(entries, key=operator.itemgetter(1))
  print "\nHIGH SCORES"
  for entry in sorted_entries[:5]:
    print "%s\t%i" % (entry[0], entry[1]) 
  print ""

def prompt_to_play():
  should_play = prompt_yes_no("Would you like to play a game?")
  if should_play == "y":
    play_game()
  else:
    end_game()

def play_game():
  say_and_print("Game on", 1)
  guesses = 0
  answer = random.randint(1,1000)
  guess_number(answer, guesses)
  
def guess_number(answer, guesses):
  global lower_bound
  global upper_bound
  guess = prompt("Guess a number between %i and %i" % (lower_bound, upper_bound))
  if guess == '':
    guess_number(answer, guesses)
  guess = int(guess)
  guesses += 1
  if guess < answer:
    lower_bound = guess
    say_and_print("Too low sucker!", 2)
    guess_number(answer, guesses)
  elif guess > answer:
    upper_bound = guess
    say_and_print("Too high you crazy!", 2)
    guess_number(answer, guesses)
  else:

    say_and_print ("You are the big wiener!!!!!!!!!!", 2)
    say_and_print ("It took you %i guesses" % guesses, 2)
    should_record = prompt_yes_no("Would you like to record your score?")
    if should_record == "y":
      initials = prompt("Enter your initials: ")
      record_score(initials, guesses)
      show_high_scores()
    else:
      show_high_scores()
      end_game()

def record_score(initials, guesses):
  with open('highscores.txt', 'a') as highscores_file:
    highscores_file.write("%s,%i\n" % (initials, guesses))

def end_game():
  print ""
  return True

if __name__ == "__main__":
  try:
    start_game()
  except KeyboardInterrupt:
    end_game()
