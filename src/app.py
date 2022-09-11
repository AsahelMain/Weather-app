from classes import Ticket, WeatherInfo
import readcsv

cache = {}
myTickets = readcsv.getTickets()

def get_weather(ticket: Ticket):
    origin_city = ticket.get_origin_city()
    destination_city = ticket.get_destination_city()
    my_weather_origin = ' '
    my_weather_destination = ' '

    if origin_city in cache:
        print(origin_city + ' already in cache')
        my_weather_origin = cache[origin_city]
    else:
        print(origin_city + " not in cache")
        my_weather_origin = ticket.get_weather_origin()
        cache[origin_city] = my_weather_origin
    
    if destination_city in cache:
        print(destination_city + ' already in cache')
        my_weather_destination = cache[destination_city]
    else:
        print(destination_city + " not in cache")
        my_weather_destination = ticket.get_weather_destination()
        cache[destination_city] = my_weather_destination
    
    return my_weather_origin, my_weather_destination

#Prueba1 - Pide el clima del ticket con indice 4 (ciudad de origen y de destino)

weather1, weather2 = get_weather(myTickets[4])
print("MTY: ", end=" ")
weather1.get_data()
print("MEX: ", end=" ")
weather2.get_data()

weather3, weather4 = get_weather(myTickets[4])
print("MTY: ", end=" ")
weather3.get_data()
print("MEX: ", end=" ")
weather4.get_data()


"""""
#Prueba-Pide el clima de todos los tickets(ciudad de origen y de destino)
for ticket in myTickets:
    if ticket.get_origin_city() == 'origin':
        continue
    weather1, weather2 = get_weather(ticket)
    weather1.get_data()
    weather2.get_data()
"""

