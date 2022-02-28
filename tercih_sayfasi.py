#C.SAID BERK TARAFINDAN ASPAR ENERJI ICIN HAZIRLANMISTIR.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_ASPARMTS(object):
    def setupUi(self, ASPARMTS):
        ASPARMTS.setObjectName("ASPARMTS")
        ASPARMTS.resize(825, 620)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ASPARMTS.sizePolicy().hasHeightForWidth())
        ASPARMTS.setSizePolicy(sizePolicy)
        ASPARMTS.setMinimumSize(QtCore.QSize(825, 620))
        ASPARMTS.setMaximumSize(QtCore.QSize(825, 620))
        ASPARMTS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(ASPARMTS)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 160, 457, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QtCore.QSize(0, 100))
        self.logo.setMaximumSize(QtCore.QSize(16777215, 100))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.yeni_musteri_olustur_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yeni_musteri_olustur_label.sizePolicy().hasHeightForWidth())
        self.yeni_musteri_olustur_label.setSizePolicy(sizePolicy)
        self.yeni_musteri_olustur_label.setMinimumSize(QtCore.QSize(180, 100))
        self.yeni_musteri_olustur_label.setMaximumSize(QtCore.QSize(180, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.yeni_musteri_olustur_label.setFont(font)
        self.yeni_musteri_olustur_label.setObjectName("yeni_musteri_olustur_label")
        self.gridLayout.addWidget(self.yeni_musteri_olustur_label, 0, 0, 1, 1)
        self.yeni_musteri_olustur_buton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.yeni_musteri_olustur_buton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yeni_musteri_olustur_buton.sizePolicy().hasHeightForWidth())
        self.yeni_musteri_olustur_buton.setSizePolicy(sizePolicy)
        self.yeni_musteri_olustur_buton.setMinimumSize(QtCore.QSize(180, 94))
        self.yeni_musteri_olustur_buton.setMaximumSize(QtCore.QSize(180, 94))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.yeni_musteri_olustur_buton.setFont(font)
        self.yeni_musteri_olustur_buton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.yeni_musteri_olustur_buton.setAutoFillBackground(False)
        self.yeni_musteri_olustur_buton.setStyleSheet("QPushButton {\n"
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
        self.yeni_musteri_olustur_buton.setObjectName("yeni_musteri_olustur_buton")
        self.gridLayout.addWidget(self.yeni_musteri_olustur_buton, 1, 0, 1, 1)
        self.eldiven_ekle_buton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eldiven_ekle_buton.sizePolicy().hasHeightForWidth())
        self.eldiven_ekle_buton.setSizePolicy(sizePolicy)
        self.eldiven_ekle_buton.setMinimumSize(QtCore.QSize(180, 94))
        self.eldiven_ekle_buton.setMaximumSize(QtCore.QSize(180, 94))
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(12)
        self.eldiven_ekle_buton.setFont(font)
        self.eldiven_ekle_buton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.eldiven_ekle_buton.setAutoFillBackground(False)
        self.eldiven_ekle_buton.setStyleSheet("QPushButton {\n"
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
        self.eldiven_ekle_buton.setAutoDefault(False)
        self.eldiven_ekle_buton.setDefault(False)
        self.eldiven_ekle_buton.setFlat(True)
        self.eldiven_ekle_buton.setObjectName("eldiven_ekle_buton")
        self.gridLayout.addWidget(self.eldiven_ekle_buton, 1, 2, 1, 1)
        self.eldiven_ekle_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.eldiven_ekle_label.setFont(font)
        self.eldiven_ekle_label.setObjectName("eldiven_ekle_label")
        self.gridLayout.addWidget(self.eldiven_ekle_label, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        ASPARMTS.setCentralWidget(self.centralwidget)

        self.pixmap = QPixmap('logo.jpg')


        self.retranslateUi(ASPARMTS)
        QtCore.QMetaObject.connectSlotsByName(ASPARMTS)

    def retranslateUi(self, ASPARMTS):
        _translate = QtCore.QCoreApplication.translate
        ASPARMTS.setWindowTitle(_translate("ASPARMTS", "ASPAR MTS"))
        self.logo.setText(_translate("ASPARMTS", "logo"))
        self.yeni_musteri_olustur_label.setText(_translate("ASPARMTS", "Yeni Müşteri Oluştur"))
        self.yeni_musteri_olustur_buton.setText(_translate("ASPARMTS", "Yeni Müşteri "))
        self.eldiven_ekle_buton.setText(_translate("ASPARMTS", "Ürün Ekle"))
        self.eldiven_ekle_label.setText(_translate("ASPARMTS", "Müşteriye Ürün Ekle"))

        self.logo.setPixmap(self.pixmap)

        self.eldiven_ekle_buton.clicked.connect(self.urun_ekle)
        self.yeni_musteri_olustur_buton.clicked.connect(self.yeni_musteri)

    def urun_ekle(self):
        import urun_ekle
        self.window = QtWidgets.QMainWindow()
        self.ui = urun_ekle.Ui_UrunEkle()
        self.ui.setupUi(self.window)
        self.window.show()


    def yeni_musteri(self):
        import musteri_olustur
        self.window = QtWidgets.QMainWindow()
        self.ui = musteri_olustur.Ui_MusteriOlustur()
        self.ui.setupUi(self.window)
        self.window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ASPARMTS = QtWidgets.QMainWindow()
    ui = Ui_ASPARMTS()
    ui.setupUi(ASPARMTS)
    ASPARMTS.show()
    sys.exit(app.exec_())
