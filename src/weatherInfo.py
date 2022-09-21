
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
    aiport_iata_code = ''

    #Constructor
    def __init__(self,  weather_main = '', weather_description = '', main_temp = '', main_feelslike = '', main_temp_min = '', main_temp_max = '', main_humidity = '', airport_iata_code = ''):
        self.weather_main = weather_main
        self.weather_description = weather_description
        self.main_temp = main_temp
        self.main_feelslike = main_feelslike
        self.main_temp_min = main_temp_min
        self.main_temp_max = main_temp_max
        self.main_humidity = main_humidity
        self.aiport_iata_code = airport_iata_code

    #Método que imprime los atributos de la clase
    def get_data(self):
        print(f'{self.weather_main}, {self.weather_description}, {self.main_temp}, {self.main_feelslike}, {self.main_temp_min}, {self.main_temp_max}, {self.main_humidity}, {self.aiport_iata_code}')
       
    #Método que regresa los atributos de la clase en forma de una lista
    def get_attributes_as_list(self):
        attributes = []
        attributes.append(self.main_temp)
        attributes.append(self.main_temp_max)
        attributes.append(self.main_temp_min)
        attributes.append(self.main_feelslike)
        attributes.append(self.main_humidity)
        attributes.append(self.weather_description)
        attributes.append(self.aiport_iata_code)
        return attributes
 


          
