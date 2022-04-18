from cProfile import label
from pydoc import plain
import sqlite3
from struct import pack
from tkinter import *

#creamos la raiz
root = Tk()
root.title("Bar Don Costa - Menu")
root.resizable(0,0)
root.config(bd=15, relief="sunken", background="lightgray")

Label(root, text="   Bar Don Costa   ", foreground="darkgreen", background="lightgray", font=("Times New Roman",28, "bold italic")).pack()
Label(root, text="Menu del dia", foreground="green", background="lightgray", font=("Times New Roma",24,"bold italic")).pack()

#separacion de titilos y categorias
Label(root, text="", background="lightgray").pack()

# Conectarnos a la base de datos
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorias y platos de la db
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1], background="lightgray", foreground="blue", font=("Times New Roman",20,"bold italic")).pack()
    
    platos = cursor.execute("SELECT * FROM plato where categoria_id={}".format(categoria[0]))
    for plato in platos:
        Label(root,text=plato[1], background="lightgray", foreground="red", font=("Times New Roman",16,"bold italic")).pack()
    
    Label(root, text="", background="lightgray").pack()

#cerramos la conexion a la base de datos
conexion.close()

#precio del menu
Label(root, text="12 euros (IVA incl.)", fg="darkgreen", font=("Times New Roman", 18, "bold italic"), background="lightgray").pack(side="right")




# Finalmente ejecutamos el bucle
root.mainloop()