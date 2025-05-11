import math
class Shape:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("shape name must be a none-empty string.")
        self.name = name.strip()

    def Area(self):
        raise NotImplementedError("subclasses must implement the area()method")
    
    def __str__(self):
        return f"{self.name}"
    
class Circle(Shape):
    def __init__(self, radius:float):
        if radius <= 0:
            raise ValueError("Radius must be a positive numbers.")
        super().__init__("Circle")
        self.radius = radius 

    def Area(self):
        return math.pi*self.radius**2
    def __str__(self):
        return f"{self.name} with radius {self.radius}"
    
    @classmethod
    def R_from_diameter(cls, diameter:float):
        if diameter <= 0:
            raise ValueError("Diameter must be positive")
        return cls(diameter/2)
    
class Rectangle(Shape):
    def __init__(self, width : float,height:float):
        if width <= 0 or height <= 0:
            raise ValueError("height and width must be positivenumbers.")
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    def Area(self):
        return self.width*self.height
    def __str__(self):
        return f"{self.name} with width {self.width} and the height {self.height}"
class Triangle(Shape):
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        super().__init__("Triangle")

        self.base = base
        self.height = height
    def Area(self):
        return (1/2)*self.base*self.height
    def __str__(self):
        return f"{self.name} with base {self.base}and the height {self.height}"

# Usage Example
if __name__ == "__main__":
    shapes = [Circle(30), Circle.R_from_diameter(50), Rectangle(23, 67), Triangle(45, 89)]
    for shape in shapes:
        print(str(shape))
        print(f"Area : {shape.Area():.2f} m^2")
        

    
    