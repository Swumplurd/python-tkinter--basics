from tkinter import *

root = Tk()
root.title("Imagenes")

imagen = PhotoImage(file="./assets/model.gif")  #Para agregar imagenes usamos la clase PhotoImage
Label(root, image=imagen, bd=0).pack()          #Para mostrarla en nuestra interfaz grafica lo hacemos mediante una label

root.mainloop()