from datetime import time
from operator import itemgetter
from prettytable import PrettyTable


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
        self.lesson = [self.kls, self.day,
                       time(hour=self.start.hour, minute=self.start.minute).strftime('%H:%M %p'),
                       time(hour=self.end.hour, minute=self.end.minute).strftime('%H:%M %p'),
                       self.teacher, self.subject]

    def __iter__(self):
        return iter(self.lesson)

    def __getitem__(self, item):
        return self.lesson[item]

    def __str__(self):
        return '{}'.format(self.lesson)

    def __repr__(self):
        return '{}'.format(self.lesson)


class Schedule:

    lessons = []

    @classmethod
    def add_lesson(cls, lesson):
        cls.lessons.append(lesson)
        print('Урок добавлен')

    @classmethod
    def __getitem__(cls, item):
        return cls.lessons[item]

    @classmethod
    def get_lesson(cls, kls=None, day=None, teacher=None):
        lst = [i for i in (kls, day, teacher) if i is not None]
        answer = []
        if len(lst) == 1:
            answer = [lesson for lesson in cls.lessons if lst[0] in lesson]
        elif len(lst) == 2:
            answer = [lesson for lesson in cls.lessons if lst[0] in lesson and lst[1] in lesson]
        elif len(lst) == 3:
            answer = [lesson for lesson in cls.lessons if lst[0] in lesson and lst[1] in lesson and lst[2] in lesson]
        for les in answer:
            print(les)

    @classmethod
    def get_all_lessons(cls):
        for lesson in sorted(cls.lessons, key=itemgetter(1)):
            print(lesson)

    @classmethod
    def get_all_lessons_pretty(cls):
        table = PrettyTable(['N', 'Class', 'Day', 'Start time', 'Finish time', 'Teacher', 'Subject'])
        x = 1
        for lesson in sorted(cls.lessons, key=itemgetter(1)):
            table.add_row([x, lesson[0], lesson[1], lesson[2], lesson[3], lesson[4], lesson[5]])
            x += 1
        print(table)


school26 = School([])
class9B = StudentClass('9B')
class7A = StudentClass('7A')
class5C = StudentClass('5C')
student1 = Student('Alex')
teacher1 = Teacher('Mr. Johnson')
teacher2 = Teacher('Mrs. Jane')
math = Subject('Mathematics')
geor = Subject('Geography')
physics = Subject('Physics')

les1 = Lesson(class9B, 1, time(8, 30), time(9, 15), teacher1, math)
les2 = Lesson(class9B, 3, time(9, 30), time(10, 15), teacher1, math)
les3 = Lesson(class9B, 5, time(19, 30), time(10, 15), teacher1, math)
les4 = Lesson(class7A, 1, time(10, 30), time(11, 15), teacher2, geor)
les5 = Lesson(class7A, 2, time(9, 45), time(10, 30), teacher2, geor)
les6 = Lesson(class7A, 4, time(12, 30), time(13, 15), teacher2, geor)
les7 = Lesson(class5C, 3, time(15, 30), time(16, 15), teacher1, physics)

Schedule.add_lesson(les1)
Schedule.add_lesson(les2)
Schedule.add_lesson(les3)
Schedule.add_lesson(les4)
Schedule.add_lesson(les5)
Schedule.add_lesson(les6)
Schedule.add_lesson(les7)

Schedule.get_all_lessons_pretty()