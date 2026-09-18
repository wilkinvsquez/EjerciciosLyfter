from Rectangle import Rectangle

def start():
    height = float(input("Inserte la altura del rectangulo: "))
    width = float(input("Inserte el ancho del rectangulo: "))
    try:
        rectangle = Rectangle(width, height)
        print(rectangle.get_area())
        print(rectangle.get_perimeter())
    except ValueError as error:
        print(error)
