from tkinter import  Tk, Button, Entry, Label,PhotoImage,Frame
from PIL import Image 
import requests       
import time
import os

class Window(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)
		self.click = 1
		
		self.master.columnconfigure(0, weight=1)
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.master.columnconfigure(2, weight=1)
		self.master.rowconfigure(2, weight=1)
		self.frame = Frame(self.master, bg='white', highlightbackground='grey1',highlightthickness=2)
		self.frame.grid(columnspan=3, row = 0, sticky='nsew', padx=5, pady=5)
		self.frame2 = Frame(self.master, bg='yellow green', highlightbackground='grey1',highlightthickness=2)
		self.frame2.grid(column=0, row = 1, sticky='nsew', padx=5, pady=5)
		self.frame3 = Frame(self.master, bg='orange2', highlightbackground='grey1',highlightthickness=2) 
		self.frame3.grid(column=1, row = 1, sticky='nsew', padx=5, pady=5)
		self.frame4 = Frame(self.master, bg='light cyan', highlightbackground='grey1',highlightthickness=2)
		self.frame4.grid(column=2, row = 1, sticky='nsew', padx=5, pady=5)
		self.frame5 = Frame(self.master, bg='peach puff', highlightbackground='grey1',highlightthickness=2) 
		self.frame5.grid(column=0, row = 2, sticky='nsew', padx=5, pady=5)
		self.frame6 = Frame(self.master, bg='royal blue', highlightbackground='grey1',highlightthickness=2)
		self.frame6.grid(column=1, row = 2, sticky='nsew', padx=5, pady=5)
		self.frame7 = Frame(self.master, bg='azure2', highlightbackground='grey1',highlightthickness=2) 
		self.frame7.grid(column=2, row =2 , sticky='nsew', padx=5, pady=5)

		self.widgets()

	def get_weather(self):
		city = self.enter_city.get()

		API = 'https://api.openweathermap.org/data/2.5/weather?q=' +city+ '&appid=a6c823e88b813b8ba68e3508021fc9ec&units=metric&lang=es'  
		try:
			json_datos = requests.get(API).json()
			self.temp['text'] = str(int(json_datos['main']['temp'])) + " °C"
			self.temp_min['text'] = str(int(json_datos['main']['temp_min']))  +" °C"
			self.temp_max['text'] = str(int(json_datos['main']['temp_max'])) +" °C"
			self.feels_like['text'] = str(int(json_datos['main']['feels_like'])) + " °C"
			self.humidity['text'] = str(json_datos['main']['humidity']) + ' %'	  
			self.description['text'] = json_datos['weather'][0]['description']  
			self.place['text'] =  json_datos['name'] + ' - '+ json_datos['sys']['country'] 
		except:
			self.warning['text'] =  'Ciudad no encontrada'
			self.temp['text'] = ''
			self.temp_min['text'] = ''
			self.temp_max['text'] = ''
			self.feels_like['text'] = ''
			self.description['text'] = ''
			self.humidity['text'] = ''
			self.master.update()
			time.sleep(2)	    	
			self.warning['text'] = ''
			self.place['text'] = ''	

	def widgets(self):
		absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
		absolute_path_search = os.path.join(absolute_folder_path, 'images/search.png')
		self.start = PhotoImage(file =absolute_path_search)
		absolute_path_temp = os.path.join(absolute_folder_path, 'images/temp.png')
		self.image_temp = PhotoImage(file =absolute_path_temp)
		absolute_path_tempmin = os.path.join(absolute_folder_path, 'images/temp_min.png')
		self.image_temp_min = PhotoImage(file =absolute_path_tempmin)
		absolute_path_tempmax = os.path.join(absolute_folder_path, 'images/temp_max.png')
		self.image_temp_max = PhotoImage(file =absolute_path_tempmax)
		absolute_path_feelslike = os.path.join(absolute_folder_path, 'images/feelslike.png')
		self.image_feelslike = PhotoImage(file =absolute_path_feelslike)
		absolute_path_humidity = os.path.join(absolute_folder_path, 'images/humidity.png')
		self.image_humidity = PhotoImage(file =absolute_path_humidity)
		absolute_path_description = os.path.join(absolute_folder_path, 'images/climate.png')
		self.image_description = PhotoImage(file =absolute_path_description)
		self.bt_start = Button(self.frame, image= self.start, bg='OliveDrab1',highlightthickness=0, activebackground='white', bd=0, command = self.get_weather)
		self.bt_start.grid(column=0, row=0, padx=2, pady=2)
		self.enter_city = Entry(self.frame, font=('Verdana', 14),highlightbackground = "grey1", highlightcolor= "green2", highlightthickness=2)
		self.enter_city.grid(column=1,row=0)
		Label(self.frame,text='Buscar ciudad',fg= 'gray55', bg='white',font=('Verdana',12)).grid(column=2,row=0, padx=5)
		self.warning = Label(self.frame,fg= 'red3', bg='white',font=('Verdana',12))
		self.warning.grid(column=3,row=0, padx=5)
		self.place = Label(self.frame,fg= 'forest green', bg='white',font=('Helvetica',12,'bold'))
		self.place.grid(column=4,row=0, padx=5)

		Label(self.frame2,text='Temperatura', bg='yellow green', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame3,text='T máxima', bg='orange2', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame4,text='T mínima' , bg='light cyan', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame5,text='Sensación térmica' , bg='peach puff', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame6,text='Humedad' , bg='royal blue', font=('Helvetica',14,'bold')).pack(expand=1)
		Label(self.frame7,text='Descripción' , bg='azure2', font=('Helvetica',14,'bold')).pack(expand=1)

		Label(self.frame2, image= self.image_temp, bg='yellow green').pack(expand=1, side='left')
		Label(self.frame3, image= self.image_temp_max, bg='orange2').pack(expand=1, side='left')
		Label(self.frame4, image= self.image_temp_min, bg='light cyan').pack(expand=1, side='left')
		Label(self.frame5, image= self.image_feelslike, bg='peach puff').pack(expand=1, side='left')
		Label(self.frame6, image= self.image_humidity, bg='royal blue').pack(expand=1, side='left')
		Label(self.frame7, image= self.image_description, bg='azure2').pack(expand=1, side='left')

		self.temp = Label(self.frame2, bg='yellow green', font = "Helvetica 16 bold")
		self.temp.pack(expand=1, side='right')
		self.temp_max = Label(self.frame3,bg='orange2', font = "Helvetica 16 bold")
		self.temp_max.pack(expand=1, side='right')
		self.temp_min = Label(self.frame4, bg='light cyan', font = "Helvetica 16 bold")
		self.temp_min.pack(expand=1, side='right')
		self.feels_like = Label(self.frame5, bg='peach puff', font = "Helvetica 16 bold")
		self.feels_like.pack(expand=1, side='right')
		self.humidity = Label(self.frame6, bg='royal blue', font = "Helvetica 16 bold")
		self.humidity.pack(expand=1, side='right')
		self.description = Label(self.frame7, bg='azure2', font = "Helvetica 16 bold")
		self.description.pack(expand=1, side='right')

if __name__ == "__main__":
	window = Tk()
	window.title('')
	window.config(bg='white')
	window.minsize(height= 600,width=1000)
	absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
	absolute_image_path = os.path.join(absolute_folder_path, 'images/weather.png')
	window.call('wm', 'iconphoto', window._w, PhotoImage(file=absolute_image_path))
	window.geometry('500x300+180+80')
	app = Window(window)
	app.mainloop()
