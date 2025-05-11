from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name:str, email):

        if not name or not email:
            raise ValueError("Name and email must be filled")

        self.name = name.strip()
        self.email = email
    @abstractmethod  
    def get_function(self)->str:
        pass
    def __str__(self):
        return f"{self.get_function()}:{self.name}({self.email})"