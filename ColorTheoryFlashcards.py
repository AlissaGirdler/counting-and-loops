import random

# Flashcard questions and answers
cards = {
    "Q1": {"question": "What is the base color group called.", "answer": "primary"},
    "Q2": {"question": "Name a primary color that has three letters.", "answer": "red"},
    "Q3": {"question": "What color do you get when mixing red and yellow", "answer": "orange"},
    "Q4": {"question": "How do you make secondary colors?", "answer": "mix two secondary"},
    "Q5": {"question": "Name the cool primary color.", "answer": "blue"},
    "Q6": {"question": "Name the warm secondary color.", "answer": "orange"},
    "Q7": {"question": "What is another name for tertiary colors?", "answer": "intermediate"},
    "Q8": {"question": "What is the relationship between colors on the opposite side of the color wheel?", "answer": "complimentary"},
    "Q9": {"question": "What color contains all colors?", "answer": "white"}
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
        if (user_answer.lower() in cards[rq]["answer"]):
            print("Correct, on to the next question!")
            break 
        
        elif ()
                print("Incorrect")
                user_answer = input("Try again: ")

else:
    print("Bye!")