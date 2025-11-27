class Student:
    school_name = 'Oxford'

student = Student()
print(type(student).school_name)
print(student.__class__.school_name)
print(student.school_name)