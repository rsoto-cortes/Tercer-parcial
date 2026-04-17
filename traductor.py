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

def guardar_palabra(esp,ing):
    with open("traductor.txt","a") as f:
        f.write(f"{esp},{ing}\n")

def agregar():
    esp= entrada_es.get().lower()
    ing=entrada_in.get().lower()
    
    if esp == "" or ing == "":
        messagebox.showerror("Error","Campos vacios")
        return
    
    guardar_palabra(esp,ing)
    messagebox.showinfo("Exito","Palabra agregada")
   
def traducir():
    palabra = entrada_palabra.get().strip(",").lower()
    dic = cargar_diccionario()
    
    if num.get() == 1:
        resultado = dic.get(palabra, "No encontrada")
    else: 
        inv_dic = {v: k for k, v in dic.items()}
        resultado = inv_dic.get(palabra, "No encontrada")
    
    label_traduccion.config(text=resultado)


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

btn_agregar=tk.Button(ventana,text="Agregar",command=agregar)
btn_agregar.place(x=120,y=370)
            

ventana.mainloop()