"""
Modelado y programación - Proyecto 01 
Alumnos:
	-Main Cerezo Asahel Said
	-Reyes López Eduardo Alfonso
El diseño de la interfaz está basado en el código de Magno Efren, cuyo github es el siguiente: https://github.com/MagnoEfren
"""

from tkinter import  Tk, PhotoImage
from window import Window  
import os

if __name__ == "__main__":
	window = Tk()
	window.title('App del clima')
	window.config(bg='white')
	window.minsize(height= 600,width=1000)
	absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
	absolute_image_path = os.path.join(absolute_folder_path, 'images/weather.png')
	window.call('wm', 'iconphoto', window._w, PhotoImage(file=absolute_image_path))
	window.geometry('500x300+180+80')
	app = Window(window)
	app.mainloop()
