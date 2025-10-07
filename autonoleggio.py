from operator import attrgetter
from noleggio import Noleggio
from automobile import Automobile

class Autonoleggio:

    #lista_automobili = []      ----> conviene mettere tutto dentro init, in questo caso comunque non sarebbe sbagliato

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""

        self.nome = nome
        self.responsabile = responsabile
        self.lista_automobili = []
        self.lista_noleggi = []

    def cambia_responsabile(self, nome_responsabile):
        self.responsabile = nome_responsabile   #Aggiorna direttamente l'attributo

    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""

        #Trasformo ciascuna riga del file in una lista di parametri
        #i quali vanno a diventare attributi del singolo oggetto automobile
        #ogni automobile viene poi aggiunta alla lista

        try:
            fileIn = open(file_path,"r",encoding="utf-8")
            for line in fileIn:
                parametri = line.strip().split(",")
                automobile = Automobile(parametri[0],parametri[1],parametri[2],parametri[3],parametri[4])
                self.lista_automobili.append(automobile)
            #return self.lista_automobili
            fileIn.close()

        except FileNotFoundError:
            print("File non esistente")

    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""

        #Inserisco una nuova automobile nella lista, inserendo il corretto ID
        #aumentando di 1 rispetto all'ultima presente

        automobile = Automobile(f"A{len(self.lista_automobili)+1}",marca,modello,anno,num_posti)
        self.lista_automobili.append(automobile)
        #return self.lista_automobili

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""

        #Uso attrgetter dalla libreria operator

        lista_ordinata = sorted(self.lista_automobili, key=attrgetter("Marca"))
        return lista_ordinata

    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""

        #Verifico due condizioni, che l'auto non sia già stata noleggiata
        #e che l'auto da noleggiare esista. Itero dunque sulla lista di noleggi cercando
        #l'id dell'auto e poi itero sulla lista di auto per accertare l'esistenza.
        #Uso dei cicli while insieme a dei flag.


        auto_disponibile = True
        k = 0
        while auto_disponibile == True and k<len(self.lista_noleggi):
            if self.lista_noleggi[k].id_automobile == id_automobile:
                auto_disponibile = False
                raise Exception("Auto non disponibile per il noleggio")
            k = k + 1


        auto_trovata = False
        i = 0
        while auto_trovata == False and i<len(self.lista_automobili):
            if self.lista_automobili[i].ID == id_automobile:
                auto_trovata = True
                id_nol = "N" + str(len(self.lista_noleggi) + 1)
                noleggio = Noleggio(id_nol, data, id_automobile, cognome_cliente)
                self.lista_noleggi.append(noleggio)
                return noleggio
            i = i+1

        if auto_trovata == False:
            raise Exception("Auto non presente")



    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""

        #Verifico che il noleggio in atto esista effettivamente e
        #lo rimuovo successivamente dalla lista dei noleggi

        noleggio_trovato = False
        j = 0
        while noleggio_trovato == False and j<len(self.lista_noleggi):
            for noleggio in self.lista_noleggi:
                if noleggio.id_noleggio == id_noleggio:
                    noleggio_trovato = True
                    self.lista_noleggi.remove(noleggio)
            j = j+1

        if noleggio_trovato == False:
            raise Exception("Noleggio non trovato")



