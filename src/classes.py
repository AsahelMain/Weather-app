import csv
from hashlib import new
import requests
from urllib import request
import os

#Clase City. Modela una ciudad.
class City:
    #Atributos
    city = ' '
    latitude = ' '
    longitude = ' '

    #Constructor
    def __init__(self, city = ' ', latitude = ' ', longitude = ' '):
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
    
    #Regresa la clave IATA de la ciudad
    def get_city(self):
        return self.city
    
    #Regresa la latitud de la ciudad
    def get_latitude(self):
        return self.latitude
    
    #Regresa la longitud de la ciudad
    def get_longitude(self):
        return self.longitude

    #Lee el archivo key.csv y regresa la llave API 
    def get_key(self):
        apikey = ''
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_key_path = os.path.join(absolute_folder_path, 'key.csv')
        with open(absolute_key_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                apikey = row[0]
        return apikey

    #Método que hace una llamada a la API para obtener el clima de la ciudad
    #Regresa un objeto de tipo WeatherInfo
    def get_weather(self):

        #Se obtiene la llave API
        apikey = self.get_key()
        URL = "http://api.openweathermap.org/data/2.5/weather?" 
        URL += "lat=" + self.latitude + "&lon=" + self.longitude + "&appid=" + apikey + "&units=metric&lang=es"
        parameters = {'address':"location"}

        #Llamada a la API
        r = requests.get(url = URL, params = parameters)

        #Se extraen los datos en forma de diccionario con la función Json
        data = r.json()
        
        #Se accede a los atributos deseados: temperatura, sensación térmica, humedad, etcétera. Se guardan en distintas variables
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        main_temp = data['main']['temp']
        main_feelslike = data['main']['feels_like']
        main_temp_min = data['main']['temp_min']
        main_temp_max = data['main']['temp_max']
        main_humidity = data['main']['humidity'] 

        #Se construye un objeto de tipo WeatherInfo con la información obtenida
        new_weather_info = WeatherInfo(weather_main, weather_description, main_temp, main_feelslike, main_temp_min, main_temp_max, main_humidity)

        return new_weather_info


#Clase WeatherInfo. Modela la información del clima de una ciudad 
class WeatherInfo:

    #Atributos
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
 


          