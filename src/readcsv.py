import csv
from classes import Ticket

#Funcion que regresa una lista de objetos ticket. Estos tickets se contruyen en base
#a la información que contiene el archivo csv 
def getTickets():
    tickets = []

    with open('dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_ticket = Ticket(row[0], row[1], row[2], row[3], row[4], row[5])
            tickets.append(new_ticket)

    return tickets