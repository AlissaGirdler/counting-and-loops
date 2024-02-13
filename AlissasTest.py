import random
import sys
# Flashcard questions and answers
cards = {
    "Q1": {"question": "Name the three different types of colors.", "answer": "Primary, secondary, and tertiary."},
    "Q2": {"question": "List the primary colors.", "answer": "Red, yellow, and blue."},
    "Q3": {"question": "List the secondary colors.", "answer": "Green, orange, and purple."},
    "Q4": {"question": "How do you make secondary colors?", "answer": "Combine two primary colors."},
    "Q5": {"question": "Name the cool primary color.", "answer": "Blue"},
    "Q6": {"question": "Name the warm secondary color.", "answer": "Orange"},
    "Q7": {"question": "What is another name for tertiary colors?", "answer": "Intermediate"},
    "Q8": {"question": "What is the relationship between colors on the opposite side of the color wheel?", "answer": "Complimentary"},
    "Q9": {"question": "Name one measurement of color properties.", "answer": "Saturation" or "value"},
    "Q10": {"question": "What color contains all colors?", "answer": "White"}
}

# User launches
print("\nWelcome to your color theory flashcards!")
print("Type 'yes' to get started or 'quit' to exit at any time.")
start = input("Are you ready? ")

if start.lower() == "yes":
    while True:
        rq = random.choice(list(cards.keys()))
        print("\nQuestion: ", cards[rq]["question"])
        user_answer = input("Your answer: ")

        if user_answer.lower() == random_card[4].lower():
            print("Correct!")
            break
        else:
            print("Incorrect")
            user_answer = input("Try again: ")
else:
    print("Bye!")