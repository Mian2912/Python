# Menu del programa
import helpers

from click import option
import manager
def loop():
    while True:

        helpers.clear() # 'clear' para linux y OS X

        print("==========================")
        print("   BIENVENIDO AL GESTOR   ")
        print("==========================")
        print("[1] Listar Clientes       ")
        print("[2] Mostrar Clientes      ")
        print("[3] Añadir Cliente        ")
        print("[4] Modificar Cliente     ")
        print("[5] Borrar Cliente        ")
        print("[6]Salir                  ")
        print("=======================   ")
        option = input("> ")

        helpers.clear() # 'clear' para linux y OS X

        if option == '1':
            print("Listado los clientes...\n")
            manager.show_all()
        elif option == '2':
            print("Mostrando un cliente...\n")
            manager.find()
        elif option == '3':
            print('Añadiendo un cliente...\n')
            if manager.add() :
                print("Cliente Añadido Correctamente")
        elif option == '4':
            print("Modificando un cliente...\n")
            if manager.edit() :
                print("Cliente Actualizado Correctamente")
        elif option == '5':
            print("Borrar un cliente...\n")
            if manager.delete() :
                print("Cliente eliminado Correctamente")
        elif option == '6':
            print("Saliendo...\n")
            break
        else:
            print("Opcion incorrecta...")

        input("\nPresiona ENTER para continuar")    