from student import Student
from instructor import Instructor
class TeachingAssistant(Student, Instructor):
    def __init__(self, name, email):
        Student.__init__(self, name, email)
        Instructor.__init__(self, name, email)
    def get_function(self):
        return "Teaching Assistant"
    

        