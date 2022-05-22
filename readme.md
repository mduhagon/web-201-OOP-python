classes and objects:

1. School teacher - student Grading.

SchoolTeacher Class (Abstract Class)
    - name: String
    - put_name()
    - get_name()
- Inherits
    - TeacherPhysics
    - TeacherChemistry

SchoolSubject
    - Syllabus: Dict[Number:String] | chapter_number: Chapter:name
    - put_syllabus()
    - get_syllabus()
    - calculate_grade()
- Inherits
    - PhysicsSubject
    - ChemistrySubject

Student
    - name: String
    - age: Number
    - class_number: Number
    - grade: Dict[Subject: Character] or []

StudentDataStorage
    - putStudent()
    - putStudents([])
    - getStudents()
    - getStudentData()
    - getStudentGrades()


Main:
    - Enroll Teachers
    - Enroll Students
    - Fetch Student Data
    - Enlist Syllabus
    - View Subjetcs


keyboard shortcuts shortcut - cmd + k + s
    - save all files at once - cmd + option + s
    