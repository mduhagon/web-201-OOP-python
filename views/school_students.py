class SchoolStudents:
    enrolled_students = []

    def enroll_student(self, student):
        self.enrolled_students.append(student)
    def all_students(self):
        for each_student in self.enrolled_students:
            print("Name :" + each_student.name)
            