from typing import List, Iterator
from student import Student
class Course:
    def __init__(self, code : str, name : str, credits : int):
        if credits <= 0:
            raise ValueError("Credits must be positive integer")
        self.code = code
        self.name = name
        self.credits = credits
        self.enrolledstudents: List[Student] = []
    def enroll_student(self, student):
        self.enrolledstudents.append(student)
    def get_student(self):
        return self.enrolledstudents
    @classmethod
    def lab_course(cls, code:str, name:str) -> "course":
        return cls(code, "{name}(lab)",1)
    def __str__(self):
        return f"{self.code}: {self.name}{self.credits} credits"