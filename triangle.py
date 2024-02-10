size = input("Enter the size of the triangle: ")

for i in range(1, int(size) + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for columns
        print("*", end="")
    print("")  # New line after each row 