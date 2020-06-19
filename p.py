
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import *
import os

import Crypto
from Crypto.PublicKey import RSA
from base64 import b64encode, b64decode
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii
import bcrypt


ventana = Tk()


def cifrarArchivo():
    
    # buscar archivo a cifrar

    archivo_abierto = filedialog.askopenfilename(title = "Select file")
    nombre = os.path.splitext(os.path.basename(archivo_abierto))[0]
    extension = os.path.splitext(os.path.basename(archivo_abierto))[1]

    #lee archivo a cifrar

    data = open(archivo_abierto, "rb") 
    data = data.read()

    #cifro data

    key = get_random_bytes(16) #genera key
    cipher = AES.new(key, AES.MODE_CBC)
    cifrado_bytes = cipher.encrypt(pad(data, AES.block_size))

    #elegir el lugar donde guardar

    directorio = filedialog.askdirectory() 
    
    #guardar iv ; clave ; extension en .enc


    ruta = directorio + "/secret" + nombre + ".enc"
    archivo_secret = open(ruta, "wb")

    datos = cipher.iv + b";" + key + b";" + bytes(extension,('utf-8'))

    archivo_secret.write(datos)
    archivo_secret.close()
    
    #guardar archivo .enc

    ruta = directorio + "/" + nombre + '.enc'
    archivo_cifrado = open(ruta,"wb")
    archivo_cifrado.write(cifrado_bytes)

    archivo_cifrado.close()


def enviaCifrado():
    #buscar archivo secret a enviar

    archivo_secret = filedialog.askopenfilename(title = "Selecciona secret")
    secret = open (archivo_secret, 'rb')
   

    #busca clave publica para hacer rsa

    archivo_clave = filedialog.askopenfilename(title = "Selecciona la clave")
    clave_publica = open(archivo_clave, 'rb')
    

    #rsa

    encryptSecret = encryptRSA(secret.read(), clave_publica.read())

    secret.close()
    clave_publica.close()

    #guardar en archivo secret

    secret = open(archivo_secret, 'wb')
    secret.write(encryptSecret)
    secret.close()


def descifrarArchivo():
    
    #busca clave privada para hacer rsa

    archivo_clave = filedialog.askopenfilename(title = "Selecciona la clave")
    clave_privada = open(archivo_clave, 'rb')

    # buscar archivo a descifrar

    archivo_abierto = filedialog.askopenfilename(title = "Select file")
    nombre = os.path.splitext(os.path.basename(archivo_abierto))[0]
    
    archivo_cifrado = open(archivo_abierto, "rb")
    cifrado = archivo_cifrado.read()

    #archivo secret con iv ; key ; extension

    ruta = os.path.split(archivo_abierto)[0] + "/secret" + os.path.split(archivo_abierto)[1]
    archivo_secret = open(ruta, "rb")
    secret = archivo_secret.read()

    #descifro archivo secret

    secret = decryptRSA(secret, clave_privada.read())
    print(secret)

    #separo iv ; key ; extension

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
    

    
def encryptRSA(datos, publicKey):
    publicKey = RSA.import_key(publicKey) #creo objeto rsa public key
    encryptor = PKCS1_OAEP.new(publicKey)
    encrypted = encryptor.encrypt(datos)
    return encrypted

def decryptRSA(encrypted, privateKey):
    privateKey = RSA.import_key(privateKey) #creo objeto rsa private key
    decryptor = PKCS1_OAEP.new(privateKey)
    decrypted = decryptor.decrypt(encrypted)
    return decrypted


  
Button(text="cifrar archivo",bg="pale green",command=cifrarArchivo).place(x=10,y=10)
Button(text="enviar archivo",bg="pale green",command=enviaCifrado).place(x=10,y=40)
Button(text="descifrar archivo",bg="pale green",command=descifrarArchivo).place(x=10,y=70)
ventana.mainloop()

#pt = descifradoCBC(key, iv, ct)
#print(pt.decode('utf-8'))