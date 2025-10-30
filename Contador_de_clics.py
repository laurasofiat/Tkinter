import tkinter as tk
ventana = tk.Tk()
ventana.title("Contador de clics")
ventana.geometry("300x200")

con= 0

def contar():
    global con
    con += 2
    etiqueta.config(text=f"Contador: {con}")

etiqueta = tk.Label(ventana, text=f"Contador: {con}")
etiqueta.pack()

boton = tk.Button(ventana, text="cuenta 2", command=contar)
boton.pack()

ventana.mainloop()


