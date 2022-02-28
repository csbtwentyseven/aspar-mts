import firebasekurulum as fk

class Authentication:
    def __init__(self,eposta,sifre):
        self.eposta = eposta
        self.sifre = sifre

    def giris_yap(self):
        try:
            fk.FirebaseKurulum.auth.sign_in_with_email_and_password(self.eposta,self.sifre)
            return True
        except Exception as e:
            return False


