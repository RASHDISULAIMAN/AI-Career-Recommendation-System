number_of_courses = int(input("Enter number of courses: "))
total = 0

for i in range(number_of_courses):
    grade = float(input(f"Enter grade for course {i + 1}: "))
    total += grade

average = total / number_of_courses

if average >= 85:
    career = "Engineering Specialist"
else:
    career = "Technical Support or Diploma Path"

print("Recommended Career Path:", career)
