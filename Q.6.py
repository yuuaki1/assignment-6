def student_data(student_id, student_name=None, student_class=None):
    # print the student id
    print(f'Student ID: {student_id}')
    # check if student name and class are provided
    if student_name and student_class:
        print(f'Student Name: {student_name}')
        print(f'Student Class: {student_class}')

# test the function
student_data(123)
student_data(123, student_name='John', student_class='10th')
