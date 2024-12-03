from abc import  ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Sqaure(Shape ):
    def __init__(self, side):
        self.__side = side
    def area(self):
        return self.__side * 4
class Rect(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def area(self):
      return self.__length * self.__width
    def perimeter(self):
        return (self.__length + self.__width) * 2