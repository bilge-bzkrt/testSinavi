import random
import sqlite3
import time
import sys

class TestSinaviUygulamasi:
    def __init__(self, name):
        self.name = name
        self.status = True
        self.score = 0
        #self.questions = questions
        #self.questionIndex = 0
        self.connectDatabase()

    def run(self):
        self.menu()

        choice = self.choice()

        if choice == 1:
            self.soruEkle()

        if choice == 2:
            self.soruSil()

        if choice == 3:
            self.SoruGuncelleme()

        if choice == 4:
            while True:
                try:
                    orderby = int(input("1-) Hepsi\n2-) Kategoriye Göre Filtrele\n\n Seçim: "))
                    if orderby < 1 or orderby > 3:
                        continue
                    break

                except ValueError:
                    print("Tamsayı Olmalı")
            self.butunSorulariGetir(orderby)

        if choice == 5:
            self.sinavaBasla()
            self.connect.close()


        if choice == 6:
            self.Cikis()


    def menu(self):
        print("********** {} Hoşgeldiniz **********".format(self.name))
        time.sleep(2)
        print("\n1-) Soru Ekle\n2-) Soru Sil\n3-) Soru Güncelle\n4-) Filtrele \n5-) Sınava Başla\n6-) Çıkış\n")

    def choice(self):
        while True:
            try:
                process = int(input("Seçim: "))
                if process < 1 or process > 6:
                    print("1 - 6 arasında bir tamsayı girilmeli.  ")
                    continue
                break
            except ValueError:
                print("operation is must be integer number.")

        return process

    def soruEkle(self):
        print("**** Soru Ekle ****")
        kategori = input("Kategori: ").lower().capitalize()
        soru = input("Soru: ").lower().capitalize()
        cevap1 = input("Cevap1: ").lower().capitalize()
        cevap2 = input("Cevap2: ").lower().capitalize()
        cevap3 = input("Cevap3: ").lower().capitalize()
        cevap4 = input("Cevap4: ").lower().capitalize()
        dogrucevap = input("dogrucevap: ").lower().capitalize()


        self.cursor.execute("INSERT INTO sinav VALUES('{}','{}','{}','{}','{}','{}','{}')".format(kategori, soru, cevap1,cevap2,cevap3,cevap4, dogrucevap))
        self.connect.commit()
        print("Soru Başarılı Bir Şekilde Eklendi ({})".format(soru))

    def soruSil(self):
        self.cursor.execute("SELECT * FROM sinav")
        butunSorular = self.cursor.fetchall()
        TumDegerleriStringeCevir = lambda x: [str(y) for y in x]
        for i, j in enumerate(butunSorular, 1):
            print("{}) {}".format(i, " ".join(TumDegerleriStringeCevir(j))))
        while True:
            try:
                select = int(input("Silmek İstediğiniz Soruyu Seçiniz: "))
                break
            except ValueError:
                print("Lütfen Soru Seçiniz (Tamsayı): ")

        self.cursor.execute("DELETE FROM sinav WHERE rowid={}".format(select))
        self.connect.commit()
        print("\nSoru Başarılı Bir Şekilde Silindi.")

    def SoruGuncelleme(self):
        self.cursor.execute("SELECT * FROM sinav")
        butunSorular = self.cursor.fetchall()
        TumDegerleriStringeCevir = lambda x: [str(y) for y in x]
        for i, j in enumerate(butunSorular, 1):
            print("{}) {}".format(i, " ".join(TumDegerleriStringeCevir(j))))
        while True:
            try:
                select = int(input("\nGüncellemek İstediğiniz Soruyu Seçiniz: "))
                break
            except ValueError:
                print("Lütfen Soru Seçiniz (Tamsayı): ")
        while True:
            try:
                guncellenecek = int(input("1-) Kategori\n2-) Soru\n3-) Dogrucevap\n\nSecim: "))
                if guncellenecek < 1 or guncellenecek > 3:
                    continue
                break
            except ValueError:
                print("Tamsayı Giriniz: ")

        islemler = ["kategori", "soru", "dogrucevap"]
        if guncellenecek > 1 or guncellenecek < 3:
            yeniDeger = input("Yeni Değeri Giriniz: ")
            self.cursor.execute(
                "UPDATE sinav SET '{}' = '{}' WHERE rowid={}".format(islemler[guncellenecek - 1], yeniDeger, select))
        self.connect.commit()
        print("Güncelleme Başarılı")

    def butunSorulariGetir(self, by):
        if by == 1:
            self.cursor.execute("SELECT * FROM sinav")
            butunSorular = self.cursor.fetchall()
            TumDegerleriStringeCevir = lambda x: [str(y) for y in x]
            for i, j in enumerate(butunSorular, 1):
                print("{}) {}".format(i, " ".join(TumDegerleriStringeCevir(j))))
        if by == 2:
            self.cursor.execute("SELECT kategori FROM sinav")
            fakulteler = list(enumerate(list(set(self.cursor.fetchall())), 1))
            for i, j in fakulteler:
                print("{} ) {}".format(i, j[0]))
            while True:
                try:
                    select = int(input("\nSeçim: "))
                    break
                except ValueError:
                    print("Tamsayı Gir: ")
            self.cursor.execute("SELECT * FROM sinav WHERE kategori = '{}'".format(fakulteler[select - 1][1][0]))
            butunSorular = self.cursor.fetchall()
            TumDegerleriStringeCevir = lambda x: [str(y) for y in x]
            for i, j in enumerate(butunSorular, 1):
                print("{}) {}".format(i, " ".join(TumDegerleriStringeCevir(j))))


    def sinavaBasla(self):
        print("Teste başlamak için bekleyiniz...")
        time.sleep(2)
        self.cursor.execute("SELECT * FROM sinav ")
        veriler = self.cursor.fetchmany(5)
        for veri in veriler:
            print("\nSoru: ", veri[1])
            print("- " , veri[2])
            print("- " , veri[3])
            print("- " , veri[4])
            print("- " , veri[5])
            cevap = input("Cevap: ").lower().capitalize()
            print("Cevabınız Değerlendiriliyor")
            for i in range(3, 0, -1):
                time.sleep(1)
                sys.stdout.write(str(i) + ' ')
                sys.stdout.flush()
            if cevap == veri[6]:
                self.score +=10
                print("\nCEVABINIZ DOĞRU")
            else:
                print("\nCEVABINIZ YANLIŞ")
        print("Puan : " + str(self.score))
        print("TEST BİTTİ")
        self.score = 0


    def Cikis(self):
        self.status = False

    def connectDatabase(self):
        self.connect = sqlite3.connect("veritabani.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS sinav( kategori TEXT,soru TEXT,cevap1 TEXT,cevap2 TEXT,cevap3 TEXT, cevap4 TEXT, dosgrucevap TEXT)")

        self.connect.commit()

test = TestSinaviUygulamasi("Test Sınavı Uygulamasına")

while test.status:
    test.run()