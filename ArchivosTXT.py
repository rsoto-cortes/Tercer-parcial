"""
manejo de archivos de texto
Apertura de archivos
    open("archivo.TXT","r")
    
Modos Principales

Modo    Descripcion
r       Leer
w       Escribir(sobrescribir)
a       Agregar
x       Crear Archivo

*****Lectura de archivos
    *archivo.read()
    *archivo.readline()
    *archivo.readlines()
    
*****Escritura de archivos
    archivo.write("Texto a escribir")
    archivo.writelines(["Linea1/n","Linea2/n"])
    
"""


"""def crear_archivo():
    nombre=input("Nombre del archivo: ")
    with open(nombre,"w") as archivo:
        print("Archivo creado correctamente")

crear_archivo()"""
        
"""def escribir_archivo():
    nombre=input("Nombre del archivo: ")
    texto=input("Escribe el texto a guardad:")
    
    with open (nombre,"w") as archivo:
        archivo.write(texto)
    
    
    print("Texto guardado correctamente")

escribir_archivo()"""


"""def agregar_texto():
    nombre=input("Nombre del archivo: ")
    texto=input("Texto a agregar: ")
    
    with open(nombre,"a") as archivo:
        archivo.write("\n"+texto)
        
        print("Texto agregado correctamente")
        
agregar_texto()
"""
"""import os
 
def leer_archivo():
    nombre=input("Nombre del archivo: ")
    
    try:
        with open (nombre,"r") as archivo:
            contenido=archivo.read()
            os.system("cls")
            print("\nContenido del archivo")
            print(contenido)
            print("------------------")
            archivo.seek(0)
            contenido=archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")
        
leer_archivo()

"""
import os
 
def leer_archivo():
    nombre=input("Nombre del archivo: ")
    
    try:
        with open (nombre,"r") as archivo:
            contenido=archivo.readlines()
            os.system("cls")
            print("\nContenido del archivo")
            print(contenido)
            
            for linea in contenido:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo no existe")
        
leer_archivo()


