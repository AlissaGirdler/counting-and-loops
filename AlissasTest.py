import random
import sys

# Flashcard questions and answers
cards = {
    "Q1": {"question": "Name one of the three different types of color groups.", "answer": ["primary", "secondary", "tertiary"]},
    "Q2": {"question": "List one of the primary colors.", "answer": ["red", "yellow", "blue"]},
    "Q3": {"question": "List one of the secondary colors.", "answer": ["green", "orange", "purple"]},
    "Q4": {"question": "How do you make secondary colors?", "answer": ["combine","mix","two","secondar"]},
    "Q5": {"question": "Name the cool primary color.", "answer": "Blue"},
    "Q6": {"question": "Name the warm secondary color.", "answer": "orange"},
    "Q7": {"question": "What is another name for tertiary colors?", "answer": "Intermediate"},
    "Q8": {"question": "What is the relationship between colors on the opposite side of the color wheel?", "answer": "Complimentary"},
    "Q9": {"question": "Name one measurement of color properties.", "answer": ["Saturation", "value"]},
    "Q10": {"question": "What color contains all colors?", "answer": "White"}
}

# User launches
print("\nWelcome to your color theory flashcards!")
print("Type 'yes' to get started or 'quit' to exit at any time.")
start = input("Are you ready? ")

if start.lower() == "yes":
        rq = random.choice(list(cards.keys()))
        print("\nQuestion: ", cards[rq]["question"])
        user_answer = input("Your answer: ")

        while True:
            if (user_answer.lower() not cards[rq]["answer"]):
            print("Correct!")
            break
        elif ()
            print("Incorrect")
            user_answer = input("Try again: ")
else:
    print("Bye!")


else:
    print("Bye!")