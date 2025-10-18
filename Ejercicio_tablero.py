import tkinter as tk #Importa la librería tkinter
#------------------Funciones---------------------
def suma(): #Función para sumar los números
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        resultado.set(str(n1 + n2))
    except ValueError: #Menja el error si la entrada no es válida
        resultado.set("error")

#----------------Ventana principal------------------
ventana = tk.Tk() #Crea la ventana  en la librería 
ventana.title("Calculadora básica") #Crea el título de la ventana
ventana.geometry("250x180") #define le tamaño de la ventana

#------------------Variable-------------------------
resultado = tk.StringVar() 

# ------------------Widgets-------------------------
tk.Label(ventana, text="Número 1:").pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Suma", command=suma).pack(pady=5)
tk.Label(ventana, text="Resultado:").pack()
tk.Label(ventana, textvariable=resultado, fg="blue", font=("Arial", 12)).pack()

ventana.mainloop()



print("calculadora lista")