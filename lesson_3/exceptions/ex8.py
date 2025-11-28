students = {'John': 25, 'Jane': 22, 'Doe': 30}

# This can simply be solved using the get method
# def get_age(name):
#    return students.get(name, 'Student not found')
# for study purposes though with exceptions it would look as so
def get_age(name):
    try:
        return students[name]
    except KeyError:
        return "Student not found"

print(get_age('John'))
print(get_age('Bob'))