import csv
import requests
import os
from weatherInfo import WeatherInfo

class Airport:
    """
    Clase que modela un aeropuerto

    ...

    Atributos
    ---------
    iata_code : str
        El código IATA del aeropuerto
    latitude : str
        La latitude del aeropuerto
    longitude : str
        La longitud del aeropuerto

    Métodos
    -------
    get_airport_code():
        Regresa la clave IATA del aeropuerto
    get_latitude():
        Regresa la latitud geográfica del aeropuerto
    get_longitude():
        Regresa la longitud geográfica del aeropuerto
    get_weather():
        Obtiene el clima del lugar, regresa un objeto de tipo WeatherInfo
    __get_key(filename, search_path):
        Método privado que regresa la llave de OpenWeather
    
    """
   
    def __init__(self, iata_code = ' ', latitude = ' ', longitude = ' '):
        """
        Construye todos los atributos necesarios para el objeto Airport

        Parámetros
        ----------
           iata_code : str
                El código IATA del aeropuerto
           latitude : str
                La latitude del aeropuerto
           longitude : str
                La longitud del aeropuerto
    
        """

        self.iata_code = iata_code
        self.latitude = latitude
        self.longitude = longitude
    
    def get_airport_code(self):
        """
        Regresa el código iata del aeropuerto

        Parámetros
        ----------
        None

        Returns
        -------
            iata_code : str
                el código iata del aeropuerto
        """
        return self.iata_code
    
    def get_latitude(self):
        """
        Regresa la latitud geográfica del aeropuerto

        Parámetros
        ----------
        None

        Returns
        -------
            latitude : str
                la latitud geográfica del aeropuerto
        """
        return self.latitude

    def get_longitude(self):
        """
        Regresa la longitud geográfica del aeropuerto

        Parámetros
        ----------
        None

        Returns
        -------
            longitude : str
                la longitud geográfica del aeropuerto
        """
        return self.longitude

    def __get_key(self, filename, search_path):
        """
        Busca el archivo key.csv, lo lee y regresa la llave que encontró

        Parámetros
        ----------
            filename : str
                el nombre del archivo a buscar
            search_path : str
                el directorio desde donde se buscará el archivo
        
        Returns
        -------
            apiKey : str
                la llave para llamar a la API
        """
        result = ' '
        for root, dir, files in os.walk(search_path):
            if filename in files:
                result = os.path.join(root, filename)

        with open(result, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                apikey = row[0]
        return apikey

    def get_weather(self):

        """
        Obtiene el clima del lugar haciendo una llamada a la API, regresa un objeto de tipo WeatherInfo

        Parámetros
        ----------
        None

        Returns
        -------
            new_weather_info : WeatherInfo
                La información climática del lugar

        """

        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.split(current_directory)[0]
        apikey = self.__get_key("key.csv", parent_directory)
        URL = "http://api.openweathermap.org/data/2.5/weather?" 
        URL += "lat=" + self.latitude + "&lon=" + self.longitude + "&appid=" + apikey + "&units=metric&lang=es"
        parameters = {'address':"location"}

        try:
            r = requests.get(url = URL, params = parameters)
        except:
            print("Error while calling the API")

        data = r.json()
        
        weather_main = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        main_temp = data['main']['temp']
        main_feelslike = data['main']['feels_like']
        main_temp_min = data['main']['temp_min']
        main_temp_max = data['main']['temp_max']
        main_humidity = data['main']['humidity'] 
        airport_name = data['name']

        new_weather_info = WeatherInfo(weather_main, weather_description, main_temp, main_feelslike, main_temp_min, main_temp_max, main_humidity, airport_name)

        return new_weather_info
