class Empty: #Klasa bazowa
	pass

class Tamagotchi(Empty): #Klasa pochodna
prog_nudy = 5 #Atrybut
prog_glodu = 10 #Atrybut

def __init__(self, imie #Argumenty): #Metoda,#Konstruktor
self.imie = imie #Instancja
self.slowa = ["Mmmmrrp", "Hrrp"] #Instancja
self.poziom_nudy = 0 #Instancja

burek = Tamagotchi("Burek") #Instancja
