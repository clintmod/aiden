#!/usr/bin/env python
import random
import sys

def guess_number(answer, guesses, lower, upper, autorun):
  diff = upper - lower
  suggested_number = (diff / 2) + lower
  message = "Guess a number between %i and %i (e.g %i): " % (lower, upper, suggested_number)
  if not autorun:
    guess = input(message)
  else:
    print(message)
    guess = suggested_number
  if guess == '':
    guess = suggested_number
  guess = int(guess)
  guesses += 1
  if guess < answer:
    lower = guess
    print("Too low sucker!")
    guess_number(answer, guesses, lower, upper, autorun)
  elif guess > answer:
    upper = guess
    print("Too high you crazy!")
    guess_number(answer, guesses, lower, upper, autorun)
  else:
    print ("You are the big wiener!!!!!!!!!!")
    message = "It took you %i guesses" % guesses
    if guesses == 1:
        message = "It took you %i guess!" % guesses
    print (message)

def main():
    autorun = False
    if sys.argv[1] == "--autorun":
        autorun = True
    if not autorun:
        result =   input("Do you want to play with me? muahahahaha: (y/n): ")
    else:
        result = 'y'
    if result == 'y':
        print("game on muthafucka")
        guesses = 0
        answer = random.randint(1,1000)
        guess_number(answer, guesses, 1, 1000, autorun)
    else:
        print("you suck ballz!!")

if __name__ == "__main__":
    main()