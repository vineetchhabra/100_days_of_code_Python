# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

avg_height = 0

for i in student_heights:
    avg_height += i
print(avg_height)

number_of_students = 0

for i in student_heights:
    number_of_students += 1
print(number_of_students) 