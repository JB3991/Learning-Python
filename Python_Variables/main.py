# Write your code below this line 👇
# print on new lines 
print("line 1 \nline 2 \nline 3")
# print my name with a space
print("Hello" + " " + "John")
# a print statement with an input 
print ("Hello " + input("What is your Name?"))
# Prints length of name 
print( len(  input("What is your name? ")))
# let the input name to a variable 
name = input("What is your name? ")
print(name)
#switching the values of A & B to B & A
a = input("a:")
b = input("b:")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

#create a band name generator 
print("Welcome to the Band Name Generator.")
name = input("Where did you grow up?\n")
pet = input("Whats the name of your pet?\n")
print("The name of your band should be, " + name + " " + pet)