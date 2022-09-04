import csv
from classes import Ticket

def getTickets():
    tickets = []

    with open('dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nuevo_ticket = Ticket(row[0], row[1], row[2], row[3], row[4], row[5])
            tickets.append(nuevo_ticket)

    return tickets