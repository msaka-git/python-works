"""
kendi yaptığım asansör programı
Bu program sınıf konusuna bulduğum kişisel ex.
Inheritance ı test etmek içinileride çift asansör (A ve B olmak üzere) tasarlayabilirsin.
"""

import time
import random
import sys

class asansör():

    def __init__(self, çağır="Çağırılıyor", kat=0, kişi=8, durum="Çalışıyor", marka="Schindler", yapım="1976"):

        self.kat=kat
        self.kişi=kişi
        self.durum=durum
        self.çağır=çağır
        self.marka=marka
        self.yapım=yapım

    def __str__(self):
        return ("Bu bir asansör simülasyon programıdır.")

    def kişi_durumu(self):
        kişi_üret = random.randint(0, 8)
        self.kişi=kişi_üret
        if (kişi_üret == 8):
            print("Asansör dolu")
            print("Şu anki kişi sayısı: ", kişi_üret)
            print("Abim ısrar etme binemezsin, bekle biraz")
            time.sleep(15)
        else:
            print("Asansör müsait")



    def bilgileri_göster(self):
        print("""
                Asaönsör özellikleri:

                Marka: {}

                En fazla kişi sayısı: {}

                Yapım Tarihi: {}

                Durum: {}

                """.format(self.marka, self.kişi, self.yapım, self.durum))


    def bin(self):
        print(self.çağır)
        asansör.kişi_durumu()
        rastgele = random.randint(0, 10)
        self.kat=rastgele
        print("Asansör şu katta: ", self.kat)
        kat_seç=int(input("Gideceğiniz katı girin: "))
        if (kat_seç == self.kat):
            print("Olmaz abi aynı kattasın")
        elif (kat_seç > self.kat):
            time.sleep(kat_seç - self.kat)
            print("çıktığınız kat: ", kat_seç)
        elif (kat_seç < self.kat):
            time.sleep(self.kat - kat_seç)
            print("indiğiniz kat: ", kat_seç)



asansör=asansör()

print("******************"
      "Lütfen işlem seçin:\n"
      "\n1- Asansöre bin\n"
      "\n2- Bilgileri göster\n"
      "******************")

while True:
    işlem=input("İşlem seç: ")

    if (işlem == "1"):
        asansör.bin()
    elif (işlem == "2"):
        asansör.bilgileri_göster()
