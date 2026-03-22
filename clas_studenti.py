class Student:
    def __init__(self, name, age, grade, email):
        self.name = input('Introduceti numele studentului: ')
        self.age = int(input('Introduceti varsta studentului: '))
        self.grade = float(input('Introduceti media Studentului: '))
        self.email = input('Introduceti E-Mail-ul:')

    def display(self):
        print(f'Name: {self.name}, Age: {self.age}, Grade: {self.grade}, E-Mail: {self.email}')

class Catalog:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        for student in self.students:
            student.display()

    def search_catalog(self):
        index = students.index(name)

catalog = Catalog()
catalog.add_student(Student(name='', age=0, grade=10, email=''))
catalog.display_all()
