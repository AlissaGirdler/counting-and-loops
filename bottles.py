for i in range (100,2,-1):
    print (i, "bottles of beer on the wall")

    if i == 5:
        print(i, "bottles of beer")
        print("If one of those bottles should happen to fall", i-1, "bottles of beer on the wall...")
    else:
        print(i, "bottles of beer")
        print ("Take one down, pass it around", i-1, "bottles of beer on the wall...")

print("2 bottles of beer on the wall\n2 bottles of beer\nTake one down pass it around 1 bottle of beer on the wall")
print("1 bottle of beer on the wall\n1 bottle of beer\nTake one down, pass it around no more botttles beer on the wall")
print("No more bottles of beer on the wall, no more bottles of beer.")
print("We've taken them down and passed them around; now we're drunk and passed out!")
print(" ")