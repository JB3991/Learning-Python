print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2

lowercase_Names = names.lower()

t = lowercase_Names.count("t")
r = lowercase_Names.count("r")
u = lowercase_Names.count("u")
e = lowercase_Names.count("e")

true = t + r + u + e

l = lowercase_Names.count("l")
o = lowercase_Names.count("o")
v = lowercase_Names.count("v")
e = lowercase_Names.count("e")

love = l + o + v + e

lovescore = int(str(true) + str(love))

print(lovescore)

if lovescore < 10 or lovescore > 90:
  print(f"Your score is {lovescore}, you go together like coke and mentos.")
if lovescore > 40 and lovescore < 50:
  print(f"Your score is {lovescore}, you are alright together.")
else:
  print(f"Your score is {lovescore}, Your not a match")