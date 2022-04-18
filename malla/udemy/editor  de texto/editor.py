from tkinter import *
from tkinter import filedialog
from io import open
# variable global
ruta = "" #la utilzaremos para almacenar la ruta del fichero

#funciones para el menu
# funcion de nuevo
def nuevo() :
    global ruta
    mensaje.set("Nuevo Fichero")
    ruta=""
    texto.delete(1.0, "end")
    root.title("Mi Editor")

def abrir() :
    global ruta
    mensaje.set("Abrir Fichero")
    ruta = filedialog.askopenfilename(initialdir=".", filetype=(("Fichero de Texto","*.txt"),), title="Abrir un fichero fe texto")
        
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " -  Mi Editor")


def guardar() :
    mensaje.set("Guardar Fichero")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else :
        guardarComo()

def guardarComo() :
    global ruta
    mensaje.set("Guardar Como Fichero")
    fichero = filedialog.asksaveasfile(title="Guardar Fichero", mode="w", defaultextension=".txt")
    if fichero is not None :
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado Cancelado")
        ruta = ""

# Configuramos la raiz
root = Tk()
# titulo de la ventana
root.title("Mi Editor")

# creando menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
# creando las diferentes opciones 
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar Como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

#añadiendo las obsiones al menu
menubar.add_cascade(menu=filemenu, label="archivo")

#Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12),background="lightgrey") #estilos del editor

# monitor inferior
mensaje= StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

# mostrando el menu 
root.config(menu=menubar)

# finalmente bucle de la aplicacion
root.mainloop()
