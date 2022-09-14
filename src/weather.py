from classes import Ticket
import readcsv

class Weather:
    cache = {}
    cities = []
    #La lista de todos los tickets
    myTickets = readcsv.getTickets()

    def get_cache(self):
        return self.cache

    def get_cities(self):
        return self.cities

    #Dado un ticket, se obtiene el clima de la ciudad de origen
    # y de destino, y se agregan al caché
    def get_weather(ticket):
        #Ciudad de origen
        origin_city = ticket.get_origin_city()
        #Ciudad de destino
        destination_city = ticket.get_destination_city()
        
        #Clima de la ciudad de origen
        my_weather_origin = ' '
        #Clima de la ciudad de llegada
        my_weather_destination = ' '

        #Si la ciudad ya está en el caché entonces ya no se hace otra request
        #sino que el clima será el valor que tiene la ciudad en el caché
        if origin_city in self.cache:
            my_weather_origin = self.cache[origin_city]
        else:
            #Se obtiene el clima de la ciudad de origen
            my_weather_origin = ticket.get_weather_origin()
            #Se guarda la ciudad y el clima en el caché 
            self.cache[origin_city] = my_weather_origin
            self.cities.append(origin_city)
        
        if destination_city in self.cache:
            my_weather_destination = self.cache[destination_city]
        else:
            my_weather_destination = ticket.get_weather_destination()
            self.cache[destination_city] = my_weather_destination
            self.cities.append(destination_city)

        return my_weather_origin, my_weather_destination

    #weather1, weather2 = get_weather(myTickets[2])

    def get_database(self):
        for ticket in self.myTickets:
            if ticket.get_origin_city() == 'origin':
                continue
            weather1, weather2 = get_weather(ticket)