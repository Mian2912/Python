class Automovil :
    marca = ""
    color = ""
    __encendido = False  #__hacemos private esta propiedad
    velocidad = 0

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def set_encendido (self) :
        self.__encendido = True

    def velocidad(self, velocidad):
        self.velocidad = velocidad

    def get_encendido(self):
        return self.__encendido