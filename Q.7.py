class Student:
    pass

class Marks:
    pass

# create instances of Student and Marks classes
student1 = Student()
marks1 = Marks()

# check if the instances are of the respective classes
print(isinstance(student1, Student)) # True
print(isinstance(marks1, Marks)) # True

# check if the classes are subclasses of the object class
print(issubclass(Student, object)) # True
print(issubclass(Marks, object)) # True
