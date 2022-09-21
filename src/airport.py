import csv
import requests
import os
from weatherInfo import WeatherInfo

class Airport:
    #Atributos
    iata_code = ' '
    latitude = ' '
    longitude = ' '

    #Constructor
    def __init__(self, iata_code = ' ', latitude = ' ', longitude = ' '):
        self.iata_code = iata_code
        self.latitude = latitude
        self.longitude = longitude
    
    #Regresa la clave IATA del aeropuerto
    def get_airport_code(self):
        return self.iata_code
    
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

        try:
            #Llamada a la API
            r = requests.get(url = URL, params = parameters)
        except:
            print("Error while calling the API")
        
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
        airport_name = data['name']

        #Se construye un objeto de tipo WeatherInfo con la información obtenida
        new_weather_info = WeatherInfo(weather_main, weather_description, main_temp, main_feelslike, main_temp_min, main_temp_max, main_humidity, airport_name)

        return new_weather_info
