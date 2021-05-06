from PyQt5.QtWidgets import QInputDialog, QApplication,QMessageBox, QMainWindow, QPushButton, QLabel, QDialog, QWidget, QTextEdit, QGridLayout, QAction, QFontComboBox,QColorDialog,QSpinBox,QMenuBar,QToolBox,QFileDialog
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtGui import QFont
import webbrowser


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = " Text Editor"
        self.left = 120
        self.top = 50
        self.width = 1000
        self.height = 600
        self.titleIcon = "photo/title.jpg"   
        sshFile="style.css"
        with open(sshFile,"r") as fh:
           self.setStyleSheet(fh.read())

                  

        self.EkranBas()
        self.aracKutulari()
        

    def EkranBas(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.titleIcon))
        

    
  
  
    def aracKutulari(self):
    # Renk seçme alanı
        self.renk = QPushButton()
        self.renk.setIcon(QtGui.QIcon("photo/renk.png"))
        self.renk.setFixedSize(40, 20)
        self.renk.clicked.connect(self.renkSec)
        self.renk.setToolTip("<h2>Renk Seç</h2>")

    # Yazı tipi seçme kutusu
        self.fontTip = QFontComboBox()
        self.fontTip.activated.connect(self.yaziTipi)
        self.fontTip.setFixedSize(120,20)
      
    # Yazı boyutu ayarları

        self.yaziBoyutu = QSpinBox()
        self.yaziBoyutu.valueChanged.connect(self.yaziBoyutuAyarla)
        self.yaziBoyutu.setFixedSize(40,20)

    # Araç çubukları
        self.kalinYaz = QPushButton()
        self.kalinYaz.setIcon(QtGui.QIcon("photo/kalin.png"))
        self.kalinYaz.setFixedSize(40, 20)
        self.kalinYaz.setToolTip("<h2>Kalın Yazı</h2>")
        self.kalinYaz.clicked.connect(self.kalinYaziYaz)
        self.yatayYaz = QPushButton()
        self.yatayYaz.setIcon(QtGui.QIcon("photo/yatay.png"))
        self.yatayYaz.setFixedSize(40, 20)
        self.yatayYaz.setToolTip("<h2>Yatay Yazı</h2>")
        self.yatayYaz.clicked.connect(self.yatayYaziYaz)
        self.altiCiziliYaz = QPushButton()
        self.altiCiziliYaz.setIcon(QtGui.QIcon("photo/alticizili.png"))
        self.altiCiziliYaz.setFixedSize(40, 20)
        self.altiCiziliYaz.setToolTip("<h2>Altı Çizili Yazı</h2>")
        self.altiCiziliYaz.clicked.connect(self.altiCiziliYaziYaz)
        self.solaYasla = QPushButton()
        self.solaYasla.setIcon(QtGui.QIcon("photo/solayasla.png"))
        self.solaYasla.setFixedSize(40, 20)
        self.solaYasla.setToolTip("<h2>Sola Yasla</h2>")
        self.solaYasla.clicked.connect(self.solaYaslaEvent)
        self.ortala = QPushButton()
        self.ortala.setIcon(QtGui.QIcon("photo/ortala.png"))
        self.ortala.setFixedSize(40, 20)
        self.ortala.setToolTip("<h2>Ortala</h2>")
        self.ortala.clicked.connect(self.ortalaEvent)
        self.sagaYasla = QPushButton()
        self.sagaYasla.setIcon(QtGui.QIcon("photo/sagayasla.png"))
        self.sagaYasla.setFixedSize(40, 20)
        self.sagaYasla.setToolTip("<h2>Sağa Yasla</h2>")
        self.sagaYasla.clicked.connect(self.sagaYaslaEvent)
        self.ikiYanaYasla = QPushButton()
        self.ikiYanaYasla.setIcon(QtGui.QIcon("photo/ikiyanayasla.png"))
        self.ikiYanaYasla.setFixedSize(40, 20)
        self.ikiYanaYasla.setToolTip("<h2>İki Yana Yasla</h2>")      
        self.ikiYanaYasla.clicked.connect(self.ikiYanaYaslaEvent)
        self.kaydetButon = QPushButton()
        self.kaydetButon.setIcon(QtGui.QIcon("photo/kaydet.png"))
        self.kaydetButon.setFixedSize(40,20)
        self.kaydetButon.setToolTip("<h2>Kaydet</h2>")
        self.kaydetButon.clicked.connect(self.dosyaKaydet_event)
        self.dosyaAc = QPushButton()
        self.dosyaAc.setIcon(QtGui.QIcon("photo/open.png"))
        self.dosyaAc.setFixedSize(40,20)
        self.dosyaAc.setToolTip("<h2>Dosya aç</h2>")
        self.dosyaAc.clicked.connect(self.dosyaAc_event)
        icon1 = QPushButton()
        icon1.setIcon(QtGui.QIcon("photo/icon1.png"))
        icon1.setFixedSize(40,20)
        icon2 = QPushButton()
        icon2.setIcon(QtGui.QIcon("photo/icon2.png"))
        icon2.setFixedSize(40,20)
        icon3 = QPushButton()
        icon3.setIcon(QtGui.QIcon("photo/icon3.png"))
        icon3.setFixedSize(40,20)
        icon4 = QPushButton()
        icon4.setIcon(QtGui.QIcon("photo/icon4.png"))
        icon4.setFixedSize(40,20)
        icon5 = QPushButton()
        icon5.setIcon(QtGui.QIcon("photo/icon5.png"))
        icon5.setFixedSize(40,20)
        icon6 = QPushButton()
        icon6.setIcon(QtGui.QIcon("photo/icon6.png"))
        icon6.setFixedSize(40,20)
        icon7 = QPushButton()
        icon7.setIcon(QtGui.QIcon("photo/icon7.png"))
        icon7.setFixedSize(40,20)
        icon8 = QPushButton()
        icon8.setIcon(QtGui.QIcon("photo/icon8.png"))
        icon8.setFixedSize(40,20)
        baslik = QPushButton()
        baslik.setStyleSheet("background-image : url(photo/baslik.jpg)")
        baslik.setFixedSize(400,40)
        baslik.clicked.connect(self.linkeGit)
        baslik.setToolTip("GitHub'ta gör :)")
   
        self.metinAlani = QTextEdit()
        
        layoutBas = QGridLayout()
        layoutBas.addWidget(self.renk, 0,0)
        layoutBas.addWidget(self.fontTip, 0,1)
        layoutBas.addWidget(self.yaziBoyutu,0,2)
        layoutBas.addWidget(self.kalinYaz, 1, 0)
        layoutBas.addWidget(self.yatayYaz, 2, 0)
        layoutBas.addWidget(self.altiCiziliYaz, 3, 0)
        layoutBas.addWidget(self.solaYasla, 4, 0)
        layoutBas.addWidget(self.ortala,5, 0)
        layoutBas.addWidget(self.sagaYasla, 6, 0)
        layoutBas.addWidget(self.ikiYanaYasla, 7, 0)
        layoutBas.addWidget(self.kaydetButon,0,10)
        layoutBas.addWidget(self.dosyaAc,0,9)
        layoutBas.addWidget(self.metinAlani, 1, 1,15,10)
        layoutBas.addWidget(baslik,0,5)
        layoutBas.addWidget(icon1, 8, 0)
        layoutBas.addWidget(icon2, 9, 0)
        layoutBas.addWidget(icon3, 10, 0)
        layoutBas.addWidget(icon4, 11, 0)
        layoutBas.addWidget(icon5, 12, 0)
        layoutBas.addWidget(icon6, 13, 0)
        layoutBas.addWidget(icon7, 14, 0)
        layoutBas.addWidget(icon8, 15, 0)

       

        self.setLayout(layoutBas)

    def yaziTipi(self):
        self.metinAlani.setFont(self.fontTip.currentFont())
    
    def renkSec(self):        
        self.renk = QColorDialog.getColor()        
        self.metinAlani.setTextColor(self.renk)
    
    def yaziBoyutuAyarla(self):
        self.metinAlani.setFontPointSize(self.yaziBoyutu.value())        
    
    def kalinYaziYaz(self):
        self.metinAlani.setFontWeight(QFont.Bold)
        self.kalinYaz.setStyleSheet("background-color : #56aaff")
        
    
    def yatayYaziYaz(self):
        self.metinAlani.setFontItalic(True)
        self.yatayYaz.setStyleSheet("background-color : #56aaff")
      

    def altiCiziliYaziYaz(self):
        self.metinAlani.setFontUnderline(True)
        self.altiCiziliYaz.setStyleSheet("background-color : #56aaff")        

    def ortalaEvent(self):
        self.metinAlani.setAlignment(QtCore.Qt.AlignCenter)
        self.ortala.setStyleSheet("background-color : #56aaff")

    def solaYaslaEvent(self):
        self.metinAlani.setAlignment(QtCore.Qt.AlignLeft)
        self.solaYasla.setStyleSheet("background-color : #56aaff")
                              
    def sagaYaslaEvent(self):
        self.metinAlani.setAlignment(QtCore.Qt.AlignRight)
        self.sagaYasla.setStyleSheet("background-color : #56aaff")
    
    def ikiYanaYaslaEvent(self):
        self.metinAlani.setAlignment(QtCore.Qt.AlignJustify)
        self.ikiYanaYasla.setStyleSheet("background-color : #56aaff")

    def linkeGit(self):
        webbrowser.open("https://github.com/mfabank")
        
    def dosyaAc_event(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        if filename[0]:
            f = open(filename[0], 'r')
            with f:
               data = f.read()
               self.metinAlani.setText(data)
            
    def dosyaKaydet_event(self):
        try:
            fname = QFileDialog.getExistingDirectory(self, 'Open f', '/home')

            metin, onay = QInputDialog.getText(
                self, " Dosya Adı", "Dosya Adı:")

            metinuzantı, onay = QInputDialog.getText(
                self, " Dosya Uzantısı", "Dosya Uzantısı:")
            metinad = ""
            uzantıad = ""
            if onay == True:

                metinad = metin
                uzantıad = metinuzantı

            with open(fname+"/"+metinad+"."+uzantıad, 'w') as f:
                my_text = self.metinAlani.toPlainText()
                f.write(my_text)
            QMessageBox.about(self, "Durum", "Başarılı")
        except:
            QMessageBox.about(self, "Dosya Kaydedilirken Hata", "Tekrar Deneyin")
    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(App.exec())
