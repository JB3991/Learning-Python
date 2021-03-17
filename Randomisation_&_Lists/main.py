import random
import my_module

random_int = random.randint(1, 10)
print(random_int)

print(my_module.pi)
# Random number between 0 - 5
random_float = random.random() * 5
print(random_float)

List of States
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])
print(states_of_america[-5])

#Change the value at index 
states_of_america[1] = "Deleware"

#adding to the end of the list
states_of_america.extend(["Test1, Test2, Test3"])

print(states_of_america)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#Total of number of itesm in list
random_name = len(names)
#random number from 0 to random name length
random_num = random.randint(0, random_name -1)

person_to_pay = names[random_num]

print(person_to_pay + " Will pay the bill today")

# OR 

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " Will pay the bill today")

List of fruit & Veg
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruit = [dirty_dozen[0], dirty_dozen[4], dirty_dozen[5], dirty_dozen[6], dirty_dozen[7], dirty_dozen[8]]
print(fruit)

vegetables = [dirty_dozen[1], dirty_dozen[2],dirty_dozen[9], dirty_dozen[10], dirty_dozen[11]]
print(vegetables)

fruit_and_veg = [fruit, vegetables]
print(fruit_and_veg)
print(fruit_and_veg[1][1])





