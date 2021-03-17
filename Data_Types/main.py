#Data Types
#print index of String
print("Hello"[0])

#Int - Whole Numbers 
print(123+456)

#float - Decimal points 
3.14159

#Boolean - True or Fale 

True
False

name = "john"

print(type(name))

name1 = "Katie"
name_len = len(name1)
name_num_char = str(name_len)
print("your name has " + name_num_char + " Characters")

#Shows the data type
a = 123
print(type(a))

# Setting b to data type String
b = str(123)
print(type(b))

#will print 200 as both numbers are Int/Floats 
print( 100 + float("100"))

# will print 100100 as we're adding 2 string togeather
print(str(100) + str(100))

# Taking a String "35" and converting these to Int, then adding the 2 digits togeather 
a = str(35)

b = int(a[0])
c = int(a[1])

d = b + c

print(d)

# Round the number to the nearest whole number 
print(round(9/2))
#Rounding to the 2nd decimal place
print(round(8/3,2))

result = 4 /2
result /= 2 
print(result)

score = 0
score += 1
print(score)

score1 = 100
lifes = 5 
winning = True

print(f"your score is {score1} and you have {lifes} lifes left. are you winning? {winning}! ")

print(6 + 4 / 2 - (1 * 2))