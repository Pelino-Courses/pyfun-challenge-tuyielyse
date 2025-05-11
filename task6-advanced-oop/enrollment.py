from student import Student
from course import Course
from typing import Optional

class Enrollment:
    def __init__(self, student:Student, course:Course, grade: Optional[float] = None):

        if not isinstance(student, Student):
            raise TypeError("student must be a student")
        self.student = student
        self.course = course 
        self.grade = grade
        student.enrollments.append(self)
        course.enrolledstudents.append(self)
    def __str__(self):
        grade_info =f"Grade: {self.grade}" if self.grade is not None else "No grade"
        return f"{self.student.name} enrolled in {self.course.code} ({grade_info})"
    