import unittest
import os
import sys
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
sys.path.insert(0,parent_directory + "/src")
from airport import Airport
from weatherInfo import WeatherInfo

class TestWeatherInfo(unittest.TestCase):
    """
    Clase de prueba para la clase WeatherInfo.

    ...

    Atributos:
    ---------
    airportMEX : Airport
        Objeto con la información del aeropuerto de la Ciudad de México.
    weather : WeatherInfo
        Información climática de la Ciudad de México.

    Métodos:
    -------
    test_get_data():
        Prueba la impresión del método get_data().
    test_get_attributes_as_list():
        Prueba el método get_attributes_as_list().
    """

    airportMEX = Airport.__new__(Airport)
    airportMEX.__init__('MEX', '19.4363', '-99.0721')
    weather = airportMEX.get_weather()

    def test_get_data(self):
        """
        Método que prueba get_data viendo si imprime 
        la información climática.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.weather.get_data()

    def test_get_attributes_as_list(self):
        """
        Método que prueba get_attributes_as_list() viendo
        si contiene el dato que debería en la 
        ubicación particular de la lista.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        list = self.weather.get_attributes_as_list()
        self.assertEqual(list[6], 'Pantitlán')

if __name__ == '__main__':
    unittest.main()