from usuario import *
def login():
    user = input("Usuario:")
    password = input("Password:")

    print("usuario:",user)
    print("password:",password)

def create_user():
    nombre_completo = input("Nombre Completo:")
    email = input("Email:")
    usuario = input("Usuario:")
    password = input("Password:")
    confirm_password = input("Confirmar Password:")

    usuario = Usuario(nombre_completo,email,usuario,password)
    return usuario

def imprimirUsuarios(usuarios):
        for usuario in usuarios:
            print(usuario.email)