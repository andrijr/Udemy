from Tetragon import *

kwadrat = Square(5)
prostokat = Rectangle(10,16)

lista = [kwadrat, prostokat]

for figura in lista:
    print("pole figury wynosi:", figura.area())
    print("obwód figury wynosi:", figura.perimeter())

for figura in lista:
    print(figura.area())
    print(figura.perimeter())
