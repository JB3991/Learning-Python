#Dictionary 
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."}

#Retrieving an Item from the Dictionary 
print(programming_dictionary["Function"])

# Adding to the Dictionary 
programming_dictionary["Loop"] = "The action of doing something over and opver again"

print(programming_dictionary)

#Empty Dictionary 
empty_dictionary = {}

#editing an iotem in the dictionary 
programming_dictionary["Bug"] = "A month in your computer"

for item in programming_dictionary:
  #Prints the keys in the Dictionary 
  print(item)
  #Prints the values in the Dictionary 
  print(programming_dictionary[item])

#Dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#Empty Dic
student_grades = {}
#for Every key in Student score do the following 
for student in student_scores:
  # score = the values of student scores 
  score = student_scores[student]
  #If statement to assign score to a grade
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

# nesting lists 
travel_log = {
  "Frace": {"Cities_Visited": ["Paris", "Lille", "Dijon"], "total_Visits": 12},
  "Germany": ["Berlin", "Hamburg", "Stuttguard"],
}

#Adding a new Dic to an Array
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, times_visited, cities):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = times_visited
  new_country["cities"] = cities
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

