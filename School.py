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
        for kls in self.classes:
            print(kls)

    def get_class(self, index):
        return self.classes[index]

    def __len__(self):
        return len(self.classes)

    def __iter__(self):
        return iter(self.classes)


class StudentClass:

    def __init__(self, students=None):
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

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)

    def __str__(self):
        return 'Student Class: {}'.format(self.students)

    def set_up_lesson(self, subject, date, start, end):
        lesson = (subject, date, start, end)
        self.lessons.append(lesson)

    def remove_lesson(self, subject, date):
        amount_of_lessons = len(self.lessons)
        for lesson in self.lessons:
            if subject in lesson and date in lesson:
                self.lessons.remove(lesson)
                print('Урок удален')
        if amount_of_lessons == len(self.lessons):
            print('Такого урока нет в расписании')

    def all_lessons(self):
        print(self.lessons)


class Subject:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name