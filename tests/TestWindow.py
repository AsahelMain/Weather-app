import unittest
import os
import sys
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
sys.path.insert(0,parent_directory + "/src")
from airport import Airport
from window import Window
from tkinter import PhotoImage

class TestWindow(unittest.TestCase):
    """
    Clase de prueba para la clase Window.

    ...

    Atributos:
    ---------
    window : Window
        Objeto ventana para Tkinter.
    airportMEX : Airport
        Objeto con la información del aeropuerto de la Ciudad de México.

    Métodos:
    -------
    test_get_weather():
        Prueba el método get_weather().
    """

    window = Window.__new__(Window)
    window.cache = {}

    airportMEX = Airport.__new__(Airport)
    airportMEX.__init__('MEX', '19.4363', '-99.0721')

    def test_get_weather_info(self):
        """
        Método que prueba get_weather_info() verifcando 
        que el contenido de la lista sea correcto.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        weather_list = self.window.get_weather_info(self.airportMEX)
        self.assertEqual(weather_list[6], 'Pantitlán')

if __name__ == '__main__':
    unittest.main()