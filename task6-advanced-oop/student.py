from typing import List
from person import Person
class Student(Person):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.enrollments = []
    def get_function(self):
        return "student"
    def __iter__(self):
        for enrollment in self.enrollments:
            yield enrollment.course
    def __add__(self, other_course):
        sum_enrollments = self.enrollments + other_course.enrollment
        return[enrollment.course for enrollment in sum_enrollments]