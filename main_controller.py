from models.student import Student
from models import physics_teacher
from views.school_students import SchoolStudents

student = Student(name="Jyotsna", age=29, class_number=3)
SchoolStudents().enroll_student(student)
SchoolStudents().all_students()

physics_teacher_1 = physics_teacher.PhysicsTeacher(name="Mia", lab_number="101")

print("Teacher details:")
print("name:"+physics_teacher_1.name, "lab number:" + physics_teacher_1.get_lab_number())