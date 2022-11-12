pair_of_rows = int(input())
grades = {}

for i in range(pair_of_rows):
    students_name = input()
    grade = float(input())
    if students_name not in grades:
        grades[students_name] = []
    grades[students_name].append(grade)

filtered_grades = {}
for name, grade in grades.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        filtered_grades[name] = average_grade
sorted_grades = sorted(filtered_grades.items(), key=lambda kvpt: - kvpt[1])
for name, grade in sorted_grades:
    print(f"{name} -> {grade:.2f}")
