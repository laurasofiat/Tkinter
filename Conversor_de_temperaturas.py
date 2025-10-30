import tkinter as tk
ventana=tk.Tk()
ventana.title("Conviertir temperaturas")
ventana.geometry("500x600")

num_var=tk.StringVar()


tk.Label(ventana, text="Ingrese temperatura").pack()
tk.Entry(ventana, textvariable=num_var).pack()

def convertir_primer_numero():
    n=float(num_var.get())
    s=(n*9/5)+32
    solucion=f"{n} En grados Fahrenheit es: {s}"
    tk.Label(ventana, text=solucion).pack()

def borrar():
    num_var.set("")

def convertir_segun_numero():
    s=float(num_var.get())
    s1=(s-32)*5/9
    solucion1=f"{s} En grados Celsius es: {s1}"
    tk.Label(ventana, text=solucion1).pack()

tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_primer_numero).pack()
tk.Button(ventana, text="Convertir a Celsius", command=convertir_segun_numero).pack()
tk.Button(ventana, text="Borrar", command=borrar).pack()

ventana.mainloop()