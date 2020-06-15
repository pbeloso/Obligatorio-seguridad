# -*- coding: utf-8 -*-
#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERIAS NECESARIAS.
from tkinter import *
import os

from Cifrados import hashPass, compararPass

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="darkslategray"

    ventana_principal=Tk()
    ventana_principal.geometry("300x250")
    ventana_principal.title("Login")

    Label(text="Elegir opcion:", bg="slategray", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()

    Button(text="Acceder", height="2", width="30", bg=pestas_color, command= lambda:[login(),ventana_principal.withdraw()]).pack() #boton "Acceder"
    Label(text="").pack()

    #lambda:[login(),ventana_principal.withdraw()]

    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command= lambda:[registro(),ventana_principal.withdraw()]).pack() #boton "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():

    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x280")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() # string como tipo de dato para nombre_usuario y la clave
    clave = StringVar() 
 
    Label(ventana_registro, text="Introdocir datos:", bg="slategray").pack()
    Label(ventana_registro, text="").pack()

    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario: ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) 
    entrada_nombre.pack()

    etiqueta_clave = Label(ventana_registro, text="Contraseña: ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()

    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="slategray", command = registro_usuario).pack() #boton "Registrarse"

    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Volver", width=10, height=1, command = lambda:[ventana_principal.deiconify(),ventana_registro.withdraw()]).pack()
    

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login

    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x280")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario:").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()

    Label(ventana_login, text="Contraseña:").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Volver", width=10, height=1, command = lambda:[ventana_principal.deiconify(),ventana_login.withdraw()]).pack()

#VENTANA VERIFICACION DE LOGIN.

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END)
    entrada_login_clave.delete(0, END) 
    listaUsuarios = open("Usuarios.txt", "r")

    fafa = verificar_usuario (usuario1)
    if fafa:
        for i in listaUsuarios:
            user = i.split(";")
            if ( user[0] == usuario1):
                resultado = compararPass(clave1, user[1].rstrip())  #.rstrip() elimina el salto de linea

                if resultado:
                    exito_login()
                else:
                    no_clave()
    else:
        no_usuario()

# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = hashPass(clave.get())
    
    if (verificar_usuario(usuario_info)==False):
        file = open("Usuarios.txt", "a") #agrego datos al archivos usuario
        file.write(usuario_info + ";" + str(clave_info) + "\n")
        file.close()
    
        entrada_nombre.delete(0, END)
        entrada_clave.delete(0, END)
    
        Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
    else:
        Label(ventana_registro, text="Nombre de usuario repetido", fg="red", font=("calibri", 11)).pack()
 
#VERIFICA SI HAY USUARIO EN ARCHIVO

def verificar_usuario(nombre):
    ListaUsuarios = open("Usuarios.txt", "r")
    for i in ListaUsuarios:
        user = i.split(";")
        if(user[0] == nombre):
            return True

    return False 

 
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.