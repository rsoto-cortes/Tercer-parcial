import tkinter as tk
from tkinter import messagebox
    
def cargar_diccionario():
    palabras_traducidas={}
    try:
        with open("traductor.txt","r") as f:
            for linea in f:
                esp,ing=linea.strip().split(",")
                palabras_traducidas[esp.lower()]=ing.lower()
    except:
        pass
    return palabras_traducidas
    

def agregar_palabra():
    español=entrada_es.get()
    ingles=entrada_in.get()
    nueva_tr={"trad_español":español,"trad_ingl":ingles}
    try:
        with open("traductor.txt","a") as archivo:
            palabras_traducidas.append(nueva_tr)
            archivo.write("\n"+palabras_traducidas)
        messagebox.showinfo("Exito","Se agrero con exito")
    except:
        messagebox.showerror("Error","No se pudo agregar la traduccion")


def traducir():
    palabra=entrada_palabra.get()
    opcion=num.get()
    
    if opcion == 1:
        try:
            with open("traductor.txt","r") as archivo:
                contenido=archivo.read()
                
            if palabra in contenido:
                label_traduccion.config()
        except:
            messagebox.showerror("Error","La palabra ha sido agregada")


ventana=tk.Tk()
ventana.title("Traductor")
ventana.geometry("300x500")

entrada_palabra=tk.Entry(ventana,width=30)
entrada_palabra.place(x=60,y=50)

num=tk.IntVar()
rbtn_es=tk.Radiobutton(ventana,text="Español-Ingles",variable=num,value=1)
rbtn_es.place(x=100,y=85)

rbtn_in=tk.Radiobutton(ventana,text="Ingles-Español",variable=num,value=2)
rbtn_in.place(x=100,y=120)

btn_traducir=tk.Button(ventana,text="Traducir",command=traducir)
btn_traducir.place(x=120,y=155)

label_traduccion=tk.Label(ventana,text="traduccion")
label_traduccion.place(x=120,y=210)

label_agregar=tk.Label(ventana,text="Agregar Palabra")
label_agregar.place(x=100,y=250)

label_esp=tk.Label(ventana,text="Español")
label_esp.place(x=40,y=290)

entrada_es=tk.Entry(ventana,width=20)
entrada_es.place(x=100,y=290)

label_ing=tk.Label(ventana,text="Ingles")
label_ing.place(x=40,y=330)

entrada_in=tk.Entry(ventana,width=20)
entrada_in.place(x=100,y=330)

btn_agregar=tk.Button(ventana,text="Agregar",command=agregar_palabra)
btn_agregar.place(x=120,y=370)
            

ventana.mainloop()