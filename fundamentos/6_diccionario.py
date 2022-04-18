persona = {
    'name': 'Miguel Angel',
    'last_name' : 'Herrera Vargas'
}
print(persona)

# Acceder al contenido de una key del diccionario
print("Acediendo a un elemento del diccionario")
print(persona['name'])
print(f"mi nombre es: {persona['name']}")

# Añadir una nueva propiedad al diccionario
print("Añadir una nueva propiedad al diccionario")
print(persona)
persona['city'] = 'Colombia'
print(persona)

# Eliminar una Propiedad
print("Eliminar una Propiedad")
del persona['last_name']
print(persona)

#Longitud del diccionario
print("Longitud del diccionario")
print(len(persona))