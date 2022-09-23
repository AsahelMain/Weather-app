#Modelado y programación - Proyecto 01 
#Alumnos:
#	-Main Cerezo Asahel Said
#	-Reyes López Eduardo Alfonso

import csv
import os.path
from airport import Airport

class ReadCSV:

    airports_list = []

    def getAirports(self):
        airports = {}

        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.split(current_directory)[0]

        with open(parent_directory + '\dataset1.csv', 'r') as file:
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
        return self.airports_list
