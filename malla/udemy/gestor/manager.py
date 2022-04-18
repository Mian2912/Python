from http import client
import re
import helpers
# Administrador de clientes
clientes = []

# añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Perez', 'dni':'15J'}
clientes.append(marta)

# no hace falta crear la variable
clientes.append({'nombre':'Manolo', 'apellido':'Lopez', 'dni':'48H'})
clientes.append({'nombre':'Ana', 'apellido':'Garcia', 'dni':'28Z'})

def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")

def show_all():
    for client in clientes:
        show(client)

def find():
    dni = input("Introduce el DNI del cliente\n>")

    for i,client in  enumerate (clientes):
        if client['dni'] == dni:
            show(client)
            return i, client

    print("No se ha encontrado ningun cliente con ese DNI")

def is_valid(dni):
    """
    >>> is_valid('48H')  # No valido, en uso
    False

    >>> is_valid('X82')  # No valido, incorrecto   
    False

    >>> is_valid('21A')  # Valido
    True 
    """


    # Comprueba que el dni empieza con un patron
    if not re.match('[0-9]{2}[A-Z]', dni):
        return False
    
    # Comprueba que ele dni no este repetido
    for client in clientes:
        if client['dni'] == dni:
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

def add():
    cliente = dict()

    print("Introduce nombre (De 2 a 30 Caracteres)")
    cliente['nombre'] = helpers.input_text(2,30)

    print("Introduce apellido (De 2 a 30 Caracteres)")
    cliente['apellido'] = helpers.input_text(2,30)

    while True:
        print("Introduce DNI (2 Numeros y 1 caracter en mayuscula)")
        dni = helpers.input_text(3,3)
        if is_valid(dni):
            cliente['dni'] = dni
            break
        print("DNI Incorrecto 0 en uso")

    clientes.append(cliente)
    return clientes

def edit():
    i, client = find()
    if client : 
        print(f"Introduc nuevo nombre ({client['nombre']})")
        clientes[i]['nombre'] = helpers.input_text(2,30)

        print(f"Introduce nuevo apellido ({client['apellido']})")
        clientes[i]['apellido'] = helpers.input_text(2,30)

        return True
    
    return False

def delete():

    i, client = find()
    if client:
            client = clientes.pop(i)
            show(client)
            return True
    return False