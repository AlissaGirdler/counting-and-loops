# Define flashcards with questions and answers

flashcards = {
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

# Function to display flashcards
def display_flashcard(flashcards):
    card = random.choice(list(flashcards.keys()))
    print("\nQuestion:", flashcards[card]["question"])
    input("Press Enter for the answer.")
    print("Answer:", flashcards[card]["answer"])

# Main program loop
while True:
    print("\nFlashcard Program")
    print("1. Display Flashcard")
    print("2. Quit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        display_flashcard(flashcards)
    elif choice == "2":
        print("Exiting the program. Adios!")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")