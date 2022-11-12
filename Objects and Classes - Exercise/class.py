class Class:
    __students_count = 22
    students = []
    grades = []

    def __init__(self, name_of_the_class):
        self.name_of_the_class = name_of_the_class


    def add_student(self, name: str, grade: float):
        if len(Class.students) < Class.__students_count and len(Class.grades) < Class.__students_count:
            Class.students.append(name)
            Class.grades.append(grade)

    def get_average_grade(self):
        average = sum(Class.grades) / len(Class.students)
        return f'{average:.2f}'

    def __repr__(self):
        return f"The students in {self.name_of_the_class}: {', '.join(Class.students)}.\nAverage grade: {self.get_average_grade()}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
