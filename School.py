from datetime import time
from operator import indexOf
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
                       time(hour=self.start.hour, minute=self.start.minute).strftime('%H:%M'),
                       time(hour=self.end.hour, minute=self.end.minute).strftime('%H:%M'),
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

    @classmethod
    def __getitem__(cls, item):
        return cls.lessons[item]

    @staticmethod
    def fnd(*args, item):
        return all(arg in item for arg in args)

    @classmethod
    def get_lesson(cls, *args):
        result = []
        for lesson in cls.lessons:
            if cls.fnd(*args, item=lesson):
                result.append(lesson)
        return result

    @staticmethod
    def coordinates(lst, dt):
        tm = ('08:30', '09:30', '10:30', '11:30', '12:30')
        x, y = None, None
        for i in tm:
            if i == lst[2]:
                y = indexOf(tm, i)
        x = lst[1]
        dt[y][x] += '({}, {}, {})'.format(lst[0], lst[4], lst[5])

    @classmethod
    def get_all_lessons_pretty(cls):
        data = [[''] * 6 for i in range(1, len(cls.lessons))]
        for lesson in cls.lessons:
            cls.coordinates(lesson, data)
        data[0][0] = '08:30 - 09:15'
        data[1][0] = '09:30 - 10:15'
        data[2][0] = '10:30 - 11:15'
        data[3][0] = '11:30 - 12:15'
        data[4][0] = '12:30 - 13:15'
        table = PrettyTable(['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        for idx in range(len(data)):
            table.add_row(data[idx])
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
les2 = Lesson(class9B, 4, time(9, 30), time(10, 15), teacher1, math)
les3 = Lesson(class9B, 5, time(9, 30), time(10, 15), teacher1, math)
les4 = Lesson(class7A, 1, time(10, 30), time(11, 15), teacher2, geor)
les5 = Lesson(class7A, 2, time(11, 30), time(12, 15), teacher2, geor)
les6 = Lesson(class7A, 4, time(12, 30), time(13, 15), teacher2, geor)
les7 = Lesson(class5C, 3, time(9, 30), time(10, 15), teacher1, physics)

Schedule.add_lesson(les1)
Schedule.add_lesson(les2)
Schedule.add_lesson(les3)
Schedule.add_lesson(les4)
Schedule.add_lesson(les5)
Schedule.add_lesson(les6)
Schedule.add_lesson(les7)
Schedule.get_all_lessons_pretty()