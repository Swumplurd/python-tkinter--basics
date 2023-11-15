from cProfile import label
from struct import pack
from tkinter import *

root = Tk()
root.title("Entry Grid")

#El metodo grid() nos permitira acomodar nuestros widgets de forma que podremos hacer referencia a que fila y que columna queremos posicionar un elemento
#Grid puede ayuarnos a acomodar elementos y que se vean bien esteticamente
label1 = Label(root, text="Nombres")
label1.grid(row=0, column=0, sticky="e", padx=5, pady=5)    #El lugar de usar pack() usamos grid() y le pasamos los argumentos row y column. Con el argumento sticky podemos alinear el texto hacia algun lugar
entry1 = Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(root, text="Apellido Paterno")
label2.grid(row=1, column=0, padx=5, pady=5)    #Damos un salto en la row para que se acomode justo debajo de la primera row
entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)    #Con los arguentos padx y pady podemos agregar separacion en eje x y eje y para una mejor estetica
entry2.config(justify="center")                 #Usando el metodo config() y pasando el argumento justify podemos indicar la alinacion del texto dentro de la entry

label3 = Label(root, text="Apellido Paterno")
label3.grid(row=2, column=0, padx=5, pady=5)
entry3 = Entry(root)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(justify="right")

label4 = Label(root, text="Edad")
label4.grid(row=3, column=0, sticky="e", padx=5, pady=5)
entry4 = Entry(root)
entry4.grid(row=3, column=1, padx=5, pady=5)
entry4.config(state="disabled")                 #Con el parametro state podemos deshabilitar una entrada

label4 = Label(root, text="Contraseña")
label4.grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry4 = Entry(root)
entry4.grid(row=4, column=1, padx=5, pady=5)
entry4.config(show="*")                         #Con el parametro show podemos elegir que caracter mostrar al momento de escribir. Esto es ideal para contraseñas

root.mainloop()
