# define student class


class Student(object):
    """
        Above is a class called student which has information from a student in order to create
        an object that includes student ID, the student's first name, the last name, and an email address.

    """

# create instance of Student

info = Student()

# assign values

info.id = '0289829 '
info.first = 'Ryan '
info.last = 'Hanks '
info.email = 'rhanks@mchenry.edu'

# print student information

print( info.id + info.first + info.last + info.email)
