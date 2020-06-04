#Metoda super pozwala nam na odwolanie sie do metody klasy bazowej ( rodzica ) jesli Klasa pochodna zmienila wczesniej dzialanie tej metody

class Rodzic():

    def superfunkcja(self):
        print("abc")

class Dziecko(Rodzic):

    def superfunkcja(self):
        super().superfunkcja()
        print("xyz")

