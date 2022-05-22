classes and objects:

## Instructions to run:
    - fork the repo and clone
    - run venv (virtual environment) and get pytest into it.
    - can run tests in the tests folder via terminal / visual studio code IDE
    - run the application from `python3 main_controller.py`

## Project School teacher - student Grading.

<h2>SchoolTeacher Class (Parent Class)</h2>
    <ol>
        <li>name: String</li>
        <li>put_name()</li>
        <li>get_name()</li>
    </ol>
    - Inherits
    <ol>
        <li>TeacherPhysics</li>
        <li>TeacherChemistry</li>
    </ol>

<h2>Student</h2>
    <ul> 
        <li>name: String</li>
        <li>age: Number</li>
        <li>class_number: Number</li>
        <li>grade: Dict[Subject: Character] or []</li>
    </ul>
    
<h2>StudentDataStorage</h2>
    <ul>
        <li>putStudent()</li>
        <li>putStudents([])</li>
        <li>getStudents()</li>
        <li>getStudentData()</li>
        <li>getStudentGrades()</li>
    </ul>
    


<h2>Main:</h2>
    <ol>
        <li>Enroll Students</li>
        <li>Fetch Student Data</li>
        <li>Enroll Teachers</li>
        <li>Enlist Syllabus</li>
        <ol>
        - class SchoolSubject
            <li>Syllabus: Dict[Number:String] | chapter_number: Chapter:name</li>
            <li>put_syllabus()</li>
            <li>get_syllabus()</li>
        </ol>
        <ol>
        - class PhysicsSubject / ChemistrySubject
            <li>calculate_grade()</li>
        </ol>
        <ol>
        - Inherits
            <li>PhysicsSubject</li>
            <li>ChemistrySubject</li>
            <li>View Subjetcs</li>
        </ol>
    </ol>
    


keyboard shortcuts shortcut - cmd + k + s</br>
save all files at once - cmd + option + s
    

Task1:</br>
    - write tests for enroll_students()</br>
    - in student_collection fetch_all_student_data() (test)</br>
    - fetch_data_with_student_name() (test)</br>
Task2:</br>
    - make one more type of teacher</br>
    - enroll teachers</br>
    - fetch data for all teachers (test)</br>
    - fetch data via teacher name (test)</br>
Task3: (advanced)</br>
    - create classes and methods for Subjects</br>