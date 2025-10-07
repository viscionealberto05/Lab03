from automobile import Automobile
class Noleggio:
    def __init__(self, id_noleggio, data, id_automobile, cognome_cliente):
        self.id_noleggio = id_noleggio
        self.data = data
        self.id_automobile = id_automobile
        self.cognome_cliente = cognome_cliente

    def __str__(self):
        return f'Info Noleggio: {self.id_noleggio} - {self.id_automobile} - {self.cognome_cliente} in data: {self.data}'