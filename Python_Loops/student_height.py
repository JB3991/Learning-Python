# Student Height

#student_heights = input("Input a list of student heights ").split()

student_heights = [180, 162, 171, 201, 153, 155, 181]

total_height = 0
number_of_students = 0

for height in student_heights:
  total_height += height
  number_of_students += 1

print(total_height)
print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)