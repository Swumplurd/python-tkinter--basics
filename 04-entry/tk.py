from cProfile import label
from struct import pack
from tkinter import *

root = Tk()
root.title("Entry")

#El widget Entry nos permite tener una entrada de texto. Se puede decir que es el equivalente de input() pero en interfaz grafica
frame1 = Frame(root)    #Comenzamos por crear un frame dentro de root
frame1.pack()   #Lo empaquetamos

entry1 = Entry(frame1)  #Creamos una entry dentro del frame1
entry1.pack(side="right")   #La empaquetamos colocaldola a la derecha con el argumento side

label1 = Label(frame1, text="Nombres")  #Creamos una label que describa la entry1 con el texto "Nombres"
label1.pack(side="left")    #La empaquetamos y la colocamos a la izquierda

#Repetimos los pasos para crear un nuevo frame con su entry y su label pero indicando que sera para Apellido Paterno
frame2 = Frame(root)
frame2.pack()

entry2 = Entry(frame2)
entry2.pack(side="right")

label2 = Label(frame2, text="Apellido Paterno")
label2.pack(side="left")

#Repetimos los pasos para crear un nuevo frame con su entry y su label pero indicando que sera para Apellido Materno
frame3 = Frame(root)
frame3.pack()

entry3 = Entry(frame3)
entry3.pack(side="right")

label3 = Label(frame3, text="Apellido Paterno")
label3.pack(side="left")

root.mainloop()
