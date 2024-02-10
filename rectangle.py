length = input("Enter the length of the rectangle: ")
width = input("Enter the width of the rectangle: ")

for _ in range(int(width)):  # Outer loop for rows
    for _ in range(int(length)):  # Inner loop for columns
        print("*", end="")
    print("")  # New line after each row