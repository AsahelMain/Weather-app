

class WeatherInfo:
    """
    Clase que modela la información del clima de lugares con aeropuerto

    ...

    Atributos:
    ---------
    weather_main : str
        El clima principal
    weather_description : str
        La descripción del clima
    main_temp : str
        La temperatura general
    main_feelslike : str
        La sensación térmica
    main_temp_min : str
        La temperatura mínima
    main_temp_max : str
        La temperatura máxima
    main_humidity : str
        El grado de humedad
    aiport_iata_code : str
        El código IATA del aeropuerto 

    Métodos
    -------
    get_data():
        Método que imprime los atributos de la clase
    get_attributes_as_list():
        Método que regresa los atributos de la clase en forma de una lista

    """

    def __init__(self,  weather_main = '', weather_description = '', main_temp = '', main_feelslike = '', main_temp_min = '', main_temp_max = '', main_humidity = '', airport_iata_code = ''):
        """
        Construye todos los atributos necesarios para el objeto WeatherInfo

        Parámetros
        ----------
            weather_main : str
            El clima principal
            weather_description : str
                La descripción del clima
            main_temp : str
                La temperatura general
            main_feelslike : str
                La sensación térmica
            main_temp_min : str
                La temperatura mínima
            main_temp_max : str
                La temperatura máxima
            main_humidity : str
                El grado de humedad
            aiport_iata_code : str
                El código IATA del aeropuerto  
        """
        self.weather_main = weather_main
        self.weather_description = weather_description
        self.main_temp = main_temp
        self.main_feelslike = main_feelslike
        self.main_temp_min = main_temp_min
        self.main_temp_max = main_temp_max
        self.main_humidity = main_humidity
        self.aiport_iata_code = airport_iata_code

    def get_data(self):
        """
        Imprime todos los atributos del objeto

        Parámetros
        ----------
        None

        Returns
        -------
        None
        """
        print(f'{self.weather_main}, {self.weather_description}, {self.main_temp}, {self.main_feelslike}, {self.main_temp_min}, {self.main_temp_max}, {self.main_humidity}, {self.aiport_iata_code}')
       
    
    def get_attributes_as_list(self):
        """
        Regresa los atributos del objeto en forma de lista

        Parámetros
        ----------
        None

        Returns
        -------
            attributes : lista de strings
                Los atributos del objeto en forma de lista 
        """
        attributes = []
        attributes.append(self.main_temp)
        attributes.append(self.main_temp_max)
        attributes.append(self.main_temp_min)
        attributes.append(self.main_feelslike)
        attributes.append(self.main_humidity)
        attributes.append(self.weather_description)
        attributes.append(self.aiport_iata_code)
        return attributes
 


          
