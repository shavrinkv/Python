class Person:
    def __init__(self, first_name: str, last_name: str, age: int, sex: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def forgot(self, info):
        self.knowledge.pop(0)


class Data:
    def __init__(self, info):
        self.info = list(info)

    def __getitem__(self, i):
            return self.info[i]



lesson = Data(['Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers'])
alexIvanych = Teacher()
vasy = Pupil()
pety = Pupil()
ilya = Pupil()
anna = Pupil()
alexIvanych.teach(lesson[0], [vasy, pety])
alexIvanych.teach(lesson[1], [ilya, anna])
alexIvanych.teach(lesson[2], [anna, pety])
alexIvanych.teach(lesson[3], [vasy, ilya, anna])
alexIvanych.teach(lesson[4], [pety])
print(vasy.knowledge)
print(pety.knowledge)
print(ilya.knowledge)
print(anna.knowledge)