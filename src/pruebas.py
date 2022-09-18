#Modelado y programación - Proyecto 01 
#Alumnos:
#	-Main Cerezo Asahel Said
#	-Reyes López Eduardo Alfonso

import readcsv
import classes

#Prueba para leer el cache
#Se imprimen todas las ciudades distintas del csv
print("CSV test: ")
print("")
try:
    myCities = readcsv.getCities()
    print("Cities: ")
    for key in myCities.keys():
        print(key, end = ' ')
except:
    print("Error reading csv file")

print("")

#Pruebas de requests para distintas ciudades 
print("-----------------")
print("Requests test: ")
print("")

try:
    if 'MEX' in myCities:
        city1 = myCities['MEX']
        weather_city1 = city1.get_weather()
        weather_list1 = weather_city1.get_attributes_as_list()
        print("MEX weather: ", end = '')
        print(weather_list1)
    else:
        print("MEX not found in myCities")   
except:
    print("Error making the request for MEX")

try:
    if 'CUN' in myCities:
        city2 = myCities['CUN']
        weather_city2 = city2.get_weather()
        weather_list2 = weather_city2.get_attributes_as_list()
        print("CUN weather: ", end = '')
        print(weather_list2)
    else:
        print("CUN not found in myCities")
except:
    print("Error making the request for CUN")

try:
    if 'TAM' in myCities:
        city3 = myCities['TAM']
        weather_city3 = city3.get_weather()
        weather_list3 = weather_city3.get_attributes_as_list()
        print("TAM weather: ", end = '')
        print(weather_list3)
    else:
        print("TAM not found in myCities")
except:
    print("Error making the request for TAM")

#Pruebas cache
print("-----------------")
print("Cache tests: ")
print("")

cache = {}
for i in range(3):
    if 'MEX' in myCities:
        if 'MEX' not in cache:
            print('MEX not in cache')
            city1 = myCities['MEX']
            weather_city1 = city1.get_weather()
            cache['MEX'] = weather_city1
            weather_list1 = weather_city1.get_attributes_as_list()
            print("MEX weather: ", end = '')
            print(weather_list1)
        else:
            print('MEX already in cache')
            weather_city1 = cache['MEX']
            weather_list1 = weather_city1.get_attributes_as_list()
            print("MEX weather: ", end = '')
            print(weather_list1)
    else:
        print("MEX not found in myCities")   
