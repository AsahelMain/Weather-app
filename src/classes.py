import csv
from hashlib import new
import requests
from urllib import request
import os

#Clase Ticket. Modela los tickets de avión
class Ticket:
    origen = ''
    destino = ''
    lat_origen = ''
    long_origen = ''
    lat_destino = ''
    long_destino = ''

    #Constructor
    def __init__(self, origen = '', destino = '', latO = '', longO = '', latD = '', longD = ''):
        self.origen = origen
        self.destino = destino
        self.lat_origen = latO
        self.long_origen = longO
        self.lat_destino = latD
        self.long_destino = longD

    #Método que regresa la llave a modo de string para hacer la llamada a la API. Lee la llave del archivo key.csv
    def get_key(self):
        apikey = ''
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_key_path = os.path.join(absolute_folder_path, 'key.csv')
        with open(absolute_key_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                apikey = row[0]
        return apikey


    #Método que regresa el clima de la ciudad de origen. Regresa un objeto de tipo WeatherInfo
    def get_weather_origin(self):
        apikey = self.get_key()
        URL = "http://api.openweathermap.org/data/2.5/weather?"
        URL += "lat=" + self.lat_origen + "&lon=" + self.long_origen + "&appid=" + apikey + "&units=metric&lang=es"
        parameters = {'address':"location"}
        #Llamada a la API
        r = requests.get(url = URL, params = parameters)
        #Se extraen los datos en forma de diccionario con la función Json
        data = r.json()
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        main_temp = data['main']['temp']
        main_feelslike = data['main']['feels_like']
        main_temp_min = data['main']['temp_min']
        main_temp_max = data['main']['temp_max']
        main_humidity = data['main']['humidity'] 
        new_weather_info = WeatherInfo(weather_main, weather_description, main_temp, main_feelslike, main_temp_min, main_temp_max, main_humidity)

        return new_weather_info
    
    #Método que regresa el clima de la ciudad de destino. Regresa un objeto de tipo WeatherInfo
    def get_weather_destination(self):
        apikey = self.get_key()
        URL = "http://api.openweathermap.org/data/2.5/weather?"
        URL += "lat=" + self.lat_destino + "&lon=" + self.long_destino + "&appid=" + apikey + "&units=metric&lang=es"
        parameters = {'address':"location"}
        r = requests.get(url = URL, params = parameters)
        data = r.json()
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        main_temp = data['main']['temp']
        main_feelslike = data['main']['feels_like']
        main_temp_min = data['main']['temp_min']
        main_temp_max = data['main']['temp_max']
        main_humidity = data['main']['humidity'] 
        new_weather_info = WeatherInfo(weather_main, weather_description, main_temp, main_feelslike, main_temp_min, main_temp_max, main_humidity)

        return new_weather_info
    
    #Método que regresa la ciudad de origen
    def get_origin_city(self):
        return self.origen

    #Método que regresa la ciudad de destino
    def get_destination_city(self):
        return self.destino

    #Método que imprime los atributos de la clase
    def get_data(self):
        print(f'{self.origen}, {self.destino}, {self.lat_origen}, {self.long_origen}, {self.lat_destino}, {self.long_destino}')


#Clase WeatherInfo. Contiene la información del clima de una ciudad 
class WeatherInfo:
    weather_main = ''
    weather_description = ''
    main_temp = ''
    main_feelslike = ''
    main_temp_min = ''
    main_temp_max = ''
    main_humidity = ''

    #Constructor
    def __init__(self,  weather_main = '', weather_description = '', main_temp = '', main_feelslike = '', main_temp_min = '', main_temp_max = '', main_humidity = '' ):
        self.weather_main = weather_main
        self.weather_description = weather_description
        self.main_temp = main_temp
        self.main_feelslike = main_feelslike
        self.main_temp_min = main_temp_min
        self.main_temp_max = main_temp_max
        self.main_humidity = main_humidity

    #Método que imprime los atributos de la clase
    def get_data(self):
        print(f'{self.weather_main}, {self.weather_description}, {self.main_temp}, {self.main_feelslike}, {self.main_temp_min}, {self.main_temp_max}, {self.main_humidity}')
       
    #Método que regresa los atributos de la clase en forma de una lista
    def get_attributes_as_list(self):
        attributes = []
        attributes.append(self.main_temp)
        attributes.append(self.main_temp_max)
        attributes.append(self.main_temp_min)
        attributes.append(self.main_feelslike)
        attributes.append(self.main_humidity)
        attributes.append(self.weather_description)
        return attributes
 
    

