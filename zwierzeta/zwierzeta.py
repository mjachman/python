import datetime
import re
now=datetime.datetime.now()
class Zwierze:
    def __init__(self, line):
        [self.rasa, self.imie, self.wiek] = line.split(",")
    def __str__(self):
        return "Rasa: " +self.rasa + "\n" +"Imie: " + self.imie +"\n" + "Wiek: " +  str(now.year-int(self.wiek)) + "\n"

class Kot(Zwierze):
    def __init__(self, line):
        self.l= len(re.findall(",", line))
        if self.l == 5:
            [self.rasa, self.imie, self.wiek,self.kolory,self.specjaly,self.cechy] = line.split(",")
        else:
            [self.rasa, self.imie, self.wiek, self.kolory, self.specjaly] = line.split(",")
    def __str__(self):
        if self.l==5:
            return Zwierze.__str__(self) + "Cechy szczególne: " + self.cechy + "\n" + "Kot ma następujące kolory: " "\n" + self.kolory.replace(" ","\n") + "\n" + "Kot lubi nastepujace specjaly: " + "\n" + self.specjaly.replace(" ","\n") +"\n"
        else:
            return Zwierze.__str__(
                self) + "Kot ma następujące kolory: " "\n" + self.kolory.replace(
                " ", "\n") + "\n" + "Kot lubi nastepujace specjaly: " + "\n" + self.specjaly.replace(" ", "\n") + "\n"

class Pies(Zwierze):
    def __init__(self, line):
        self.l = len(re.findall(",", line))
        if self.l == 5:
            [self.rasa, self.imie, self.wiek, self.siersc, self.glosnosc, self.cechy] = line.split(",")
        else:
            [self.rasa, self.imie, self.wiek, self.siersc, self.glosnosc] = line.split(",")
    def __str__(self):
        if self.l==5:
            return Zwierze.__str__(self) + "Cechy szegolne: " + self.cechy + "Charakterystyka siersci: " + self.siersc +  "\n" + "Glosnosc szkekania: " + self.glosnosc +"\n"
        else:
            return Zwierze.__str__(
                self) + "Charakterystyka siersci: " + self.siersc + "\n" + "Glosnosc szkekania: " + self.glosnosc + "\n"

class Zwierzeta:
    def __init__(self, lineList):
        self.animalList=[]
        for line in lineList:
            if re.match(r'Pies',line):
                self.animalList.append(Pies(line))
            else:
                self.animalList.append(Kot(line))
