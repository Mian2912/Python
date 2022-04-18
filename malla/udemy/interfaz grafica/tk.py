from cgitb import text
from dataclasses import field
from tkinter import *
from cProfile import label
from typing import TextIO

root = Tk()
root.title("Hola Mundo")
root.resizable(1, 1)
"""
# root.geometry("400x400")
#  variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")
# añadiendo el frame
frame = Frame(root, height=480, width=320)
frame.pack(fill="both", expand=1)

# creando un label
# label = Label(frame, text="Hola mundo")
# label.place(x=0, y=0)
Label(frame, text="Hola mundo").pack(anchor="nw")
label = Label(frame, text="¡Otra Etiqueta!")
Label(frame, text="¡Ultima etiqueta!").pack(anchor="se")

label.pack(anchor="center")
label.config(background="green", foreground="white")
label.config(font=("Verdana",24))
label.config(textvariable=texto)
imagen = PhotoImage(file="./descarga.gif")
Label(root, image=imagen, bd=0).pack(side="left")

nombre = Label(root, text="Nombre")
nombre.grid(row=0 ,column=0, sticky="w", padx=5,pady=2)
inputNombre = Entry(root)
inputNombre.grid(row=1, column=0, padx=5, pady=5)
inputNombre.config(justify="center", )

apellidos = Label(root, text="Apellidos")
apellidos.grid(row=2, column=0, sticky="w", padx=5)
inputApellidos = Entry(root)
inputApellidos.grid(row=3, column=0, padx=5, pady=5)
inputApellidos.config(justify="center", show="*")
"""

def sumar ():
    r.set(float(n1.get()) + float(n2.get()))

n1 = StringVar()
n2 = StringVar()
r = StringVar()


Entry(root, justify="center", textvariable=n1).pack()
Entry(root, justify="center", textvariable=n2).pack()
Entry(root, justify="center", textvariable=r, state="readonly").pack()

Button(root, text="sumar", border=0, background="red", foreground="white",command=sumar).pack()




root.mainloop()

