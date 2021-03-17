# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("What is your age?"))
#   if age < 12:
#     print("please pay £5")
#   elif age <= 18:
#     print("Please pay £8")
#   elif age < 22:
#     print("Please pay £10")
#   else:
#     print("Please pay £12")
# else:
#     print("Sorry, your not tall enough to ride the rollercoaster")

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0 :
#   print("This number is even")
# else: 
#   print("This number is odd")

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / (height * height),2)

# if bmi <= 18:
#   print(f"Your BMI is {bmi}, you are underweight")
# elif bmi <= 22:
#   print(f"Your BMI is {bmi}, you have a normal weight")
# elif bmi <= 28:
#   print(f"Your BMI is {bmi}, you are slighty overweight")
# elif bmi <= 33:
#   print(f"Your BMI is {bmi}, you are obese")
# else: 
#   print(f"Your BMI is {bmi}, you need help")
  

# year = int(input("What is the year?"))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("This is a leap year ")
#     else:
#       print("This is Not a leap year")
#   else: 
#     print("This is a Leap Year")
# else:
#   print("This is NOT a leap year")
  
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are £5")
#   elif age <= 18:
#     bill = 8
#     print("Youth Tickets are £8")
#   else:
#     bill = 12
#     print("Adult tickets are £12")
  
#   wants_photo = input("Do you want a photo? Y or N. ")
#   if wants_photo == "Y": 
#     bill += 3
#   print(f"Your final bill is {bill}")

# else:
#     print("Sorry, your not tall enough to ride the rollercoaster")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# elif size == "L":
#     bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2 
#   else: 
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your total bill is £{bill}")

# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride the rollercoaster")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are £5")
#   elif age <= 18:
#     bill = 8
#     print("Youth Tickets are £8")
#   elif age >= 45 and age <= 55:
#     bill = 0
#     print("Tickets are free for mid life crisis")
#   else:
#     bill = 12
#     print("Adult tickets are £12")
  
#   wants_photo = input("Do you want a photo? Y or N. ")
#   if wants_photo == "Y": 
#     bill += 3
#   print(f"Your final bill is {bill}")

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# names = name1 + name2

# lowercase_Names = names.lower()

# t = lowercase_Names.count("t")
# r = lowercase_Names.count("r")
# u = lowercase_Names.count("u")
# e = lowercase_Names.count("e")

# true = t + r + u + e

# l = lowercase_Names.count("l")
# o = lowercase_Names.count("o")
# v = lowercase_Names.count("v")
# e = lowercase_Names.count("e")

# love = l + o + v + e

# lovescore = int(str(true) + str(love))

# print(lovescore)

# if lovescore < 10 or lovescore > 90:
#   print(f"Your score is {lovescore}, you go together like coke and mentos.")
# if lovescore > 40 and lovescore < 50:
#   print(f"Your score is {lovescore}, you are alright together.")
# else:
#   print(f"Your score is {lovescore}, Your not a match")

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 

# choice1 = input('You find yourself on the beach. Where do you want to go? Type "Forrst" or "Cave" \n').lower()
# if choice1 == "forrest":
#   choice2 = input('Now that your in the forrest, you have come to a fork! Type "Left" or "Right". \n').lower()
#   if choice2 == "right":
#     choice3 = input('You followed the right path which has lead you to the tempele of teasure! You now have 2 option. To enter through the front door or via the roof! Type "Door" or "Roof" \n').lower()
#     if choice3 == "roof":
#       print("You climb to the top of tempele, where you absaile down to find the hidden Treasure! YOU WIN!")
#     else: 
#       print("You took front door which was booby trapped. GAME OVER! ")
#   else:
#     print("You took the left turning which took you to the hidden tribe, who hold you hostage. GAME OVER!")


# else:
#   print("You fell into the cave and was trapped forever. GAME OVER!")