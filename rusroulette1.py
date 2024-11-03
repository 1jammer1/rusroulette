#!/bin/python3
# stop judging me my code is not that bad
import subprocess
import os
import time
import random
import sys

define die():
  if dienum = 1:
    print("congrats you won you dont die")
    sys.exit(0)
  else:
    question_function()

def question_function():
    # Define a list of questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "What is the largest planet in our solar system?": "Jupiter",
        "Who painted the Mona Lisa?": "Leonardo da Vinci",
        "What is the chemical symbol for gold?": "Au",
        "What is the largest mammal on Earth?": "Blue whale"
    }

    # Select a random question
    question = random.choice(list(questions.keys()))

    # Print the question and start the timer
    print(question)
    start_time = time.time()

    # Get the user's answer
    answer = input("Enter your answer: ")

    # Check if the answer is correct and if the time limit has been exceeded
    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time > 10:
        print("Time's up! You took too long to answer.")
        return False
    elif answer.lower() == questions[question].lower():
        print("Correct! You answered in {:.2f} seconds.".format(elapsed_time))
        sys.exit(1)
    else:
        print("Incorrect. The correct answer is {}.".format(questions[question]))
            print("say goodbye")
            sys.exit(1)
  
  

# just check if they try to tamper with my things
subprocess.Popen(['python3', 'justchecking.py'])
# warn the user
print("oh whoopsie your now playing russian roulette with your pc dont try to exit or all of your files will be deleted Thanks!")
time.sleep(5)
# menu
os.system("clear")
print("Linux Russian Roulette Menu:")
print("1. all by yourself (loser)")
print("2. Play with friends (LAN)")
print("3. just kill me already")
hahaloser = input("what shall you do (num): ")
if hahaloser == "1"
  os.system("clear")
  print("you should get some friends") # insult the user
  time.sleep(0.5)
  os.system("clear")
  print("Randomizing") #give some illusion of working
  time.sleep(2)
  print("...")
  time.sleep(0.5)
  # okay time to actually do it
  dienum = random.randrange(1, 10)
  die()
elif hahaloser == "2":
  print("no server is not implemented you get let off")
  sys.exit(0)
elif hahaloser == "3":
  print("bye bye")
  sys.exit(1)
