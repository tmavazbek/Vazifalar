from random import choice
from datetime import datetime

class Dorixona:
    def __init__(self):
        self.royxat = [
            {
                "name": "Paratsetamol",
                "tannarx": 2500,
                "ogriq": "bosh og'riq",
                "srog": "2027-10-12",
                "soni": 50
            },
            {
                "name": "Ibuprofen",
                "tannarx": 8000,
                "ogriq": "Tish og'riq",
                "srog": "2026-05-20",
                "soni": 30
            }
        ]
        self.kassa = 5000
    def add_drug(self, name, tannarx, ogriq, srog, soni):
        self.royxat.append(
            {
                "name" : name, 
                "tannarx" : tannarx,
                "ogriq" : ogriq,
                "srog" : srog,
                "soni" : soni
            }
        )
    
    def sotmoq_name(self, name):
        for i in self.royxat:
            if name == i["name"]:
                if i["soni"] > 0:
                    i["soni"] -= 1
                    self.kassa += (2*i["tannarx"])
                    print(f"{i["name"]} sotildi, {i['soni']}ta qoldi\nKassa: {self.kassa} som")
                else:
                    print("Bunday dori qolmagan")
            
        
    def sotmoq_ogriq(self, ogriq):
        lst = []
        for i in self.royxat:
            if ogriq == i["ogriq"]:
                if i["soni"] > 0:
                    lst.append(i["name"])
        if lst != []:
            name = choice(lst)
            self.sotmoq_name(name)
        else:
            print(f"{ogriq} uchun dori mavjud emas")
    
    def utilizatsiya(self):
        for i in self.royxat:
            srog = [int(i) for i in i["srog"].split("-")]
            sana = datetime(srog[0], srog[1], srog[2])
            bugun = datetime(2026, 4, 22)
            if bugun > sana:
                self.royxat.remove(i)
                print(f'{i["name"]}ni surogi otgan\n')

dori = Dorixona()

# print(f"Dorilar: {dori.royxat}")
# print(f"Kassa: {dori.kassa}")

dori.add_drug("name", 1225, "tomoq ogriq", "2026-04-20", 10)
# print(f"Yangilangan dorilar: {dori.royxat}")

# print(dori.sotmoq_name("Paratsetamol"))
# print(dori.royxat)

# print(dori.sotmoq_ogriq("bosh og'riq"))

dori.utilizatsiya()
print(dori.royxat)

