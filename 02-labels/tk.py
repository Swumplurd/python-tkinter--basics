from tkinter import *

root = Tk()
root.title("Labels")

Label(root, text="Hola Mundo Arriba-Izquierda").pack(anchor="nw")   #Podemos crear labels y empaquetarlas directamente sin almacenarlas en una variable de esta forma
Label(root, text="Hola Mundo Centro").pack(anchor="center")         #El parametro text nos permite escribir el texto de la etuqueta
Label(root, text="Hola Mundo Abajo-Derecha").pack(anchor="se")      #EL parametro anchor dentro del metodo pack() nos permite anclar el contenido hacia algun lugar de la ventana usando como referencia los puntos cardinales en ingles

lastlabel = Label(root, text="Ultmima Etiqueta")    #Creamos una etiqueta almacenada en la variable lastlabel
lastlabel.pack()    #La empaquetamos
lastlabel.config(bg="gray", fg="white", font=("Arial", 24))   #Podemos añadir colores de fondo con bg, color de fuente con fg y cambiar de tipo y tamaño de fuente con font

root.mainloop()