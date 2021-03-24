
from login import *
import os
def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def menu():
    print("Menu")
    print("1. Login")
    print("2. Crear usuario")
    print("3. Listar usuario")
    print("4. Salir")

ejecucion = True
usuarios = []
while ejecucion:
    print("Bienvienido a Simple Login")
    menu()
    seleccion = input("Digite una opcion: ")

    if seleccion=="1":
        login()
    elif seleccion=="2":
        usuario = create_user()
        usuarios.append(usuario)
    elif seleccion=="3":
        imprimirUsuarios(usuarios)
    elif seleccion=="4":
        ejecucion = False
    else:
        borrarPantalla()
        menu()
    salir = input("Para salir presione Q o presione otra tecla para continuar: ")
    if salir == "Q":
        ejecucion = False
    borrarPantalla()


