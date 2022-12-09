import requests
from tunnit import viikon_tunnit, viiden_paivan_tunnit

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()

def yksit_tunt(viiden_paivan_tunnit):
    paivan_tunnit = viiden_paivan_tunnit
    return paivan_tunnit



def tyotunnit(kokonaistunnit):
    tuntimaara = kokonaistunnit
    return tuntimaara



class Tekija:
    def __init__(self,tuntien_maara, paivan_tunnit, lisapisteet):
        self.tekijan_tunnit = tuntien_maara
        self.yksittaiset_tunnit = paivan_tunnit
        self.lisapisteet = lisapisteet



    def keskimaara(self):
        self.paivan_keskimaara = self.tekijan_tunnit / 5

    def tuntien_tulostaja(self):
        if self.tekijan_tunnit < 30:
            print("Tee enemmän töitä")
            print(self.tekijan_tunnit)
            print(f"Olet tehnyt keskimäärin {self.paivan_keskimaara} tuntia päivässä")
        elif self.tekijan_tunnit >= 30:
            for i in range(1):
                print("Kerronpa sinulle vitsin hyvän työn johdosta")
                print(vastaus["value"])
                print(self.tekijan_tunnit)
                print(f"Olet tehnyt keskimäärin {self.paivan_keskimaara} tuntia päivässä")

    def paiv_tunt_tulostus(self):
        for i in self.yksittaiset_tunnit:
            print(i)

    def tuntien_tarkastus(self):
        if self.yksittaiset_tunnit[0] + self.yksittaiset_tunnit[1] + self.yksittaiset_tunnit[2] + self.yksittaiset_tunnit[3] + self.yksittaiset_tunnit[4] == self.tekijan_tunnit:
           print("Hyvä. Et valehdellut tunneistasi, sinulle lisätään 1 lisäpiste")
           self.lisapisteet = self.lisapisteet + 1
        elif self.yksittaiset_tunnit[0] + self.yksittaiset_tunnit[1] + self.yksittaiset_tunnit[2] + self.yksittaiset_tunnit[3] + self.yksittaiset_tunnit[4] != self.tekijan_tunnit:
            print("Valehtelit tunneistasi, joten et saa lisäpisteitä")

    def yhteistulostus(self):
        for i in self.yksittaiset_tunnit:
            print(i)
        print(self.tekijan_tunnit)
        print(self.lisapisteet)





tekija_huubert = Tekija(tyotunnit(viikon_tunnit), yksit_tunt(viiden_paivan_tunnit), 0)

tekija_huubert.keskimaara()

tekija_huubert.tuntien_tulostaja()
tekija_huubert.paiv_tunt_tulostus()
tekija_huubert.tuntien_tarkastus()
tekija_huubert.yhteistulostus()




