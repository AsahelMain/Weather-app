
import csv
import os.path
from airport import Airport

class ReadCSV:
    """
    Clase que se encarga de la lectura de la base de datos CSV.

    ...

    Atributos: 
    ---------
    airports_list : List 
        Lista de los aeropuertos dentro de la base de datos

    Métodos:
    -------
    getAirports():
        Método que obtiene la información de los aeropuertos.
    get_airports_list():
        Método que obtiene la lista de aeropuertos.
    """

    airports_list = []

    def getAirports(self):
        """
        Método que lee la base de datos y obtiene la información de los vuelos 
        usando un diccionario. Para cada vuelo, se guarda la información según
        los aeropuertos de origen y destino, almacenando su latitud y longitud sólo
        si no se encuentran en el diccionario. 

        Parámetros
        ----------
        None 

        Returns 
        -------
        None
        """
        airports = {}

        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.split(current_directory)[0]

        with open(parent_directory + '/dataset1.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                iata_code1 = row[0]
                iata_code2 = row[1]

                if iata_code1 not in airports:
                    airport_object = Airport(row[0], row[2], row[3])
                    airports[iata_code1] = airport_object
                    self.airports_list.append(iata_code1)
                if iata_code2 not in airports:
                    airport_object = Airport(row[1], row[4], row[5])
                    airports[iata_code2] = airport_object
                    self.airports_list.append(iata_code2)

        return airports

    def get_airports_list(self):
        """
        Método por el cual se obtiene la lista de aeropuertos
        (códigos iata) sin repetición que se encuentran en la 
        base de datos como aerpuertos ya sea de origen o destino.

        Parámetros 
        ----------
        None 

        Returns 
        -------
        airports_list : List
            Lista de aeropuertos (códigos iata)
        """
        return self.airports_list
