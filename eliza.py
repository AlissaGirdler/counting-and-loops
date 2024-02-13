import random
import sys

cards = [
  ("How many primary colors are there?", "3",),
  ("How many secondary colors are there?","3"),
  ("What are the three primary colors?",
     ["Blue",
      "Red",
      "Yellow"])
  ]

print("Welcome to your color theory flashcards!")
print("Type 'yes' to get started or 'quit' to exit at any time.")
start = input("\nAre you ready? ").lower()

i = 0

if "y" in start:
  while i in range (2,0):
    print(cards[i][0])
    user_answer = input("Your answer: ")

    if user_answer.lower() in cards[i][1]:
      print("Correct, on to the next flashcard!")

    elif while user_answer not in cards[i][1]:
      print("Incorrect.")
      user_answer = input("Try again: ")

    elif "quit" in user_answer:                      
      print("Goodbye!")
      sys.exit(0)

elif "quit" in start:                      
  print("Goodbye!")
  sys.exit(0)