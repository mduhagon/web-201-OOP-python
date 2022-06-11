class Student:

    def __init__(self, name, age, class_number):
        self.name = name
        self.age = age
        self.class_number = class_number
        self.grade = {}

    def calculate_dob(self, current_year):
        return current_year - self.age

