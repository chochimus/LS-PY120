class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

student = Student('Jim')
student2 = Student('Joe')

print(student.name)
print(student.__class__.school_name)
print(student.school_name)
print()
print(student2.name)
print(student2.__class__.school_name)
print(student2.school_name)