from enum import auto
from turtle import color

class Automovil: 
    # Atributos de la clase Automovil
    marca = ""
    color = "blanco"

    def __init__(self, marca, color):
            self.marca = marca
            self.color = color

# creando una instacia de la clase Automovil
auto1 = Automovil("hyundai", "rojo")
print(auto1.marca)
print(auto1.color)
print(f"Marca: {auto1.marca}, Color: {auto1.color}") 
