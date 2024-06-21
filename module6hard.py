import math

class Figure:

    sides_count = 0

    def __init__(self, color, *sides):
        """
            self.__color - list
            self.__sides - list
            self.filled - bool
        """
        self.__color = color
        self.__sides = [1] * self.sides_count if len(sides) != self.sides_count else list(sides)
        self.filled = True
    
    def __is_valid_color(self, r, g, b):
        """ 
            Incapsulated method checks if values r,g,b is in range between 0 and 255
            r, g, b - int
        """
        r, g, b = abs(r), abs(g), abs(b)
        if (r+g+b) <= 255*3:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        """
            Change color of object instances
            r, g, b - int
        """
        r, g, b = abs(r), abs(g), abs(b)
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        
    def get_color(self):
        """
            Return tuple of colors
            __color - list
        """
        return self.__color

    def __is_valid_side(self, *sides):
    
        if len(sides) == self.sides_count:
            return True
        else:
            return False

    def set_sides(self, sides):

        if self.__is_valid_side(sides):
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count

    def get_sides(self):

        return self.__sides

    def __len__(self):
        if isinstance(self.get_sides(), int):
            return int(self.get_sides() *  self.sides_count)
        else:
            return int(self.get_sides() *  self.sides_count)

class Circle(Figure):
    sides_count = 1
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] // 2

    def get_square(self):
        return 3.14159 * self.__radius**2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__find_height(self.get_sides())
    
    def __find_height(self, *sides):
        a, b, c = self.get_sides()
        p = (a + b + c) // 2
        h = math.sqrt(p*(p-a)*(p-c)*(p-b))/c
        return h
    
    def get_square(self):
        S = (1/2) * self.get_sides()[0] * self.__height
        return S
    
class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color)
        if len(sides) != 1: 
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = [*sides] * self.sides_count

    def get_sides(self):
        return self.__sides
        
    def set_sides(self, *sides):
        if len(sides) != self.sides_count:
            return
        else:
            self.__sides = [*sides]

    def get_volume(self):
        return self.__sides[0]**3



