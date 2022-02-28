#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN HAZIRLANMISTIR.

import firebasekurulum as fk
import time

class Firestore:
    ana_veritabani_key = fk.FirebaseKurulum()
    db = ana_veritabani_key.firestore_erisim()

    def __init__(self,musteri_no = None, class_bilgisi = None, serino_liste = None, musteri_adi = None):
        self.musteri_no = musteri_no
        self.class_bilgisi = class_bilgisi
        self.serino_liste = serino_liste
        self.musteri_adi = musteri_adi

    def urun_ekle(self):

        if (self.musteri_no_kontrol(musteriNo=self.musteri_no) == False):
            musteri_noUYGUN = "{}".format(self.musteri_no)
            class_noUYGUN = "{}".format(self.class_bilgisi)

            yazilan_oge = 1
            for i in self.serino_liste:
                seri_noUYGUN = "{}".format(i)
                self.db.collection("Musteriler").document(musteri_noUYGUN).collection(class_noUYGUN).document(
                    seri_noUYGUN).set({"Seri No": "{}".format(seri_noUYGUN)})
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


if __name__ == '__main__':
    fs = Firestore()
    fs.musteri_no_kontrol("125")