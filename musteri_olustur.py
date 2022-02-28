#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN HAZIRLANMISTIR.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import firestore

class Ui_MusteriOlustur(object):
    def setupUi(self, MusteriOlustur):
        MusteriOlustur.setObjectName("MusteriOlustur")
        MusteriOlustur.resize(500, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MusteriOlustur.sizePolicy().hasHeightForWidth())
        MusteriOlustur.setSizePolicy(sizePolicy)
        MusteriOlustur.setMinimumSize(QtCore.QSize(500, 600))
        MusteriOlustur.setMaximumSize(QtCore.QSize(500, 600))
        MusteriOlustur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MusteriOlustur)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(140, 30, 358, 541))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.musteri_kurum_adi_info = QtWidgets.QLabel(self.formLayoutWidget)
        self.musteri_kurum_adi_info.setMinimumSize(QtCore.QSize(0, 100))
        self.musteri_kurum_adi_info.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.musteri_kurum_adi_info.setFont(font)
        self.musteri_kurum_adi_info.setAlignment(QtCore.Qt.AlignCenter)
        self.musteri_kurum_adi_info.setObjectName("musteri_kurum_adi_info")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.musteri_kurum_adi_info)
        self.musteri_kurum_adi_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.musteri_kurum_adi_lineedit.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.musteri_kurum_adi_lineedit.setFont(font)
        self.musteri_kurum_adi_lineedit.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.musteri_kurum_adi_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.musteri_kurum_adi_lineedit.setObjectName("musteri_kurum_adi_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.musteri_kurum_adi_lineedit)
        self.musteri_numarasi_info = QtWidgets.QLabel(self.formLayoutWidget)
        self.musteri_numarasi_info.setMinimumSize(QtCore.QSize(0, 100))
        self.musteri_numarasi_info.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.musteri_numarasi_info.setFont(font)
        self.musteri_numarasi_info.setAlignment(QtCore.Qt.AlignCenter)
        self.musteri_numarasi_info.setObjectName("musteri_numarasi_info")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.musteri_numarasi_info)
        self.musteri_numarasi_lineedit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.musteri_numarasi_lineedit.setMinimumSize(QtCore.QSize(0, 100))
        self.musteri_numarasi_lineedit.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.musteri_numarasi_lineedit.setFont(font)
        self.musteri_numarasi_lineedit.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.musteri_numarasi_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.musteri_numarasi_lineedit.setObjectName("musteri_numarasi_lineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.musteri_numarasi_lineedit)
        self.class00 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.class00.setFont(font)
        self.class00.setObjectName("class00")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.class00)
        self.class0 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.class0.setFont(font)
        self.class0.setObjectName("class0")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.class0)
        self.class4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.class4.setFont(font)
        self.class4.setObjectName("class4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.class4)
        self.kaydet_buton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.kaydet_buton.setMinimumSize(QtCore.QSize(0, 100))
        self.kaydet_buton.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.kaydet_buton.setFont(font)
        self.kaydet_buton.setStyleSheet("QPushButton {\n"
"color: rgb(4, 155, 224);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid;\n"
"border-color:#049BE0;\n"
"border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(4, 155, 224);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(62, 198, 247);\n"
"}")
        self.kaydet_buton.setObjectName("kaydet_buton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.kaydet_buton)
        self.bilgi_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bilgi_label.setFont(font)
        self.bilgi_label.setText("")
        self.bilgi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bilgi_label.setObjectName("bilgi_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.bilgi_label)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(30, 30, 65, 100))
        self.logo.setObjectName("logo")
        MusteriOlustur.setCentralWidget(self.centralwidget)

        self.pixmap = QPixmap('logo_kucuk.jpg')

        self.retranslateUi(MusteriOlustur)
        QtCore.QMetaObject.connectSlotsByName(MusteriOlustur)

    def retranslateUi(self, MusteriOlustur):
        _translate = QtCore.QCoreApplication.translate
        MusteriOlustur.setWindowTitle(_translate("MusteriOlustur", "Müşteri Oluştur"))
        self.musteri_kurum_adi_info.setText(_translate("MusteriOlustur", "Müşteri/Kurum Adı:"))
        self.musteri_numarasi_info.setText(_translate("MusteriOlustur", "Müşteri Numarası: "))
        self.class00.setText(_translate("MusteriOlustur", "CLASS 00"))
        self.class0.setText(_translate("MusteriOlustur", "CLASS 0"))
        self.class4.setText(_translate("MusteriOlustur", "CLASS 4"))
        self.kaydet_buton.setText(_translate("MusteriOlustur", "MÜŞTERİYİ KAYDET"))
        self.logo.setText(_translate("MusteriOlustur", "logo"))

        self.logo.setPixmap(self.pixmap)

        self.kaydet_buton.clicked.connect(self.musteri_kaydet)

    def musteri_kaydet(self):
        musteri_adi = self.musteri_kurum_adi_lineedit.text()
        musteri_numarasi = self.musteri_numarasi_lineedit.text()

        firestore_db = firestore.Firestore(musteri_no=musteri_numarasi, musteri_adi=musteri_adi)

        try:
            firestore_db.musteri_ekle()
            self.bilgi_label.setText("Müşteri Başarıyla Eklendi!")
        except ValueError as hata:
            self.bilgi_label.setText(str(hata))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusteriOlustur = QtWidgets.QMainWindow()
    ui = Ui_MusteriOlustur()
    ui.setupUi(MusteriOlustur)
    MusteriOlustur.show()
    sys.exit(app.exec_())
