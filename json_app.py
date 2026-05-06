from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QComboBox, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QLabel, QCheckBox, QHBoxLayout
import json

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setStyleSheet("font-size: 25px")

        self.v_main_lay = QVBoxLayout()
        self.h1_lay = QHBoxLayout()
        self.h2_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("Name")
        self.second = QLineEdit()
        self.second.setPlaceholderText("second")
        self.age = QLineEdit()
        self.age.setPlaceholderText("age")

        self.v_main_lay.addWidget(self.name)
        self.v_main_lay.addWidget(self.second)
        self.v_main_lay.addWidget(self.age)


        self.jins = QLabel("Jins")
        self.m = QRadioButton("M")
        self.f = QRadioButton("F")

        self.h1_lay.addWidget(self.jins)
        self.h1_lay.addWidget(self.m)
        self.h1_lay.addWidget(self.f)
        self.v_main_lay.addLayout(self.h1_lay)


        self.shahar = QLabel("Shahar")
        self.cmb = QComboBox()
        self.cmb.addItems(["Toshkent", "Namangan", "Farg'ona", "Samarqand"])
        self.cmb.activated[str].connect(self.viloyat)

        self.h2_lay.addWidget(self.shahar)
        self.h2_lay.addWidget(self.cmb)
        self.v_main_lay.addLayout(self.h2_lay)


        self.cmb2 = QComboBox()
        self.v_main_lay.addWidget(self.cmb2)

        self.btn_sub = QPushButton("submit")
        self.btn_sub.clicked.connect(self.submit)
        self.btn_exit = QPushButton("exit")
        self.btn_exit.clicked.connect(exit)


        self.h_btn_lay.addWidget(self.btn_sub)
        self.h_btn_lay.addWidget(self.btn_exit)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def viloyat(self, viloyat):
        self.cmb2.clear()

        if viloyat == "Toshkent":
            self.cmb2.addItems(["Olmazor", "Mirzo Ulug'bek", "Chilonzor", "Yunusobod", "Shayxontohur", "Yakkasaroy"])
        elif viloyat == "Namangan":
            self.cmb2.addItems(["Chust", "Pop", "Uychi", "Kosonsoy", "Mingbuloq", "Namangan"])
        elif viloyat == "Farg'ona":
            self.cmb2.addItems(["Marg'ilon", "Qo'qon", "Rishton", "Beshariq", "Dang'ara", "Oltiariq"])
        elif viloyat == "Samarqand":
            self.cmb2.addItems(["Urgut", "Kattaqo'rg'on", "Ishtixon", "Jomboy", "Narpay", "Payariq"])

    def submit(self):
        if self.name and self.age and self.second and self.m and self.f and self.cmb and self.cmb2:
            ism = self.name.text()
            familiya = self.second.text()
            yosh = int(self.age.text())
            if self.m.isChecked():
                jins = "Erkak"
            else:
                jins = "Ayol"
            viloyat = self.cmb.currentText()
            tuman = self.cmb2.currentText()

            data = {
                "ism": ism,
                "familiya": familiya,
                "yosh": yosh,
                "jins": jins,
                "viloyat": viloyat,
                "tuman": tuman
            }

            f = open("malumot.json", "w", encoding="utf-8")
            json.dump(data, f, indent=4)
            f.close()

            self.name.clear()
            self.second.clear()
            self.age.clear()
            self.cmb.clear()
            self.cmb2.clear()

            self.msg = QMessageBox()
            self.msg.setText("Ma'lumotlar qo'shildi.")
            self.msg.setIcon(QMessageBox.Information)
            self.msg.exec_()
            

        else:
            self.msg = QMessageBox()
            self.msg.setText("Hamma maydonni toldirish shart!")
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.exec_()


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
