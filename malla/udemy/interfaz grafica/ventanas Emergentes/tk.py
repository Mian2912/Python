from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog
from turtle import title

root = Tk()
root.title("Ventanas Emergentes")

def test ():
    # MessageBox.showinfo("Hola!","Hola Mundo")
    # MessageBox.showwarning("Alerta","sesion solo para administradores")
    # MessageBox.showerror("Danger", "Ha ocurrido un error inespirado")
    # resultado = MessageBox.askquestion("Salir","Estas seguro que quieres salir sin guardar")
    # if resultado == "yes" :
    #     root.destroy()
    # resultado = MessageBox.askokcancel("Salir","Sobre Escribir el fichero actual")
    # if resultado :
    #     root.destroy()
    # resultado = MessageBox.askyesno("Salir","Sobre Escribir el fichero actual")
    # if resultado :
    #     root.destroy()

    # resultado = MessageBox.askretrycancel("Reintentar","No se puede conectar")
    # if resultado: 
    #     root.destroy() 

    # color = ColorChooser.askcolor(title="elige un color")
    # print(color)

    # fichero = FileDialog.askopenfile(title="Abrir un Fichero", initialdir="C:", filetypes=(("Fichero de texto", "*.txt"), ("Todos Los Ficheros","*.*")))
    ruta = FileDialog.asksaveasfile("Guardar un fichero")
    print(ruta)
    pass

Button(root, text="Clicame", command=test).pack()

root.mainloop()