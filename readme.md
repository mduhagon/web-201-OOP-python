# Classes & Objects:

## Instructions to run:
    - fork the repo and clone
    - run venv (virtual environment) and get pytest into it.
    - can run tests in the tests folder via terminal / visual studio code IDE
    - run the application from `python3 main_controller.py`

## Project School Student Grading System

#

    MODELS:
    - SchoolTeacher Class (Parent Class)
        name: String
        put_name()
        get_name()
        - Inherits:
        class TeacherPhysics
        class TeacherChemistry
    - Student 
        name: String
        age: Number
        class_number: Number
        grade: Dict[String: Character]| [subject:grade]
#
    VIEWS:
    - StudentDataStorage
        putStudent()
        putStudents([])
        getStudents()
        getStudentData()
        getStudentGrades()
    
#

    MAIN:
        - Enroll Students
        - Fetch Student Data
        - Enroll Teachers
        - Enlist Syllabus
        
        - class SchoolSubject
          - name
          - Syllabus: Dict[Number:String] | chapter_number:chapter_name
          - put_syllabus()
          - get_syllabus()
        - class PhysicsSubject / ChemistrySubject
            calculate_grade()
        - enlist_subjects()
        - view_subjects()
        - view_subject_syllabus(subject_name)
        
#

# TO-DOs:
    Task1:
        - 1.1 write tests for enroll_students()
        - 1.2 in student_collection fetch_all_student_data() (test)
        - 1.3 fetch_data_with_student_name() (test)
    Task2:
        - 2.1 make one more type of teacher
        - 2.2 collection for teachers and enroll teachers
        - 2.3 fetch data for all teachers (test)
        - 2.4 fetch data via teacher name (test)
  
    Task3: (advanced)
      - create classes and methods for Subjects

#

## keyboard shortcuts shortcut - cmd + k + s
    save all files at once - cmd + option + s
    

