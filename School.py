from datetime import date
from datetime import time
from datetime import datetime
from operator import itemgetter


class School:

    def __init__(self, classes):
        if classes is None:
            self.classes = []
        else:
            self.classes = list(classes)

    def add_class(self, kls):
        self.classes.append(kls)

    def remove_class(self, kls):
        self.classes.remove(kls)

    def get_all_classes(self):
        print('Все классы школы:', self.classes)

    def get_class(self, index):
        return self.classes[index]

    def __len__(self):
        return len(self.classes)

    def __iter__(self):
        return iter(self.classes)


class StudentClass:

    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            self.students = []
        else:
            self.students = sorted(list(students))
        self.lessons = []

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def get_student(self, index):
        return self.students[index]

    def all_students(self):
        print(self.students)

    def has_student(self, student):
        return student in self.students

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def all_lessons(self):
        print('Уроки класса {}:'.format(self.name))
        for lesson in sorted(self.lessons, key=itemgetter(1)):
            print(lesson)

    def remove_lesson(self, day, subject):
        amount_of_lessons = len(self.lessons)
        for lesson in self.lessons:
            if day in lesson and subject in lesson:
                lesson[-2].lessons.remove(lesson)
                self.lessons.remove(lesson)
                print('Урок удален')
        if amount_of_lessons == len(self.lessons):
            print('Такого урока нет в расписании')


class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Teacher:

    def __init__(self, name):
        self.name = name
        self.lessons = []

    def all_lessons(self):
        print('Уроки учителя {}:'.format(self.name))
        for lesson in sorted(self.lessons, key=itemgetter(1)):
            print(lesson)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Subject:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Lesson:

    def __init__(self, kls, day, start, end, teacher, subject):
        self.kls = kls
        self.day = day
        self.start = start
        self.end = end
        self.teacher = teacher
        self.subject = subject
        self.lesson = (self.kls, datetime(year=self.day.year, month=self.day.month, day=self.day.day).strftime('%x'),
                       time(hour=self.start.hour, minute=self.start.minute).strftime('%H:%M %p'),
                       time(hour=self.end.hour, minute=self.end.minute).strftime('%H:%M %p'),
                       self.teacher, self.subject)

        kls.lessons.append(self.lesson)
        teacher.lessons.append(self.lesson)
        print('Урок добавлен в расписание учебного класса')

    def __iter__(self):
        return iter(self.lesson)

    def __str__(self):
        return '{}'.format(self.lesson)

    def __repr__(self):
        return '{}'.format(self.lesson)


school26 = School([])
class9B = StudentClass('9B')
student1 = Student('Alex')
teacher1 = Teacher('Mr. Johnson')
math = Subject('Mathematics')
les1 = Lesson(class9B, date(2020, 4, 28), time(8, 30), time(9, 15), teacher1, math)