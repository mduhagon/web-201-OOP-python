from models.student import Student
from views.school_students import SchoolStudents

student = Student(name="Jyotsna", age=29, class_number=3)
SchoolStudents().enroll_student(student)
SchoolStudents().all_students()
