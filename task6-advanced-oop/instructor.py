from person import Person
class Instructor(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.courses_teaching = []
    def get_function(self):
            return "instructor"