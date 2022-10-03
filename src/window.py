"""
Modelado y programación - Proyecto 01 
Alumnos:
	-Main Cerezo Asahel Said
	-Reyes López Eduardo Alfonso
El diseño de la interfaz está basado en el código de Magno Efren, cuyo github es el siguiente: https://github.com/MagnoEfren
"""

from tkinter import  Button, Entry, Label, PhotoImage, Frame
from tkinter.ttk import Combobox    
import time
import os
from airport import Airport
from readcsv import ReadCSV

class Window(Frame):
	"""
	Clase usada para representar la ventana de la aplicación
		
	...

	Atributos:
	-----------
	reader : ReadCSV
		objeto que permite obtener todos los aeropuertos
	airports_dictionary : Airport
		diccionario con los distintos aeropuertos
	airports_lists : Airport
		lista con los distintos aeropuertos

	Métodos:
	----------
	get_weather_info(airport: Airport):
		Método que recibe un objeto de tipo Airport y que regresa los atributos climáticos del lugar
		en una lista
	search_weather():
		Método que busca el lugar deseado y muestra en pantalla la información climática obtenida
	widgets():
		Método con todos los widgets de la ventana
	"""
	
	

	def __init__(self, master, *args):
		"""
		Cosntructor de la clase window que contiene los elementos con los que va a interactuar el usuario.

		...

		Parámetros:
		---------
		master : str 
			Representa la ventana padre. Es un parámetro opcional y por default es none. 
		*args : non-keyword
			Representa un número variable de argumentos.

		Atributos:
		reader : ReadCSV
			Contiene la lectura de la base de datos.
		airports_dictionary : Dictionary
			Diccionario cuyas llaves son los códigos iata y que contiene las ciudades con sus latitudes y longitudes.
		airports_list : List
			Lista de ciudades de la base de datos.
		cache : Dictionary 
			Diccionario cuyas llaves son los códigos iata y contiene la información climática de las ciudades guardadas.
		click : int
			Tiene por efecto desatar un evento.
		frame : Widget Frame
			Barra de búsqueda.
		frame2 : Widget Frame
			Marco principal de la ventana.
		frame3: Widget Frame
			Marco secundario de muestreo para "sensación térmica"
		frame4: Widget Frame
			Marco secundario de muestreo para "humedad"
		frame5: Widget Frame
			Marco secundario de muestreo para "descripción"
		"""

		super().__init__( master,*args)

		self.reader = ReadCSV()
		self.airports_dictionary = self.reader.getAirports()
		self.airports_list = self.reader.get_airports_list()
		self.cache = {}

		self.click = 1
		self.master.columnconfigure(0, weight=1)
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.master.columnconfigure(2, weight=1)
		self.master.rowconfigure(2, weight=1)
		self.frame = Frame(self.master, bg='white', highlightbackground='grey1',highlightthickness=2)
		self.frame.grid(columnspan=3, row = 0, sticky='nsew', padx=5, pady=5)
		self.frame2 = Frame(self.master, bg='DarkOliveGreen1', highlightbackground='grey1',highlightthickness=2)
		self.frame2.grid(columnspan=3, row = 1, sticky='nsew', padx=5, pady=5)
		self.frame3 = Frame(self.master, bg='peach puff', highlightbackground='grey1',highlightthickness=2) 
		self.frame3.grid(column=0, row = 2, sticky='nsew', padx=5, pady=5)
		self.frame4 = Frame(self.master, bg='royal blue', highlightbackground='grey1',highlightthickness=2)
		self.frame4.grid(column=1, row = 2, sticky='nsew', padx=5, pady=5)
		self.frame5 = Frame(self.master, bg='azure2', highlightbackground='grey1',highlightthickness=2) 
		self.frame5.grid(column=2, row =2 , sticky='nsew', padx=5, pady=5)

		

		self.widgets()

	def get_weather_info(self, airport: Airport):
		"""
		Método que recibe un objeto de tipo Airport y que regresa los atributos climáticos del lugar
		en una lista
		
		Parámetros
		----------
		airport : Airport
			el objeto de tipo aeropuerto
		
		Returns
		-------
		weather_list : Airport 
			Lista con la información del clima 
		"""
		airport_iata_code = airport.get_airport_code()
		if airport_iata_code in self.cache:
			weather = self.cache[airport_iata_code]
			weather_list = weather.get_attributes_as_list()
		else:
			weather = airport.get_weather()
			self.cache[airport_iata_code] = weather
			weather_list = weather.get_attributes_as_list()
		return weather_list
	
	
	def search_weather(self):
		"""
		Método que busca el lugar deseado y muestra en pantalla la información climática obtenida

		Parámetros
		----------
		None

		Returns
		-------
		None

		"""
		airport_iata_code = self.enter_airport.get()
		airport_iata_code = airport_iata_code.upper()

		if airport_iata_code in self.airports_dictionary:
			desired_airport = self.airports_dictionary[airport_iata_code]
			weather_info = self.get_weather_info(desired_airport)
			self.temp['text'] = "Temperatura " + str(float(weather_info[0])) + " °C\n\n" + "T máxima " + str(float(weather_info[1]))  +" °C\n\n" + "T mínima " +str(float(weather_info[2])) +" °C"
			self.feels_like['text'] = str(float(weather_info[3])) + " °C"
			self.humidity['text'] = str(int(weather_info[4])) + ' %'	  
			self.description['text'] = weather_info[5]
			self.place['text'] = weather_info[6]
		else:
			self.place['text'] = ''
			self.warning['text'] =  'Ciudad no encontrada'
			self.temp['text'] = ''
			self.feels_like['text'] = ''
			self.description['text'] = ''
			self.humidity['text'] = ''
			self.master.update()
			time.sleep(2)	    	
			self.warning['text'] = ''	

	def get_images(self):
		"""
		Función que obtiene las imágenes del directorio "images".

		Parámetros:
		----------
		None

		Returns:
		-------
			images : Array
			Arreglo con las imágenes del directorio.

		"""
		images = []

		absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
		absolute_path_search = os.path.join(absolute_folder_path, 'images/search.png')
		self.start = PhotoImage(file =absolute_path_search)
		images.append(self.start)
		absolute_path_temp = os.path.join(absolute_folder_path, 'images/info.png')
		self.image_temp = PhotoImage(file =absolute_path_temp)
		images.append(self.image_temp)
		absolute_path_feelslike = os.path.join(absolute_folder_path, 'images/feelslike.png')
		self.image_feelslike = PhotoImage(file =absolute_path_feelslike)
		images.append(self.image_feelslike)
		absolute_path_humidity = os.path.join(absolute_folder_path, 'images/humidity.png')
		self.image_humidity = PhotoImage(file =absolute_path_humidity)
		images.append(self.image_humidity)
		absolute_path_description = os.path.join(absolute_folder_path, 'images/climate.png')
		self.image_description = PhotoImage(file =absolute_path_description)
		images.append(self.image_description)

		return images

	def set_search_bar(self, images):
		"""
		Método que establece la apariencia y funcionalidad del primer frame que contiene lo relativo a la búsqueda.

		Parámetros: 
		----------
		images : Array
			Arreglo de imágenes.

		Returns:
		-------
		None.

		"""

		def delete_text(e):
			"""
			Método que borra la entrada de enter_airport.

			Parámetros: 
			----------
			e : Event Listener
				Se activa con la interacción con el usuario. 

			Returns:
			-------
			None.

			"""
			self.enter_airport.delete(0,"end")

		self.bt_start = Button(self.frame, image= images[0], bg='OliveDrab1',highlightthickness=0, activebackground='white', bd=0, command = self.search_weather)
		self.bt_start.grid(column=0, row=0, padx=2, pady=2)

		self.enter_airport = Entry(self.frame, font=('Verdana', 14),highlightbackground = "grey1", highlightcolor= "green2", highlightthickness=2)
		self.enter_airport.grid(column=1,row=0)
		self.enter_airport.insert(0, "Introducir código IATA")
		self.enter_airport.bind("<FocusIn>", delete_text)

		Label(self.frame,text='	Aeropuertos disponibles:',fg= 'gray55', bg='white',font=('Verdana',12)).grid(column=2,row=0, padx=5)

		self.airport_list = Combobox(self.frame, state = "readonly", values=self.airports_list, font=('Helvetica',12,'bold'))
		self.airport_list.grid(column=3, row=0)

		self.warning = Label(self.frame,fg= 'red3', bg='white',font=('Verdana',12))
		self.warning.grid(column=4,row=0, padx=5)

		self.place = Label(self.frame,fg= 'forest green', bg='white',font=('Helvetica',12,'bold'))
		self.place.grid(column=5,row=0, padx=5)

	def set_frames(self, images):
		"""
		Método que establece la apariencia y funcionalidad de los frames de la ventana.

		Parámetros: 
		----------
		images : Array

		Returns:
		-------
		None.

		"""
		Label(self.frame2,text='Informe del clima', bg='DarkOliveGreen1', font=('Helvetica',20,'bold')).pack(expand=1)
		Label(self.frame3,text='Sensación térmica', bg='peach puff', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame4,text='Humedad' , bg='royal blue', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame5,text='Descripción' , bg='azure2', font=('Helvetica',14,'bold')).pack(expand=1)

		Label(self.frame2, image= images[1], bg='DarkOliveGreen1').pack(expand=1, side='left')
		Label(self.frame3, image= images[2], bg='peach puff').pack(expand=1, side='left')
		Label(self.frame4, image= images[3], bg='royal blue').pack(expand=1, side='left')
		Label(self.frame5, image= images[4], bg='azure2').pack(expand=1, side='left')

		self.temp = Label(self.frame2, bg='DarkOliveGreen1', font = "Helvetica 16 bold")
		self.temp.pack(expand=1, side='right')
		self.feels_like = Label(self.frame3,bg='peach puff', font = "Helvetica 16 bold")
		self.feels_like.pack(expand=1, side='right')
		self.humidity = Label(self.frame4, bg='royal blue', font = "Helvetica 16 bold")
		self.humidity.pack(expand=1, side='right')
		self.description = Label(self.frame5, bg='azure2', font = "Helvetica 16 bold")
		self.description.pack(expand=1, side='right')

	def widgets(self):
		"""
		Método que establece la visualización e interacción con los widgets.

		Parámetros: 
		----------
		None.

		Returns:
		-------
		None.

		"""
		self.images = self.get_images()
		self.set_search_bar(self.images)
		self.set_frames(self.images)