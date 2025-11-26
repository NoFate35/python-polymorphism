import sys
sys.path.append('/home/ivan/python-polymorphism/dynamic_dispatching')
import figure as Figure
import circle as Circle
import square as Square


def test_solution():
    Circle.init()
    Square.init()

    circle = Circle.make(5)
    square = Square.make(5)
    circle_area = Figure.get_area(circle)
    square_area = Figure.get_area(square)

    assert round(circle_area) == 79
    assert square_area == 25
