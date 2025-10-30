import tkinter as tk #Importa la librería tkinter
ventana=tk.Tk() #Crea la venta en la librería
ventana.title("Calculadora con Tkinter") #Crea el título de la ventana
ventana.geometry("400x300") #Da las medidas de la ventana
entrada=tk.Entry(ventana, width=20, font=("Arial",18),justify="right") #crea el ancho (width) de entradas,el tipo de letra, su tamaño y su posición
entrada.grid(row=0, columnspan=4, padx=10, pady=10) #Ubica la rejilla, sus posiciones y sus espacios (padx y pady)
botones=[ #Posicion de los botones en la calculadora
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("+",4,2),("=",4,3)
]
def calcular(): #Función para calcular el resultado
    try:
        # Obtener la expresión del campo de entrada
        expresion = entrada.get()
        # Evaluar la expresión y convertir el resultado a string
        resultado = str(eval(expresion))
        # Limpiar el campo de entrada
        entrada.delete(0, tk.END)
        # Insertar el resultado
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END) #Borra el dato ingresado en la calculadora
        entrada.insert(0, "Error") #Inserta en la entra 0 la palabra "error" cuando ha ocurrido una falla   

def borrar(): #Función para borrar los datos ingresados
    entrada.delete(0, tk.END) #Borra el dato ingresado en la calculadora

def click_boton(numero): #Función para los botones de la calculadora
    entrada.insert(0, numero) #Inserta el valor del botón presionado en la entrada

for(texto,fila, columna)in botones: #recorre los botones para obtener su texto, fila y columna
    if texto=="=": #si el texto es igual a "="
        tk.Button(ventana, text=texto, width=5, height=2, font=("Arial"), command=calcular).grid(row=fila, column=columna, padx=5, pady=5) #Crea el botton de "=" con sus características y lo agrega a la rejilla
    else: #si no se cumple la condición anterior
        tk.Button(ventana, text=texto, width=5, heigth=2,font=("Arial",14), command=lambda t=texto: click_boton(t)).grid(row=fila, column=columna, padx=5, pady=5) #Crea los botones con sus características

tk.Button(ventana, text="C", widht=22, heigth=2, font=("Arial",14), command=borrar).grid(row=5, column=0, columpan=4, padx=5, pady=5) #crea el boton "c" con sus características le agrega la función de borrar y lo agrega a la rejilla 

ventana.mainloop() #Crea el bucle infinito para que la ventana se mantenga abierta  
        
        
        
        
        
        
        
        