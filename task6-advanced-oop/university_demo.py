from student import Student
from instructor import Instructor
from  teaching_assistant import TeachingAssistant
from course import Course
from enrollment import Enrollment

Elyse = Student("Elyse", "elyse@gmail.com")
Ernest = Student("Ernest", "ernest@gmail.com")
Olivier = Instructor("Professor Olivier", "olivier@gmail.com")
Sam = TeachingAssistant("Samuel", "sam@gmail.com")

python = Course("PYT1206", "Python", 10)
Web_design = Course("WEB1207", "Web Design", 15)

Enrollment( Elyse, python)
Enrollment(Ernest, python)
Enrollment(Elyse, Web_design)
Enrollment(Sam, Web_design)

Olivier.courses_teaching.append(python)
Sam.courses_teaching.append(Web_design)

for student in[Elyse, Ernest, Sam]:
    for enrollment in student.enrollments:
        print(enrollment)