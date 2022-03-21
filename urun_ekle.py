#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN HAZIRLANMISTIR.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QButtonGroup

import firestore

class Ui_UrunEkle(object):
    def setupUi(self, EldivenEkle):
        EldivenEkle.setObjectName("EldivenEkle")
        EldivenEkle.resize(500, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EldivenEkle.sizePolicy().hasHeightForWidth())
        EldivenEkle.setSizePolicy(sizePolicy)
        EldivenEkle.setMinimumSize(QtCore.QSize(500, 600))
        EldivenEkle.setMaximumSize(QtCore.QSize(500, 600))
        EldivenEkle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(EldivenEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 20, 65, 100))
        self.logo.setObjectName("logo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 30, 391, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.musteri_numarasi_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.musteri_numarasi_label.setFont(font)
        self.musteri_numarasi_label.setObjectName("musteri_numarasi_label")
        self.horizontalLayout.addWidget(self.musteri_numarasi_label)
        self.musteri_numarasi_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.musteri_numarasi_line.setFont(font)
        self.musteri_numarasi_line.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:30px;\n"
"\n"
"}")
        self.musteri_numarasi_line.setText("")
        self.musteri_numarasi_line.setAlignment(QtCore.Qt.AlignCenter)
        self.musteri_numarasi_line.setObjectName("musteri_numarasi_line")
        self.horizontalLayout.addWidget(self.musteri_numarasi_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("border: 3px solid;\n"
"border-color:#049BE0;\n"
"border-radius:15px")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_standart = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_standart.setFont(font)
        self.radioButton_standart.setObjectName("radioButton_standart")
        self.horizontalLayout_2.addWidget(self.radioButton_standart)
        self.radioButton_arc = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_arc.setFont(font)
        self.radioButton_arc.setObjectName("radioButton_arc")
        self.horizontalLayout_2.addWidget(self.radioButton_arc)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.serni_numara_kaydet_buton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.serni_numara_kaydet_buton.setMinimumSize(QtCore.QSize(0, 75))
        self.serni_numara_kaydet_buton.setMaximumSize(QtCore.QSize(16777215, 75))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.serni_numara_kaydet_buton.setFont(font)
        self.serni_numara_kaydet_buton.setStyleSheet("QPushButton {\n"
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
        self.serni_numara_kaydet_buton.setObjectName("serni_numara_kaydet_buton")
        self.verticalLayout.addWidget(self.serni_numara_kaydet_buton)
        self.bilgilendirme_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bilgilendirme_label.setFont(font)
        self.bilgilendirme_label.setText("")
        self.bilgilendirme_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bilgilendirme_label.setObjectName("bilgilendirme_label")
        self.verticalLayout.addWidget(self.bilgilendirme_label)
        EldivenEkle.setCentralWidget(self.centralwidget)

        self.pixmap = QPixmap('logo_kucuk.jpg')
        self.classGrup = QButtonGroup(EldivenEkle)
        self.standartArcGrup = QButtonGroup(EldivenEkle)

        self.classGrup.addButton(self.radioButton)
        self.classGrup.addButton(self.radioButton_2)
        self.classGrup.addButton(self.radioButton_3)

        self.standartArcGrup.addButton(self.radioButton_standart)
        self.standartArcGrup.addButton(self.radioButton_arc)

        self.retranslateUi(EldivenEkle)
        QtCore.QMetaObject.connectSlotsByName(EldivenEkle)

    def urun_kaydet(self):
        radioStandartArcBilgi = self.standartarc_radioButonKontrol()
        radioClassBilgi = self.class_radioButonKontrol()
        serino_liste = self.plainTextEdit.toPlainText().strip().split("\n")
        musteri_no = self.musteri_numarasi_line.text()

        firestore_db = firestore.Firestore(musteri_no=musteri_no, class_bilgisi=radioClassBilgi, serino_liste=serino_liste, standart_arc=radioStandartArcBilgi)
        try:
            firestore_db.urun_ekle()
            self.bilgilendirme_label.setText("Ürün Ekleme Başarılı")
        except ValueError as hata:
            self.bilgilendirme_label.setText(str(hata))

    def class_radioButonKontrol(self):
        if (self.radioButton.isChecked()):
            return self.radioButton.text()

        elif (self.radioButton_2.isChecked()):
            return self.radioButton_2.text()

        elif (self.radioButton_3.isChecked()):
            return self.radioButton_3.text()

    def standartarc_radioButonKontrol(self):
        if (self.radioButton_standart.isChecked()):
            return self.radioButton_standart.text()

        elif (self.radioButton_arc.isChecked()):
            return self.radioButton_arc.text()


    def retranslateUi(self, EldivenEkle):
        _translate = QtCore.QCoreApplication.translate
        EldivenEkle.setWindowTitle(_translate("EldivenEkle", "Eldiven Ekle"))
        self.logo.setText(_translate("EldivenEkle", "logo"))
        self.musteri_numarasi_label.setText(_translate("EldivenEkle", "Müşteri Numarası: "))
        self.plainTextEdit.setPlaceholderText(_translate("EldivenEkle", "LÜTFEN SERİ NUMARALARINI ALT ALTA GELECEK ŞEKİLDE EKLEYİN"))
        self.radioButton.setText(_translate("EldivenEkle", "CLASS 0"))
        self.radioButton_2.setText(_translate("EldivenEkle", "CLASS 00"))
        self.radioButton_3.setText(_translate("EldivenEkle", "CLASS 4"))
        self.radioButton_standart.setText(_translate("EldivenEkle", "STANDART"))
        self.radioButton_arc.setText(_translate("EldivenEkle", "ARC"))
        self.serni_numara_kaydet_buton.setText(_translate("EldivenEkle", "Seri Numaralarını Kaydet"))

        self.logo.setPixmap(self.pixmap)

        self.serni_numara_kaydet_buton.clicked.connect(self.urun_kaydet)