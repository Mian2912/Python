# Las tuplas son inmutables
mi_tupla = ("Python", "Django", "React", "Vue")
print(mi_tupla)

# acceder a un elemeto
print("acceder a un elemeto")
print(mi_tupla[0]) #El primer elemento
print(mi_tupla[-1]) #El ultimo elemento

# Intentemos modificar un elemento de la mi_tupla
print("Intentemos modificar un elemento de la mi_tupla")
mi_tupla[2] = 'Angular'
print(mi_tupla) 