import unittest
import os
import sys
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
sys.path.insert(0,parent_directory + "/src")
from airport import Airport
from weatherInfo import WeatherInfo

class TestAirport(unittest.TestCase):
    """
    Clase de prueba para la clase airport.

    ...

    Atributos:
    ---------
    airportMEX : Airport
        Objeto con la información del aeropuerto de la Ciudad de México.

    Métodos:
    -------
    test_get_airport_code():
        Prueba el método get_airport_code.
    test_get_latitude():
        Prueba el método get_latitude.
    test_get_longitude():
        Prueba el método get_longitude.
    test_get_weather():
        Prueba el método get_weather.
    """

    airportMEX = Airport.__new__(Airport)
    airportMEX.__init__('MEX', '19.4363', '-99.0721')

    def test_get_airport_code(self):
        """
        Método que prueba get_airport_code viendo 
        que regrese el código iata correcto.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.assertEqual(self.airportMEX.get_airport_code(), 'MEX') 

    def test_get_latitude(self):
        """
        Método que prueba get_latitude verifcando que regrese 
        la latitud correcta.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.assertEqual(self.airportMEX.get_latitude(), '19.4363') 

    def test_get_longitude(self):
        """
        Método que prueba get_longitude verifcando que regrese 
        la longitud correcta.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.assertEqual(self.airportMEX.get_longitude(), '-99.0721')

    def test_get_weather(self):
        """
        Método que prueba get_weather verificando que regrese
        un objeto tipo WeatherInfo.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        weather = self.airportMEX.get_weather()
        self.assertIsInstance(weather, WeatherInfo)


if __name__ == '__main__':
    unittest.main()