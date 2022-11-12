command = input()
courses = {}
while True:
    if command == 'end':
        break
    course_name, student_name = command.split(' : ')
    if course_name not in courses:
        courses[course_name] = 0
    courses[course_name] += 1
    if student_name in courses:
        courses[student_name] = course_name
    print(f"{course_name}: {student_name}")
    print(f"-- {student_name}")
    command = input()

for course_name, student_name in courses.items():
    print(f"{course_name}: {student_name}")
    # print(f"-- {student_name}")
