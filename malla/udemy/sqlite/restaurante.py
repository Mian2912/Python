from cgi import print_directory
from pickletools import OpcodeInfo
from select import select
import sqlite3
from unicodedata import category

from django.db import IntegrityError

# funcion para crear la base de datos
def crear_bd():
    #creamos la conexion a la base de datos
    conexion = sqlite3.connect('restaurante.bd')
    cursor = conexion.cursor()
    try :
        cursor.execute('''
            CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL
            )
        ''')
    except sqlite3.OperationalError:    
        print("la tabla de Categoria ya existe")
    else: 
        print("La tabla de Categoria se ha creado correctamente")

    try:
        cursor.execute('''
            CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL,
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id)
            )
        ''')
    except sqlite3.OperationalError:    
        print("la tabla de Plato ya existe")
    else: 
        print("La tabla de Plato se ha creado correctamente")

    conexion.commit()
    # cerramos la conexion a la base de datos
    conexion.close()

# funcion para agregar categoria
def agregar_categoria():
    conexion = sqlite3.connect('restaurante.bd')
    cursor = conexion.cursor()
    try:
        categoria = input("¿Nombre de la nueva categoria: \n")
        cursor.execute("INSERT INTO categoria(nombre) VALUES('{}')".format(categoria))
    except sqlite3.IntegrityError:
        print(f"La categoria '{categoria}' ya existe.")
    else:
        print(f"La categoria '{categoria}' creada correctamente")
    conexion.commit()
    # cerramos la conexion a la base de datos
    conexion.close()
  
# funcion para agregar plato
def agregar_plato():
    conexion = sqlite3.connect('restaurante.bd')
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("selecciona una categoria para añadir el plato: ")
    for categoria in categorias :
        print(f"[{categoria[0]}] {categoria[1]}")

    categoria_usuario = int(input("> "))
    
    plato = input("Nombre Del nuevo Plato?\n> ")

    try:
        cursor.execute("INSERT INTO plato (nombre, categoria_id) VALUES('{}','{}')".format(plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print(f"El plato '{plato}' ya existe")
    else:
        print(f"Plato '{plato}' creado correctamente")
    conexion.commit()
    # cerramos la conexion a la base de datos
    conexion.close()

# funcion para mostra el menu
def mostrar_menu():
    conexion = sqlite3.connect('restaurante.bd')
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t {}".format(plato[1]))

    conexion.close()

#crear la base de datos
crear_bd()

# menu de opciones del programa
while True:
    print("Bienvenido al gestor del restaurante! \n     [1] Agregar Una Categoria \n     [2] Agregar un plato\n     [3]Mostrar menu\n     [4] Salir")
    opcion = input("Introduce una opcion: ")

    if opcion == "1" :
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("Gracias Por Utilizar nuestros Servicios")
        break
    else: 
        print("Opcion Incorrecta")
