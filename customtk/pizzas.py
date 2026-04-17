import customtkinter as ctk
from tkinter import ttk, messagebox
import os

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Pizzas")
root.geometry("1000x600")

pedido_actual = []
archivo_ventas = "pizzas.txt"  

opciones_tamano = {"Chica":40, "Mediana":80, "Grande":120}
tamano_var = ctk.StringVar(value="Chica")
ingredientes_vars = {
    "Jamón": ctk.BooleanVar(),
    "Piña": ctk.BooleanVar(),
    "Champiñones": ctk.BooleanVar()
}

frame_izq = ctk.CTkFrame(root, width=600, height=580)
frame_izq.place(x=10, y=10)

ctk.CTkLabel(frame_izq, text="Nombre:").place(x=20, y=20)
nombre_var = ctk.StringVar()
ctk.CTkEntry(frame_izq, textvariable=nombre_var, width=200).place(x=120, y=20)

ctk.CTkLabel(frame_izq, text="Dirección:").place(x=20, y=60)
direccion_var = ctk.StringVar()
ctk.CTkEntry(frame_izq, textvariable=direccion_var, width=200).place(x=120, y=60)

ctk.CTkLabel(frame_izq, text="Teléfono:").place(x=20, y=100)
telefono_var = ctk.StringVar()
ctk.CTkEntry(frame_izq, textvariable=telefono_var, width=200).place(x=120, y=100)

ctk.CTkLabel(frame_izq, text="Tamaño:").place(x=20, y=140)
x_base = 120
for i, (tamano, precio) in enumerate(opciones_tamano.items()):
    ctk.CTkRadioButton(frame_izq, text=f"{tamano} ${precio}",
                       variable=tamano_var, value=tamano).place(x=x_base + i*150, y=140)

ctk.CTkLabel(frame_izq, text="Ingredientes:").place(x=20, y=180)
x_base = 120
for i, ing in enumerate(ingredientes_vars.keys()):
    ctk.CTkCheckBox(frame_izq, text=f"{ing} $10", variable=ingredientes_vars[ing]).place(x=x_base + i*150, y=180)

ctk.CTkLabel(frame_izq, text="Num. de Pizzas:").place(x=20, y=220)
num_var = ctk.IntVar(value=1)
ctk.CTkEntry(frame_izq, textvariable=num_var, width=80).place(x=120, y=220)
ctk.CTkButton(frame_izq, text="Agregar", command=lambda: agregar_pizza()).place(x=220, y=220)

tabla = ttk.Treeview(frame_izq, columns=("Tamaño","Ingredientes","Num","Subtotal"), show="headings", height=10)
tabla.heading("Tamaño", text="Tamaño")
tabla.heading("Ingredientes", text="Ingredientes")
tabla.heading("Num", text="Num. Pizzas")
tabla.heading("Subtotal", text="SubTotal")
tabla.place(x=20, y=350, width=600, height=200)

ctk.CTkButton(frame_izq, text="Quitar", command=lambda: quitar_pizza()).place(x=50, y=480)
ctk.CTkButton(frame_izq, text="Terminar", command=lambda: terminar_pedido()).place(x=250, y=480)

frame_der = ctk.CTkFrame(root, width=370, height=580)
frame_der.place(x=620, y=10)

ctk.CTkLabel(frame_der, text="Ventas del día").place(x=100, y=20)
ventas_text = ctk.CTkTextbox(frame_der, width=350, height=400)
ventas_text.place(x=10, y=60)
ventas_text.configure(state="disabled")



def agregar_pizza():
    tamano = tamano_var.get()
    precio_base = opciones_tamano[tamano]
    ingredientes = [ing for ing, var in ingredientes_vars.items() if var.get()]
    costo_ing = len(ingredientes) * 10
    num = num_var.get()
    subtotal = (precio_base + costo_ing) * num
    
    tabla.insert("", "end", values=(tamano, ",".join(ingredientes), num, subtotal))
    pedido_actual.append((tamano, ingredientes, num, subtotal))

def quitar_pizza():
    selected = tabla.selection()
    if selected:
        idx = tabla.index(selected[0])
        tabla.delete(selected[0])
        pedido_actual.pop(idx)

def terminar_pedido():
    total = sum(p[3] for p in pedido_actual)
    cliente = nombre_var.get()
    
    with open(archivo_ventas, "a", encoding="utf-8") as f:
        f.write(f"Cliente: {cliente}\n")
        f.write(f"Dirección: {direccion_var.get()}\n")
        f.write(f"Teléfono: {telefono_var.get()}\n")
        f.write("Pizzas:\n")
        for tamano, ingredientes, num, subtotal in pedido_actual:
            f.write(f"  - {tamano}, {','.join(ingredientes)}, Num:{num}, Subtotal:${subtotal}\n")
        f.write(f"TOTAL: ${total}\n")
        f.write("="*40 + "\n")
    
    messagebox.showinfo("Pedido terminado", f"Total del pedido: ${total}")
    pedido_actual.clear()
    tabla.delete(*tabla.get_children())
    cargar_historial()

def cargar_historial():
    if os.path.exists(archivo_ventas):
        with open(archivo_ventas, "r", encoding="utf-8") as f:
            contenido = f.read()
        ventas_text.configure(state="normal")
        ventas_text.delete("1.0", "end")
        ventas_text.insert("end", contenido)
        ventas_text.configure(state="disabled")

cargar_historial()

root.mainloop()
