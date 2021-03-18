# Functions

def greet():
  print("hello")
  print("How are you today?")
  print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
  print(f"Hello {name}")

greet_with_name("John")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"Hows the weather in {location}")

greet_with("John", "London")

#Doesn't matter what was round the keyword Arguments are in the parameters 
greet_with(location="London", name="Jonathan")

Wall painting calculator

import math

def paint_calc(height, width, cover):
  area = height * width
  number_of_cans = math.ceil(area / cover)
  print(f"You'll need {number_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

PRIME NUMBER CHECKER 

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)

