import tkinter as tk
from tkinter import ttk
import serial, time

def led():
    arduino = serial.Serial("COM5", 9600)
    time.sleep(2)
    arduino.write(b'9')
    arduino.close()

root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
boton = ttk.Button(text="¡Hola, mundo!", command=led)
boton.place(x=50, y=50)
root.mainloop()