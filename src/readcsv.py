import csv
from classes import City

#Funcion getCities. Lee el archivo csv y a partir de él
#devuelve un diccionario
#en la que las llaves son las claves IATA de aeropuertos
#y los valores son objetos de tipo City
def getCities():
    cities = {}

    #Se accede al archivo csv
    with open('dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            #Las primeras dos columnas del archivo corresponden a 
            #las claves iata de los aeropuertos. Asignamos estos valores
            #a dos variables
            city_name1 = row[0]
            city_name2 = row[1]

            #Revisamos primero si la ciudad ya está en el diccionario
            if city_name1 not in cities:
                #Creamos un objeto de tipo ciudad con el nombre, latitud y longitud de la ciudad
                city_object = City(row[0], row[2], row[3])
                #Guardamos la ciudad en el diccionario. La llave será la clave IATA y el valor el objeto
                #de tipo City
                cities[city_name1] = city_object
            if city_name2 not in cities:
                city_object = City(row[1], row[4], row[5])
                cities[city_name2] = city_object

    return cities
