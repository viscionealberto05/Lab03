class Automobile:
    def __init__(self, ID, Marca, Modello, Anno_Immatricolazione, Numero_Posti):
        self.ID = ID
        self.Marca = Marca
        self.Modello = Modello
        self.Anno_Immatricolazione = Anno_Immatricolazione
        self.Numero_Posti = Numero_Posti

    def __str__(self):
        return f"ID:{self.ID}, Marca:{self.Marca}, Modello:{self.Modello}, Anno Immatricolazione:{self.Anno_Immatricolazione}, Numero Posti:{self.Numero_Posti}"