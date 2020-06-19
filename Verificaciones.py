#VERIFICA SI HAY USUARIO EN ARCHIVO

def verificar_usuario(nombre):
    if(len(nombre) == 0):              # no cumple
            return True

    ListaUsuarios = open("Usuarios.txt", "r")
    for i in ListaUsuarios:
        user = i.split(";")
        if (user[0] == nombre):     # ya existe
            return True

    return False
            
#VERIFICA QUE LA CLAVE SEA VALIDA

def verificar_clave(passw):

    if len(passw) < 8:
        return False

    numeros = 0
    mayusculas = 0
    minusculas = 0

    for carac in passw:
        if carac.isspace():
            return False
        elif carac.isdigit():
            numeros += 1
        elif carac.isupper():
            mayusculas += 1
        elif carac.islower():
            minusculas += 1

    return numeros != 0 and mayusculas !=0 and minusculas != 0