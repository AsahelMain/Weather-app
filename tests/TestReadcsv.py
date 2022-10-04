import unittest
import os
import sys
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
sys.path.insert(0,parent_directory + "/src")
from readcsv import ReadCSV
from airport import Airport

class TestReadcsv(unittest.TestCase):
    """
    Clase de prueba para la clase readcsv

    ...

    Métodos:
    -------
    test_get_airports():
        Prueba el método get_airports.
    test_dictionary():
        Verifica el diccionario de códigos de aeropuerto.
    test_list():
        verifica la lista de aeropuertos.
    """

    def test_get_airports(self):
        """
        Método que prueba get_airports viendo que el diccionario
        contenga aeropuertos usando las llaves de la lista.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.reader = ReadCSV()
        airports_dictionary = self.reader.get_airports()
        airports_list = self.reader.get_airports_list()
        for iata_code in airports_list:
            airport = airports_dictionary[iata_code]
            self.assertIsInstance(airport, Airport)

    def test_dictionary(self):
        """
        Método que verifica si el diccionario guarda correctamente 
        los datos de cada aeropuerto.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.reader = ReadCSV()
        self.airports_dictionary = self.reader.get_airports()
        self.airportMEX = self.airports_dictionary['MEX']
        self.assertEqual(self.airportMEX.get_latitude(), '19.4363')
        self.assertEqual(self.airportMEX.get_longitude(), '-99.0721')

    def test_list(self):
        """
        Método que verifica que la lista de aeropuertos contenga 
        todos los aeropuertos de la base de datos.

        Parámetros 
        ----------
        None

        Returns
        -------
        None 
        """
        self.reader = ReadCSV()
        self.airports_dictionary = self.reader.get_airports()
        airports_list = self.reader.get_airports_list()
        self.assertEqual(len(airports_list), 156)


if __name__ == '__main__':
    unittest.main()