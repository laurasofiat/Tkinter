import tkinter as tk
ventana=tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("300x300")

tarea=tk.StringVar()
tk.Label(ventana, text="Ingrese una tarea").pack()
tk.Entry(ventana, textvariable=tarea).pack()

def agregar():
    tareas.insert(tk.END, tarea.get())
  
tk.Button(ventana, text="Agregar tarea", command=agregar).pack()

def eliminar():
    seleccion=tareas.curselection()
    for i in reversed(seleccion):
        tareas.delete(i)

tk.Button(ventana, text="Eliminar Tarea", command=eliminar).pack()

tareas=tk.Listbox(ventana)
tareas.pack()

ventana.mainloop() 