from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h1_edit_lay = QHBoxLayout()
        self.h2_edit_lay = QHBoxLayout()
        self.h3_edit_lay = QHBoxLayout()
        self.h4_edit_lay = QHBoxLayout()
        self.h5_edit_lay = QHBoxLayout()

        self.lbl = QLabel("0")
        self.lbl.setStyleSheet("background: grey; font-size:25px")

        self.btn_on = QPushButton("On/Off")
        self.btn_on.clicked.connect(self.on)
        self.tep = True

        self.btn_bir = QPushButton("1")
        self.btn_bir.clicked.connect(self.bir)
        self.btn_ikki = QPushButton("2")
        self.btn_ikki.clicked.connect(self.ikki)
        self.btn_uch = QPushButton("3")
        self.btn_uch.clicked.connect(self.uch)
        self.btn_tort = QPushButton("4")
        self.btn_tort.clicked.connect(self.tort)
        self.btn_besh = QPushButton("5")
        self.btn_besh.clicked.connect(self.besh)
        self.btn_olti = QPushButton("6")
        self.btn_olti.clicked.connect(self.olti)
        self.btn_yetti = QPushButton("7")
        self.btn_yetti.clicked.connect(self.yetti)
        self.btn_sakkiz = QPushButton("8")
        self.btn_sakkiz.clicked.connect(self.sakkiz)
        self.btn_toqqiz = QPushButton("9")
        self.btn_toqqiz.clicked.connect(self.toqqiz)
        self.btn_nol = QPushButton("0")
        self.btn_nol.clicked.connect(self.nol)

        self.btn_qosh = QPushButton("+")
        self.btn_qosh.clicked.connect(self.qosh)
        self.btn_ayir = QPushButton("-")
        self.btn_ayir.clicked.connect(self.ayir)
        self.btn_kopay = QPushButton("*")
        self.btn_kopay.clicked.connect(self.kopay)
        self.btn_bol = QPushButton("/")
        self.btn_bol.clicked.connect(self.bol)

        self.btn_teng = QPushButton("=")
        self.btn_teng.clicked.connect(self.teng)
        self.btn_nuqta = QPushButton(".")
        self.btn_nuqta.clicked.connect(self.nuqta)

        self.btn_clear = QPushButton("Clear")
        self.btn_clear.clicked.connect(self.Clear)
        self.btn_back = QPushButton("<-")
        self.btn_back.clicked.connect(self.back)


        self.h1_edit_lay.addWidget(self.btn_clear)
        self.h1_edit_lay.addWidget(self.btn_back)
        self.h1_edit_lay.addWidget(self.btn_on)

        self.h2_edit_lay.addWidget(self.btn_yetti)
        self.h2_edit_lay.addWidget(self.btn_sakkiz)
        self.h2_edit_lay.addWidget(self.btn_toqqiz)
        self.h2_edit_lay.addWidget(self.btn_qosh)
        
        self.h3_edit_lay.addWidget(self.btn_tort)
        self.h3_edit_lay.addWidget(self.btn_besh)
        self.h3_edit_lay.addWidget(self.btn_olti)
        self.h3_edit_lay.addWidget(self.btn_ayir)

        self.h4_edit_lay.addWidget(self.btn_bir)
        self.h4_edit_lay.addWidget(self.btn_ikki)
        self.h4_edit_lay.addWidget(self.btn_uch)
        self.h4_edit_lay.addWidget(self.btn_kopay)
        
        self.h5_edit_lay.addWidget(self.btn_nuqta)
        self.h5_edit_lay.addWidget(self.btn_nol)
        self.h5_edit_lay.addWidget(self.btn_teng)
        self.h5_edit_lay.addWidget(self.btn_bol)

        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h1_edit_lay)
        self.v_main_lay.addLayout(self.h2_edit_lay)
        self.v_main_lay.addLayout(self.h3_edit_lay)
        self.v_main_lay.addLayout(self.h4_edit_lay)
        self.v_main_lay.addLayout(self.h5_edit_lay)

        self.setLayout(self.v_main_lay)

    def bir(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("1")
            else:
                self.lbl.setText(f"{numb}1")

    def ikki(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("2")
            else:
                self.lbl.setText(f"{numb}2")

    def uch(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("3")
            else:
                self.lbl.setText(f"{numb}3")

    def tort(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("4")
            else:
                self.lbl.setText(f"{numb}4")

    def besh(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("5")
            else:
                self.lbl.setText(f"{numb}5")

    def olti(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("6")
            else:
                self.lbl.setText(f"{numb}6")

    def yetti(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("7")
            else:
                self.lbl.setText(f"{numb}7")

    def sakkiz(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("8")
            else:
                self.lbl.setText(f"{numb}8")

    def toqqiz(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("9")
            else:
                self.lbl.setText(f"{numb}9")

    def nol(self):
        if self.tep:
            numb = self.lbl.text()
            if numb == "0":
                self.lbl.setText("0")
            else:
                self.lbl.setText(f"{numb}0")

    def qosh(self):
        if self.tep:
            numb = self.lbl.text()
            if numb and numb[-1] not in "+-*/":
                self.lbl.setText(f"{numb}+")
            elif numb and numb[-1] in "+-*/":
                self.lbl.setText(f"{numb[:-1]}+")
            if numb and numb[-1] in ".":
                self.lbl.setText(f"{numb}0+")

    def ayir(self):
        if self.tep:
            numb = self.lbl.text()
            if numb and numb[-1] not in "+-*/":
                self.lbl.setText(f"{numb}-")
            elif numb and numb[-1] in "+-*/":
                self.lbl.setText(f"{numb[:-1]}-")
            if numb and numb[-1] in ".":
                self.lbl.setText(f"{numb}0-")

    def kopay(self):
        if self.tep:
            numb = self.lbl.text()
            if numb and numb[-1] not in "+-*/":
                self.lbl.setText(f"{numb}*")
            elif numb and numb[-1] in "+-*/":
                self.lbl.setText(f"{numb[:-1]}*")
            if numb and numb[-1] in ".":
                self.lbl.setText(f"{numb}0*")

    def bol(self):
        if self.tep:
            numb = self.lbl.text()
            if numb and numb[-1] not in "+-*/":
                self.lbl.setText(f"{numb}/")
            elif numb and numb[-1] in "+-*/":
                self.lbl.setText(f"{numb[:-1]}/")
            if numb and numb[-1] in ".":
                self.lbl.setText(f"{numb}0/")

    def teng(self):
        if self.tep:
            numb = self.lbl.text()
            if numb and numb[-1] not in "+-*/":
                try:
                    natija = eval(numb)
                    self.lbl.setText(str(natija))
                except ZeroDivisionError:
                    self.lbl.setText("Nolga bo'lib bo'lmaydi!")
                except Exception:
                    self.lbl.setText("Xato!")

    def nuqta(self):
        if self.tep:
            numb = self.lbl.text()
            last_num = numb.split("+-*/")[-1]
            if "." not in last_num:
                if numb == "0":
                    self.lbl.setText("0.")
                else:
                    self.lbl.setText(f"{numb}.")
            if numb[-1] in "+-*/":
                self.lbl.setText(f"{numb}0.")
            else:
                self.lbl.setText(f"{numb}.")

    def back(self):
        if self.tep:
            numb = self.lbl.text()
            if not numb[-1].isdigit() and numb[-1] not in ".+-*/":
                self.lbl.setText("0")
                return
            if numb and numb != "0":
                self.lbl.setText(f"{numb[:-1:]}")
                if len(numb) == 1:
                    self.lbl.setText("0")

    def Clear(self):
        self.lbl.clear()
        self.lbl.setText("0")

    def on(self):
        if self.tep:
            self.lbl.clear()
            self.tep = False
        else:
            self.lbl.clear()
            self.lbl.setText("0")
            self.tep = True


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
