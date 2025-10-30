import tkinter as tk
ventana=tk.Tk()
ventana.title("Registro de datos básicos")
ventana.geometry("500x600")

nombre_var=tk.StringVar()
apellido_var=tk.StringVar()
edad_var=tk.StringVar()
correo_var=tk.StringVar()

tk.Label(ventana, text="Nombres").pack()
tk.Entry(ventana, textvariable=nombre_var).pack()

tk.Label(ventana, text="Apellidos").pack()
tk.Entry(ventana, textvariable=apellido_var).pack()

tk.Label(ventana, text="Edad").pack()
tk.Entry(ventana, textvariable=edad_var).pack()

tk.Label(ventana, text="Correo Electrónico").pack()
tk.Entry(ventana, textvariable=correo_var).pack()

def guardar():
    n=nombre_var.get()
    a=apellido_var.get()
    e=edad_var.get()
    c=correo_var.get()
    texto= f"Datos guardados:\n\nNombre: {n}\nApellido: {a}\nEdad: {e}\nCorreo: {c}"
    tk.Label(ventana, text=texto).pack(pady=10)

tk.Button(ventana, text="Guardar", command=guardar).pack()

ventana.mainloop()
    