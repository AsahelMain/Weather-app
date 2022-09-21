#Modelado y programación - Proyecto 01 
#Alumnos:
#	-Main Cerezo Asahel Said
#	-Reyes López Eduardo Alfonso

import csv
import os.path
from airport import Airport

airports_list = []

#Funcion getCities. Lee el archivo csv y a partir de él
#devuelve un diccionario
#en la que las llaves son las claves IATA de aeropuertos
#y los valores son objetos de tipo City
def getAirports():
    airports = {}

    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]

    #Se accede al archivo csv
    with open(parent_directory + '\dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) #Saltamos el primer renglón del archivo CSV 
        for row in reader:
            #Las primeras dos columnas del archivo corresponden a 
            #las claves iata de los aeropuertos. Asignamos estos valores
            #a dos variables
            iata_code1 = row[0]
            iata_code2 = row[1]

            #Revisamos primero si la ciudad ya está en el diccionario
            if iata_code1 not in airports:
                #Creamos un objeto de tipo ciudad con el nombre, latitud y longitud de la ciudad
                airport_object = Airport(row[0], row[2], row[3])
                #Guardamos la ciudad en el diccionario. La llave será la clave IATA y el valor el objeto
                #de tipo City
                airports[iata_code1] = airport_object
                airports_list.append(iata_code1)
            if iata_code2 not in airports:
                airport_object = Airport(row[1], row[4], row[5])
                airports[iata_code2] = airport_object
                airports_list.append(iata_code2)

    return airports

def get_airports_list():
    return airports_list
