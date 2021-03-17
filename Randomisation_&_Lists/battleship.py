import random
#List of emojis 
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
# Putting the lists into one list 
map = [row1, row2, row3]
# users input
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# users first number 
horzi = int(position[0])
# users second Number
vert = int(position[1])

# assign the users first number to a column
selected_row = map[vert - 1]
#assign the users second number to a row and replace the emoji with an X
selected_row[horzi - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")