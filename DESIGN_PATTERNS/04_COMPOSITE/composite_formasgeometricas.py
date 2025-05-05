from abc import ABC, abstractmethod
# Component
class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        pass
# Leaf
class Circle(Shape):
    def draw(self) -> None:
        print("Drawing a Circle")
class Rectangle(Shape):
    def draw(self) -> None:
        print("Drawing a Rectangle")
# Composite
class ShapeGroup(Shape):
    def __init__(self) -> None:
        self._shapes = []

    def add(self, shape: Shape) -> None:
        self._shapes.append(shape)

    def remove(self, shape: Shape) -> None:
        self._shapes.remove(shape)

    def draw(self) -> None:
        print("Drawing a Shape Group")
        for shape in self._shapes:
            shape.draw()
# Client code
if __name__ == "__main__":
    circle1 = Circle()
    rectangle1 = Rectangle()

    group1 = ShapeGroup()
    group1.add(circle1)
    group1.add(rectangle1)
    circle2 = Circle()
    group2 = ShapeGroup()
    group2.add(circle2)
    group2.add(group1)
    group2.draw()
