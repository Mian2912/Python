from enum import auto


class Automovil:
    marca = ""
    color = ""
    encendido = False
    velocidad = 0

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def encender (self) :
        self.encendido = True

    def set_velocidad(self, velocidad) :
        self.velocidad = velocidad

auto = Automovil("hyundai", "Rojo")
# auto2 = Automovil('Ford', 'Negro')

auto.encender()
auto.set_velocidad(60)

if auto.encendido :
    print(f"el automovil esta encendio y va a una velocidad de {auto.velocidad} Km/h")
else:
    print("El auto esta Apagado")