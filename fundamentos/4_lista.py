from tkinter import INSERT


mi_lista = ["Pyhon", "Django", "React", "Angular"]

# imprimir lista
print(mi_lista)

# Acceder a un elemento de la lista
print("Acceder a un elemento de la lista")
print(mi_lista[0]) #Python
print(mi_lista[3]) #Angular

# Acceder al ultimo elemento de la lista
print("Accediendo al ultimo elemento de la lista")
# cuando ingreso numero negativo comienza en -1
print(mi_lista[-1])
print(mi_lista[-4]) # Python

# Modificar un elemento de la lista
print(mi_lista)
mi_lista[1] = "Java"
print(mi_lista)

# añadiendo un nuevo elemento a la lista
print("añadiendo un nuevo elemento a la lista")
mi_lista.append("Vue")
print(mi_lista)

#añadir un elemento al comienzo de la lista
mi_lista.insert(0,'C#')

mi_lista.insert(2, "Flutter")
print(mi_lista)

# Longitud
print(len(mi_lista))


l =[1,'Python']
print(l)