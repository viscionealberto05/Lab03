from automobile import Automobile

class Autonoleggio:

    #lista_automobili = []

    def __init__(self, nome, responsabile,lista_automobili):
        """Inizializza gli attributi e le strutture dati"""

        self.nome = nome
        self.responsabile = responsabile
        self.lista_automobili = []

    def cambia_responsabile(self, nome_responsabile):
        self.responsabile = nome_responsabile

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""

        try:
            fileIn = open(file_path,"r",encoding="utf-8")
            for line in fileIn:
                parametri = line.strip().split(",")
                automobile = Automobile(parametri[0],parametri[1],parametri[2],parametri[3],parametri[4])
                Autonoleggio.lista_automobili.append(automobile)
            return Autonoleggio.lista_automobili
            fileIn.close()


        except FileNotFoundError:
            print("File non esistente")



    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""

        automobile = Automobile(f"A{len(Autonoleggio.lista_automobili)+1}",marca,modello,anno,num_posti)
        Autonoleggio.lista_automobili.append(automobile)
        return Autonoleggio.lista_automobili

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""
        # TODO

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        # TODO


    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        # TODO



