def mid_rate(person):
    if isinstance(person, Lecturer) or isinstance(person, Student):
        summs = 0
        num = 0
        for i in person.grades:
            summs += sum(person.grades[i])
            num += len(person.grades[i])
            if num != 0:
                return summs / num
            else:
                return 0

def get_avarage(list_of_persons):
    if isinstance(list_of_persons, list):
        mid = 0
        num = 0
        if isinstance(list_of_persons[0], Student) or isinstance(list_of_persons[0], Lecturer):
            for i in list_of_persons:
                mid += mid_rate(i)
                num += 1
                if num != 0:
                     return mid / num
                else:
                    return 0

def get_list_students():
    return Student.all_students

def get_list_lectors():
    return Lecturer.all_lectors

class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.all_students.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, rate):
        if not isinstance(lector, Lecturer):
            print("Не является лектором!")
        else:
            if course in lector.courses_attached:
                try:
                    lector.grades[course].append(rate)
                except BaseException:
                    lector.grades[course] = [rate]
            else:
                print(f"{lector.name} {lector.surname} не ведет курс {course}")

    def dcourses_in_progress(self):
        res = ""
        for i in self.courses_in_progress:
            res += i + ", "
        res = res[0:len(res) - 2]
        return res

    def dfinished_courses(self):
        res = ""
        for i in self.finished_courses:
            res += i + ", "
        res = res[0:len(res) - 2]
        return res

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {mid_rate(self)}\n\
Курсы в процессе изучения: {self.dcourses_in_progress()}\nЗавершенные курсы: {self.dfinished_courses()}"

    def __lt__(self, students):
        return mid_rate(self) < mid_rate(students)

    def __le__(self, students):
        return mid_rate(self) <= mid_rate(students)

    def __eq__(self, students):
        return mid_rate(self) == mid_rate(students)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lectors = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.all_lectors.append(self)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {mid_rate(self)}"

    def __lt__(self, reviewer):
        return mid_rate(self) < mid_rate(reviewer)

    def __le__(self, reviewer):
        return mid_rate(self) <= mid_rate(reviewer)

    def __eq__(self, reviewer):
        return mid_rate(self) == mid_rate(reviewer)


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

# Прверочный блок
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

the_best_student = Student('Jhon', 'Dou', 'your_gender')
the_best_student.courses_in_progress += ['Python']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Jein', 'Dou')
cooler_lecturer = Lecturer('Oliver', 'Stone')

cool_lecturer.courses_attached += ['Python']
cooler_lecturer.courses_attached += ['Python']


best_student.rate_lector(cool_lecturer, 'Python', 8)
best_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(cool_lecturer, 'Python', 10)

best_student.rate_lector(cooler_lecturer, 'Python', 6)
best_student.rate_lector(cooler_lecturer, 'Python', 5)
best_student.rate_lector(cooler_lecturer, 'Python', 7)
best_student.rate_lector(cooler_lecturer, 'Python', 8)


cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(the_best_student, 'Python', 8)
cool_reviewer.rate_hw(the_best_student, 'Python', 8)
cool_reviewer.rate_hw(the_best_student, 'Python', 88)


print(mid_rate(the_best_student))
print(get_avarage(get_list_students()))
print(get_avarage(get_list_lectors()))
print(the_best_student.dfinished_courses())
print(the_best_student.dcourses_in_progress())
print(the_best_student)
print(the_best_student > best_student)
print(the_best_student >= best_student)
print(the_best_student == best_student)
print(cooler_lecturer)
print(cool_lecturer < cooler_lecturer)
print(cool_lecturer >= cooler_lecturer)
print(cool_lecturer == cooler_lecturer)
