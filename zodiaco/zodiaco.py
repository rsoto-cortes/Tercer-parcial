import tkinter as tk
from tkinter import messagebox 
from PIL import Image,ImageTk

def imprimir():
    nom=entrada_nombre.get()
    ape1=entrada_apellido1.get()
    ape2=entrada_apellido2.get()
    nomcompleto=nom+" "+ape1+" "+ape2
    año=int(entrada_año.get())
    mes=int(entrada_mes.get())
    genero=int(opcion.get())
    añosfin=2026-año
    cerdo=(1959,1971,1983,1995,2007)
    rata=(1960,1972,1984,1996,2008)
    buey=(1961,1973,1985,1997,2009)
    tigre=(1962,1974,1986,1998,2010)
    conejo=(1963,1975,1987,1999,2011)
    dragon=(1964,1976,1988,2000,2012)
    serpiente=(1965,1977,1989,2001,2013)
    caballo=(1966,1978,1990,2002,2014)
    cabra=(1967,1979,1991,2003,2015)
    mono=(1968,1980,1992,2004,2016)
    gallo=(1969,1981,1993,2005,2017)
    perro=(1970,1982,1994,2006,2018)
    
    try:
        if nomcompleto == "":
            messagebox.showerror("Error","LLene todas las casillas")
        else:
            label_nomcompleto.config(text=f"Hola {nomcompleto}")
        
        
        if mes <= 0 or mes > 12:
            messagebox.showerror("Error","Mes invalido")
        elif mes > 3:
            añosfin = añosfin-1
            label_añosfinal.config(text=f"Tienes {añosfin} años")
        elif mes <= 3:
            label_añosfinal.config(text=f"Tienes {añosfin} años")
            
        if genero < 1 or genero > 2:
            messagebox.showerror("Error","Seleccione su genero")
            return
        
            
        i=0
        for i in range(5):
            if año == cerdo[i]:
                label_imagen.config(text="cerdo")
                          
            if año ==rata[i]:
                label_imagen.config(text="rata")
                
            if año == buey[i]:
                label_imagen.config(text="buey")
            
            if año == tigre[i]:
                label_imagen.config(text="tigre")
            
            if año == conejo[i]:
                label_imagen.config(text="conejo")
        
            if año == dragon[i]:
                label_imagen.config(text="dragon")
            
            if año == serpiente[i]:
                label_imagen.config(text="serpiente")

            if año ==caballo[i]:
                label_imagen.config(text="caballo")
            
            if año == cabra[i]:
                label_imagen.config(text="cabra")
                
            if año == mono[i]:
                label_imagen.config(text="mono")
                
            if año == gallo[i]:
                label_imagen.config(text="gallo")
                
            if año == perro[i]:
                label_imagen.config(text="perro")
            else:
                messagebox.showerror("Error","Año invalido")
                 
            
            
            
    except ValueError:
        messagebox.showerror("Error","LLene todas las casillas")
        
        
ventana=tk.Tk()
ventana.title("ZODIACO")
ventana.geometry("600x400")

frame_datos=tk.LabelFrame(ventana,text="")
frame_datos.place(x=35,y=10,width=275,height=350)

label=tk.Label(frame_datos,text="Datos Personales")
label.place(x=80,y=10)

label_nombre=tk.Label(frame_datos,text="Nombre")
label_nombre.place(x=10,y=40)

entrada_nombre=tk.Entry(frame_datos,width=30)
entrada_nombre.place(x=75,y=40)

label_apellido1=tk.Label(frame_datos,text="Apellido P")
label_apellido1.place(x=10,y=60)

entrada_apellido1=tk.Entry(frame_datos,width=30)
entrada_apellido1.place(x=75,y=60)

label_apellido2=tk.Label(frame_datos,text="Apellido M")
label_apellido2.place(x=10,y=80)

entrada_apellido2=tk.Entry(frame_datos,width=30)
entrada_apellido2.place(x=75,y=80)

label2=tk.Label(frame_datos,text="Fecha de nacimiento")
label2.place(x=80,y=140)

label_dia=tk.Label(frame_datos,text="Dia")
label_dia.place(x=35,y=170)

entrada_dia=tk.Entry(frame_datos,width=13)
entrada_dia.place(x=15,y=190)

label_mes=tk.Label(frame_datos,text="Mes")
label_mes.place(x=115,y=170)

entrada_mes=tk.Entry(frame_datos,width=13)
entrada_mes.place(x=90,y=190)

label_año=tk.Label(frame_datos,text="Año")
label_año.place(x=185,y=170)

entrada_año=tk.Entry(frame_datos,width=13)
entrada_año.place(x=165,y=190)

label3=tk.Label(frame_datos,text="Sexo")
label3.place(x=115,y=230)

opcion=tk.IntVar()

rbt_masculino=tk.Radiobutton(frame_datos,text="Masculino",variable=opcion,value=1)
rbt_masculino.place(x=95,y=250)

rbt_femenino=tk.Radiobutton(frame_datos,text="Femenino",variable=opcion,value=2)
rbt_femenino.place(x=95,y=270)

btn_imprimir=tk.Button(frame_datos,text="Imprimir",command=imprimir)
btn_imprimir.place(x=100,y=310)

label_nomcompleto=tk.Label(ventana,text="",font=("Arial","15"))
label_nomcompleto.place(x=325,y=20)

label_añosfinal=tk.Label(ventana,text="",font=("Arial","15"))
label_añosfinal.place(x=325,y=100)

label_signo=tk.Label(ventana,text=" ",font=("Arial","15"))
label_signo.place(x=325,y=180)

label_imagen=tk.Label(ventana,text="")
label_imagen.place(x=375,y=210)


ventana.mainloop()