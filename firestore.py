#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN HAZIRLANMISTIR.
import datetime

import firebasekurulum as fk
import time

class Firestore:
    ana_veritabani_key = fk.FirebaseKurulum()
    db = ana_veritabani_key.firestore_erisim()

    def __init__(self,musteri_no = None, class_bilgisi = None, serino_liste = None, musteri_adi = None, standart_arc = None):
        self.musteri_no = musteri_no
        self.class_bilgisi = class_bilgisi
        self.serino_liste = serino_liste
        self.musteri_adi = musteri_adi
        self.standart_arc = standart_arc

    def urun_ekle(self):
        if (self.musteri_no_kontrol(musteriNo=self.musteri_no) == False):
            musteri_noUYGUN = "{}".format(self.musteri_no)
            class_noUYGUN = "{}".format(self.class_bilgisi)
            standart_arcUYGUN = "{}".format(self.standart_arc)

            tarih = datetime.datetime.now()
            gunAyYil = "{}.{}.{}".format(tarih.day, tarih.month, tarih.year)
            yazilan_oge = 1
            for i in self.serino_liste:
                seri_noUYGUN = "{}".format(i)
                self.db.collection("Musteriler").document(musteri_noUYGUN).collection(standart_arcUYGUN).document(class_noUYGUN).collection(seri_noUYGUN).document(seri_noUYGUN).set({"Seri No": "{}".format(seri_noUYGUN),"Basım Tarihi":"{}".format(gunAyYil)})
                print("{}/{} öge yazildi".format(yazilan_oge, len(self.serino_liste)))
                yazilan_oge = yazilan_oge + 1

        else:
            raise ValueError("Müşteri Numarası Kayıtlı Değil")



    def musteri_ekle(self):
        if(self.musteri_no_kontrol(musteriNo = self.musteri_no)):
            self.db.collection("Musteriler").document(self.musteri_no).set({"Müşteri Adı:":self.musteri_adi})
        else:
            raise ValueError("Müşteri No Zaten Var")

    def musteri_no_kontrol(self,musteriNo):
        self.kontrolcu = self.db.collection("Musteriler").get()
        for musteriler in self.kontrolcu:
            if(musteriler.id == musteriNo):
                return False
        return True