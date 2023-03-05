class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


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
            self.lecture_grades[course][student] = grade
        else:
            self.lecture_grades[course] = {student: grade}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)

lecturer = Lecturer('Mega', 'Lecturer')
lecturer.courses_attached += ['Python']
print(lecturer.courses_attached)
error = lecturer.rate_lecture(best_student, 'Python', 10)
if error:
    print(error)
else:
    print(lecturer.lecture_grades)
