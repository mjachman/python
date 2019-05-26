def czynnikiPierwsze(n):
    i = 2
    cp = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            cp.append(i)
    if n > 1:
        cp.append(n)
    return cp

def liczbaIWykladnik(l):
    x=czynnikiPierwsze(l)
    if x.count(czynnikiPierwsze(l)[0]) == len(x):
        y = [x[0], len(x)]
        return y

class ZlaPodstawa(Exception):
    def __str__(self):
        return "Proba utworzenia obiektu o podstawie <=0 i == 1"
class ZlyArgument(Exception):
    def __str__(self):
        return "Proba utworzenia obiektu o argumencie <=0 "
class RoznePodstawy(Exception):
    def __str__(self):
        return "Logarytmy maja rozne podstawy"
class Logarytm:
    def __init__(self, podstawa, argument):
        if podstawa <= 1:
            raise ZlaPodstawa()
        if argument <= 0:
            raise ZlyArgument()
class Logarytm:
    def __init__(self, podstawa,argument):
        self.podstawa = podstawa
        self.argument = argument
    def __add__(self,other):
        if self.podstawa==other.podstawa:
            self.argument = self.argument*other.argument
            return Logarytm(self.podstawa,self.argument)
        else:
            raise RoznePodstawy()
    def redukuj(self):
        if self.podstawa %1 !=0:
            raise TypeError("liczba niecałkowita w podstawie")
        elif liczbaIWykladnik(self.podstawa)[0] == liczbaIWykladnik(self.argument)[0]:
            y=liczbaIWykladnik(self.podstawa)[1]
            p=round(self.podstawa ** (1./y))
            a=round(self.argument ** (1./y))
            return Logarytm(p,a)
    def oblicz(self):
        if liczbaIWykladnik(self.podstawa)[0] == liczbaIWykladnik(self.argument)[0]:
            x=liczbaIWykladnik(self.podstawa)[1]
            y=liczbaIWykladnik(self.argument)[1]
            z=y/x
            return round(z)
    def __str__(self):
        return "log" + str(self.podstawa) + "(" + str(self.argument) + ")"

a=Logarytm(0,3)
b=Logarytm(5,5)
c=Logarytm(3,27)
d=Logarytm.oblicz(c)

print(d)