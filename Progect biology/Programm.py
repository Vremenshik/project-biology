import random
import sys


from PyQt5 import QtCore, QtMultimedia
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QBrush, QPixmap


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./data/Desine/Zastavka.ui', self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Textures/Ночь.jpg")))
        self.setPalette(pal)
        self.label_2.resize(300, 300)
        self.pixmap = QPixmap('./data/Textures/Logo_comp.jpg')
        self.label_2.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.asd)
        self.load_mp3('./data/Musika/Ramires_Moria_-_V_mire_ZHivotnykh_72587234.mp3')
        self.player.play()

    def asd(self):
        uic.loadUi('./data/Desine/Main_menu.ui', self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Textures/Fi.jpg")))
        self.setPalette(pal)
        self.logo.resize(300, 300)
        self.pixmap = QPixmap('./data/Textures/Logo_comp.jpg')
        self.logo.setPixmap(self.pixmap)
        self.exit.clicked.connect(self.Exit)
        self.Vpered.clicked.connect(self.First)
        self.pushButton_2.clicked.connect(self.Sentinngs)
        self.load_mp3('./data/Musika/Ramires_Moria_-_V_mire_ZHivotnykh_72587234.mp3')
        self.player.play()



    def Two(self):
        uic.loadUi("./data/Desine/Firstui.ui", self)
        self.pushButton_2.clicked.connect(self.Three)
        self.pushButton.clicked.connect(self.Fail)
        self.pushButton_3.clicked.connect(self.Fail)
        self.pushButton_4.clicked.connect(self.Fail)

    def Three(self):
        uic.loadUi("./data/Desine/Tree.ui", self)
        self.pushButton_2.clicked.connect(self.all)
        self.pushButton.clicked.connect(self.Fail)
        self.pushButton_3.clicked.connect(self.Fail)
        self.pushButton_4.clicked.connect(self.Fail)

    def all(self):
        uic.loadUi("./data/Desine/untitled.ui", self)
        self.pushButton.clicked.connect(self.asd)

    def Sentinngs(self):
        uic.loadUi("./data/Desine/Sentinngs.ui", self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Textures/1200x900.jpg")))
        self.setPalette(pal)
        self.pushButton_2.clicked.connect(self.Troll)
        self.pushButton_3.clicked.connect(self.Titels)
        self.Nazad.clicked.connect(self.asd)

    def Titels(self):
        uic.loadUi("./data/Desine/Titles.ui", self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Textures/Ночь.jpg")))
        self.setPalette(pal)
        self.pushButton.clicked.connect(self.Sentinngs)
        self.load_mp3('./data/Musika/Titels.mp3')
        self.player.play()

    def Troll(self):
        uic.loadUi("./data/Desine/Troll.ui", self)
        pal = self.palette()
        pal.setBrush(QPalette.Normal, QPalette.Window, QBrush(QPixmap("./data/Textures/Donat.jpg")))
        self.setPalette(pal)
        self.pushButton.clicked.connect(self.Sentinngs)

    def First(self):
        uic.loadUi("./data/Desine/First.ui", self)
        self.label.resize(500, 500)
        self.pixmap = QPixmap('./data/Textures/get_file.png')
        self.label.setPixmap(self.pixmap)
        self.pushButton_3.clicked.connect(self.Fail)
        self.pushButton.clicked.connect(self.Fail)
        self.pushButton_2.clicked.connect(self.Fail)
        self.pushButton_4.clicked.connect(self.Two)

    def Fail(self):
        uic.loadUi("./data/Desine/Fail.ui", self)
        self.pushButton.clicked.connect(self.asd)


    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def Exit(self):
        uic.loadUi("./data/Desine/Exit.ui", self)
        self.Yes.clicked.connect(self.close())
        self.pushButton_2.clicked.connect(self.No_Exit)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
