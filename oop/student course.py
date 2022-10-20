# Create class of student
class Student:
    def __init__(self, admno, name, course='python'):
        self.admno = admno
        self.name = name
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        self.feepaid += amount



s1 = Student(1, 'Mark', 'Java')
s1.payment(5000)
print(s1.getDue())
print(s1.getdue())

s2 = Student(2, "Jack")
print(s2.getdue())


