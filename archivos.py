
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import *
import os

ventana = Tk()



def abrir_archivo():
    archivo_abierto = filedialog.askopenfilename(title = "Select file")
    
    archivo = open(archivo_abierto, "rb")

    guardar_archivo(archivo.read())

def guardar_archivo(dato):
    archivo_guardado = filedialog.asksaveasfilename(title = "Select file")
    
    archivo=open(archivo_guardado,"wb")
    archivo.write(dato)
    print(archivo_guardado)

def carpeta():
    directorio=filedialog.askdirectory()
    if directorio!="":
        os.chdir(directorio)
    print(os.getcwd())

Button(text="Abrir archivo",bg="pale green",command=abrir_archivo).place(x=10,y=10)
Button(text="Guardar archivo",bg="light blue",command=guardar_archivo).place(x=10,y=40)
Button(text="Directorio",bg="salmon",command=carpeta).place(x=10,y=70)

ventana.mainloop()