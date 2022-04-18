from cProfile import label
from tkinter import *

from click import edit

#configuracion de la raiz

root = Tk()

menuBar=Menu(root)
root.config(menu=menuBar)
filemenu= Menu(menuBar, tearoff=0)
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menuBar, tearoff=0)
editmenu.add_command(label="Copiar Ctrl + C")
editmenu.add_command(label="Cortar   Ctrl + C")
editmenu.add_command(label="Pegar  Ctrl + V")


helpmenu = Menu(menuBar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca De ....")

menuBar.add_cascade(label="Archivo", menu=filemenu)
menuBar.add_cascade(label="Editar", menu=editmenu)
menuBar.add_cascade(label="Ayuda", menu=helpmenu)




root.mainloop()