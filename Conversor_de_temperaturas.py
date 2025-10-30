import tkinter as tk
ventana=tk.Tk()
ventana.title("Conviertir temperaturas")
ventana.geometry("500x600")

num_var=tk.StringVar()
num_var1=tk.StringVar()

tk.Label(ventana, text="Ingrese temperatura Celsius").pack()
tk.Entry(ventana, textvariable=num_var).pack()

def convertir_primer_numero():
    n=float(num_var.get())
    s=(n*1.8)+32
    solucion=f"{n} En grados Fahrenheit es: {s}"
    tk.Label(ventana, text=solucion).pack()

tk.Button(ventana, text="Convertir a Fahrenheit", command=convertir_primer_numero).pack()

tk.Label(ventana, text="Ingrese temperatura Fahrenheit").pack()
tk.Entry(ventana, textvariable=num_var1).pack()

def convertir_segun_numero():
    n1=float(num_var1.get())
    s1=(n1-32)/1.8
    solucion1=f"{n1} En grados Celsius es: {s1}"
    tk.Label(ventana, text=solucion1).pack()

tk.Button(ventana, text="Convertir a Celsius", command=convertir_segun_numero).pack()


ventana.mainloop()