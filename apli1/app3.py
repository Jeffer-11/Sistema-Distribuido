# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

# # Crear una instancia de la clase
# persona1 = Persona("Jefferson", 30)

# # Usar un método de la clase
# print(persona1.saludar())

# def computeAreasquereal(side):
#     return side * side

# def computeAreaCircle(radius):
#     return 3.14 * radius * radius

# print( f"Area of square with side 5: {computeAreasquereal(3)}")
# print(f"Area of circle with radius 5:, {computeAreaCircle(3): 2f}") 


class Geometry:
    pi = 3.1415
    def __init__(self, side, radius):
        self.side = side
        self.radius = radius
    print("The obejct was created successfully")
    def area(self):
        squareArea = self.side * self.side
        circleArea = Geometry.pi * self.radius**2
        return squareArea, circleArea
        



areaSquareCIrcle=Geometry(3,3)
result=list()
result=areaSquareCIrcle.area()
print(f"Area of square with side 3: {result[0]}, {result[1]:.2f}")


# Create a rectangle class with attributes width and height and a method area() that returns the area
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 5)
print(f"Area of rectangle with width 4 and height 5: {rectangle.area()}")
nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

class Promedio:   
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

promedio_obj = Promedio(nota1, nota2, nota3)
prome = promedio_obj.calcular_promedio()

if prome == 10: 
    print(f"El estudiante tiene el mejor promedio: {prome:.2f}")
elif prome >= 7:
    print(f"El estudiante aprueba: {prome:.2f}")
else:
    print(f"El estudiante reprueba: {prome:.2f}")
