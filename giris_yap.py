#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN HAZIRLANMISTIR.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLineEdit

import authentication
import tercih_sayfasi

class Ui_girisyap(object):
    def setupUi(self, girisyap):
        girisyap.setObjectName("girisyap")
        girisyap.resize(534, 687)
        girisyap.setStyleSheet("border:0;")
        self.centralwidget = QtWidgets.QWidget(girisyap)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);border:0;")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 40, 431, 621))
        self.frame.setStyleSheet("border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.logo.setMinimumSize(QtCore.QSize(240, 100))
        self.logo.setMaximumSize(QtCore.QSize(240, 100))
        self.logo.setStyleSheet("border: 0\n"
"")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_3.addWidget(self.logo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.bilgilendirme_label = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.bilgilendirme_label.setMinimumSize(QtCore.QSize(0, 100))
        self.bilgilendirme_label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        self.bilgilendirme_label.setFont(font)
        self.bilgilendirme_label.setStyleSheet("color: rgb(4, 155, 224);\n"
"\n"
"border: 2px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:0px\n"
"\n"
"")
        self.bilgilendirme_label.setObjectName("bilgilendirme_label")
        self.verticalLayout.addWidget(self.bilgilendirme_label)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, -1, 20, -1)
        self.formLayout.setObjectName("formLayout")
        self.eposta_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.eposta_label.setFont(font)
        self.eposta_label.setStyleSheet("color: rgb(17, 124, 202);\n"
"border:0;")
        self.eposta_label.setObjectName("eposta_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.eposta_label)
        self.sifre_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.sifre_label.setFont(font)
        self.sifre_label.setStyleSheet("color: rgb(17, 124, 202);\n"
"border:0;")
        self.sifre_label.setObjectName("sifre_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.sifre_label)
        self.eposta_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.eposta_lineedit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.eposta_lineedit.setFont(font)
        self.eposta_lineedit.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.eposta_lineedit.setText("")
        self.eposta_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.eposta_lineedit.setObjectName("eposta_lineedit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.eposta_lineedit)
        self.sifre_lineedit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sifre_lineedit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.sifre_lineedit.setFont(font)
        self.sifre_lineedit.setStyleSheet("QLineEdit{\n"
"\n"
"border: 3px solid;\n"
"border-color:rgb(17, 124, 202);\n"
"border-radius:15px\n"
"\n"
"}")
        self.sifre_lineedit.setInputMask("")
        self.sifre_lineedit.setText("")
        self.sifre_lineedit.setAlignment(QtCore.Qt.AlignCenter)
        self.sifre_lineedit.setObjectName("sifre_lineedit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.sifre_lineedit)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.girisyap_buton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.girisyap_buton.setMinimumSize(QtCore.QSize(0, 100))
        self.girisyap_buton.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.girisyap_buton.setFont(font)
        self.girisyap_buton.setStyleSheet("QPushButton {\n"
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
        self.girisyap_buton.setObjectName("girisyap_buton")
        self.verticalLayout.addWidget(self.girisyap_buton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("border:0;\n"
"color: rgb(255, 0, 0);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        girisyap.setCentralWidget(self.centralwidget)

        self.pixmap = QPixmap('logo.jpg')

        self.retranslateUi(girisyap)
        QtCore.QMetaObject.connectSlotsByName(girisyap)

    def retranslateUi(self, girisyap):
        _translate = QtCore.QCoreApplication.translate
        girisyap.setWindowTitle(_translate("girisyap", "ASPARMTS - GİRİŞ YAP"))
        self.logo.setText(_translate("girisyap", "LOGO"))
        self.bilgilendirme_label.setHtml(_translate("girisyap", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto Black\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">ASPAR MÜŞTERİ TAKİP SİSTEMİ</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">LÜTFEN GİRİŞ YAPINIZ</span></p></body></html>"))
        self.eposta_label.setText(_translate("girisyap", "E-POSTA:"))
        self.sifre_label.setText(_translate("girisyap", "ŞİFRE:"))
        self.girisyap_buton.setText(_translate("girisyap", "GİRİŞ YAP"))

        self.sifre_lineedit.setEchoMode(QLineEdit.Password)
        self.logo.setPixmap(self.pixmap)


        self.girisyap_buton.clicked.connect(self.girisyap)

    def girisyap(self):
        eposta = self.eposta_lineedit.text()
        sifre = self.sifre_lineedit.text()
        auth = authentication.Authentication(eposta,sifre)

        try:
                if(auth.giris_yap()):
                        self.giris_basarili()

                else:
                        self.label.setText("Giriş Başarısız.")
                        print("Giris Basarisiz")
        except:
                self.label.setText("Lütfen İnternet Bağlantınızı Kontrol Ediniz.")

    def giris_basarili(self):
            self.window = QtWidgets.QMainWindow()
            self.ui = tercih_sayfasi.Ui_ASPARMTS()
            self.ui.setupUi(self.window)
            self.window.show()
            girisyap.close()


if __name__ == '__main__':
        import sys
        app = QtWidgets.QApplication(sys.argv)
        girisyap = QtWidgets.QMainWindow()
        ui = Ui_girisyap()
        ui.setupUi(girisyap)
        girisyap.show()
        sys.exit(app.exec_())

