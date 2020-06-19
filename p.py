
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import *
import os

from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


ventana = Tk()


def cifrarArchivo():
    
    # buscar archivo a cifrar

    archivo_abierto = filedialog.askopenfilename(title = "Select file")
    nombre = os.path.splitext(os.path.basename(archivo_abierto))[0]
    extension = os.path.splitext(os.path.basename(archivo_abierto))[1]

    #lee archivo a cifrar

    data = open(archivo_abierto, "rb") 
    data = data.read()

    key = get_random_bytes(16) #genera key

    cipher = AES.new(key, AES.MODE_CBC)
    cifrado_bytes = cipher.encrypt(pad(data, AES.block_size))

    #elegir el lugar donde guardar

    directorio = filedialog.askdirectory() 
    
    #guardar iv ; clave ; extension en .enc

    ruta = directorio + "/secret" + nombre + ".enc"
    archivo_secret = open(ruta, "wb")
    archivo_secret.write(cipher.iv)
    archivo_secret.write(b";")
    archivo_secret.write(key)
    archivo_secret.write(b";")
    archivo_secret.write(bytes(extension,('utf-8')))


    archivo_secret.close()
    
    #guardar archivo .enc

    ruta = directorio + "/" + nombre + '.enc'
    archivo_cifrado = open(ruta,"wb")
    archivo_cifrado.write(cifrado_bytes)

    archivo_cifrado.close()



def descifrarArchivo():
    
    # buscar archivo a descifrar

    archivo_abierto = filedialog.askopenfilename(title = "Select file")
    nombre = os.path.splitext(os.path.basename(archivo_abierto))[0]
    
    archivo_cifrado = open(archivo_abierto, "rb")
    cifrado = archivo_cifrado.read()

    #archivo secret con iv ; key ; extension

    ruta = os.path.split(archivo_abierto)[0] + "/secret" + os.path.split(archivo_abierto)[1]
    archivo_secret = open(ruta, "rb")
    secret = archivo_secret.read()

    listaSecret = secret.split(b";")

    iv = listaSecret[0]
    key = listaSecret[1]
    extension = listaSecret[2]
    print(extension.decode('utf-8'))
    

    #descifro archivo_cifrado

    cipher = AES.new(key, AES.MODE_CBC, iv)
    descifrado = unpad(cipher.decrypt(cifrado), AES.block_size)
    
    #guardo archivo descifrado

    ruta_guardado = os.path.split(archivo_abierto)[0] + '/' + nombre + extension.decode('utf-8')
    print(ruta_guardado)
    archivo = open(ruta_guardado,"wb")
    archivo.write(descifrado)
    


  
Button(text="cifrar archivo",bg="pale green",command=cifrarArchivo).place(x=10,y=10)
Button(text="descifrar archivo",bg="pale green",command=descifrarArchivo).place(x=10,y=40)
ventana.mainloop()

#pt = descifradoCBC(key, iv, ct)
#print(pt.decode('utf-8'))