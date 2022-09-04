class Ticket:
    origen = ''
    destino = ''
    lat_origen = ''
    long_origen = ''
    lat_destino = ''
    long_destino = ''

    def __init__(self, origen = '', destino = '', latO = '', longO = '', latD = '', longD = ''):
        self.origen = origen
        self.destino = destino
        self.lat_origen = latO
        self.long_origen = longO
        self.lat_destino = latD
        self.long_destino = longD

    def get_data(self):
        print(f'{self.origen}, {self.destino}, {self.lat_origen}, {self.long_origen}, {self.lat_destino}, {self.long_destino}')
