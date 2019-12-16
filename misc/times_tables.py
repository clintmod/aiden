#!/usr/bin/env python
import time
import random
import operator

LIMIT = 20

nums1 = [3,4,6,7,8,9,12]

right_answers = 0
wrong_answers = 0

def print_high_scores(entries):
  entries = set(entries)
  sorted_entries = sorted(entries, key=operator.itemgetter(1))
  print "\nHIGH SCORES"
  for entry in sorted_entries[:5]:
    print "{}\t{:.2f}".format(entry[0], entry[1]) 
  print "\n"

def prompt_yes_no(message):
  return raw_input("{} y/n: ".format(message))

def prompt(message):
  return raw_input("{}\n".format(message))

def show_high_scores():
  entries = []
  with open("times_tables_highscores.csv") as f:
    for line in f:
      entry = line.split(",")
      entries.append((entry[0], float(entry[1]))) 
  print_high_scores(entries)

def start_game():
  show_high_scores()
  answer_count = 1
  global right_answers
  global wrong_answers
  while answer_count <= LIMIT:
    print "answer count: {}, LIMIT: {}".format(answer_count, LIMIT) 
    i = random.choice(nums1)
    j = random.choice(nums1)
    answer = prompt("{} x {} = \n".format(i, j))
    try:
      answer = int(answer)
    except ValueError:
      print "That wasn't a number."
      next
    answer_count += 1
    if answer == i * j:
      print "You smart! You not dumb!"
      right_answers += 1
    else:
      print "You get wrong! You stupid! It was {}.".format(i*j)
      wrong_answers += 1


def end_game():
  print "\n"
  return True

def record_score(initials, time):
  with open('times_tables_highscores.csv', 'a') as highscores_file:
    highscores_file.write("{},{}\n".format(initials, time))

if __name__ == "__main__":
  try:
    total_start_time = time.time()
    start_game()
    total_end_time = time.time()
    total_diff_time = total_end_time - total_start_time
    print "Total time was: {:.2f}".format(total_diff_time)
    print "You got {} correct and {} wrong.".format(right_answers, wrong_answers)
    if right_answers == LIMIT:
      should_record = prompt_yes_no("Would you like to record your time?")
      if should_record == "y":
        initials = prompt("Enter your initials: ")
        record_score(initials, total_diff_time)
        show_high_scores()
      else:
        show_high_scores()
  except KeyboardInterrupt:
    end_game()
