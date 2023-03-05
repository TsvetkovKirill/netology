class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def avg_grade(self):
        count = 0
        sum = 0
        for course_grades in self.grades.values():
            for grade in course_grades:
                count += 1
                sum += grade
        return sum / count

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.avg_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def rate_lecture(self, student, course, grade):
        if course not in self.courses_attached:
            return 'Преподаватель не преподает данный курс'
        if course in self.lecture_grades:
            self.lecture_grades[course] += [grade]
        else:
            self.lecture_grades[course] = [grade]
        if course in student.grades:
            student.grades[course] += [grade]
        else:
            student.grades[course] = [grade]

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade()}"

    def avg_grade(self):
        count = 0
        grade_sum = 0
        for course_grades in self.lecture_grades.values():
            for grade in course_grades:
                count += 1
                grade_sum += grade
        return grade_sum / count

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def calculate_avg_students_grade(course, students):
    sum = 0
    count = 0
    for student in students:
        for grade in student.grades[course]:
            count += 1
            sum += grade
    return sum / count

def calculate_avg_lecturers_grade(course, lecturers):
    sum = 0
    count = 0
    for lecturer in lecturers:
        for grade in lecturer.grades[course]:
            count += 1
            sum += grade
    return sum / count

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', "ООП"]
best_student.finished_courses += ['Введение']

worst_student = Student('Worst', 'Student', 'your_gender')
worst_student.courses_in_progress += ['Python', "ООП"]
worst_student.finished_courses += ['Введение']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 7)

cool_reviewer.rate_hw(worst_student, 'Python', 1)
cool_reviewer.rate_hw(worst_student, 'Python', 2)


lecturer = Lecturer('Mega', 'Lecturer')
lecturer.courses_attached += ['Python']
print(lecturer.courses_attached)
error = lecturer.rate_lecture(best_student, 'Python', 10)
if error:
    print(error)
else:
    print(lecturer.lecture_grades)
print('------------')
print(cool_reviewer)
print()
print(lecturer)
print()
print(best_student)

print('best_student > worst_student = ', best_student > worst_student)
