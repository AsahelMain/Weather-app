import readcsv

myTickets = readcsv.getTickets()

for row in myTickets:
    row.get_data()