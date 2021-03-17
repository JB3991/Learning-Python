#loops

# fruits = ["Apple", "Pear", "Orange"]
# for fruit in fruits:
#   print(fruit)
#   print(fruit + " Pie")

#Add's all the numbers from O to 100 togeather 
# total = 0 

# for number in range(0, 101):
#   total += number

# print(total)

#number goes up in 2's from 0 to 21
# for number in range(0, 22, 2):
#   print(number)

# add all the even numbers from 2 to 100
# total1 = 0 
# for number in range(0, 101, 2):
#   total1 += number

# print(total1)

# for number in range(0, 50): 
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Buzz")
#   elif number % 5 == 0:
#     print("Fizz")
#   else: 
#     print(number)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)

for sym in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for nums in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
  password += char

print(password)