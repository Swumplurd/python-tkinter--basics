from tkinter import *

#Configuracion de la raiz
root = Tk()                             #Instancia de tkinter la cual nos permite tener una ventana
root.title("Calculadora")               #Agregamos un titulo a la ventana
root.iconbitmap("./assets/calc.ico")    #Agregamos un icono a la ventana
root.resizable(True, True)              #Podemos establecer si la ventana sera redimensionable en ancho o en alto

#Init
frame = Frame(root)                     #Creamos un frame dentro de root quien sera su elemento padre
frame.pack(fill="both", expand=1)       #Empaquetamos frame y el argumento fill nos permitira llenar el espacio en caso de que la ventana crezca; el argumento expand nos permitira expandir el frame al 100% del elemento padre

root.config(bg="#06283D", relief="groove", bd=10)   #El metodo config nos permite confiurar un elemento. Podemos configurar el color de fondo con el parametro bd, un relieve con el parametro relief, un borde con el parametro bd
frame.config(width=480, height=320, bg="#DFF6FF", cursor="spider", bd=15)   #De igual manera configuramos este frame con los parametros antes mencionados y otorgandole una altura y un ancho con height y width respectivamente, ademas tambien agrefamos un cursor personalizado con el argumento cursor

#Finalmente bucle de la aplicacion
root.mainloop()     #El metodo mainloop() es el que nos permite ejecutar toda la configuracion previa y permite mostrar la ventana mientras el proceso siga activo