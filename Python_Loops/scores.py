# High-Scores

# student_scores = input("Input a list of student scores ").split()
student_scores = [15, 50, 84, 20, 74, 66]

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

print(student_scores)

high_score = 0
#set high score to the heigh score within the array
for score in student_scores:
  if score > high_score:
    high_score = score

print(f"The high score is: {high_score}")