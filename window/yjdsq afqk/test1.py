from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
class TestWindow(QMainWindow):
    spisoc = []
    def __init__(self):
        super().__init__()
        self.setFixedSize(700,400)

        self.name = QLabel("Введите свое Имя и Фамилию")
        self.edit = QLineEdit()
        self.course = QLabel("Введите Группу")
        self.edit1 = QLineEdit()
        box = QVBoxLayout()
        wid = QWidget()
        wid.setLayout(box)
        box.addWidget(self.name)
        box.addWidget(self.edit)
        box.addWidget(self.course)

        box.addWidget(self.edit1)

        lbl1 = QLabel("Какой тип автомобиля имеет две двери?")
        rb1 = QRadioButton(text="Седан")
        rb2 = QRadioButton(text="Хэтчбек")
        self.rb3 = QRadioButton(text="Купе")

        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(self.rb3)
        

        lbl2 = QLabel("Это единственный советский автомобиль, который поставляли в Японию?")
        rb1_1 = QRadioButton(text="Зис-5")
        rb2_1 = QRadioButton(text="ГАЗ-М20 (победа)")
        self.rb3_1 = QRadioButton(text="НИВА ВАЗ-2121")
        vbox_2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox_2)
        vbox_2.addWidget(lbl2)
        vbox_2.addWidget(rb1_1)
        vbox_2.addWidget(rb2_1)
        vbox_2.addWidget(self.rb3_1)
   

        lbl3 = QLabel("У этого автомобиля омыватель лобового стекла работал от давления из запасного колеса, которое хранилось под капотом?")
        rb1_2 = QRadioButton(text="FORD ANGLIA 105E")
        rb2_2 = QRadioButton(text="FIAT 127")
        self.rb3_2 = QRadioButton(text="Volkswagen beetle")

        vbox_3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox_3)
        vbox_3.addWidget(lbl3)
        vbox_3.addWidget(rb1_2)
        vbox_3.addWidget(rb2_2)
        vbox_3.addWidget(self.rb3_2)


        lbl4 = QLabel("Кто является самым крупным автопроизводителем электрокаров?")
        rb1_3 = QRadioButton(text="Ё-мобиль")
        rb2_3 = QRadioButton(text="Toyota")
        self.rb3_3 = QRadioButton(text="Tesla")

        vbox_4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox_4)
        vbox_4.addWidget(lbl4)
        vbox_4.addWidget(rb1_3)
        vbox_4.addWidget(rb2_3)

        vbox_4.addWidget(self.rb3_3)

        lbl5 = QLabel("Этот автопроизводитель единственный, кто размещает зажигание слева от руля?")
        rb1_4 = QRadioButton(text="Volvo")
        self.rb2_4 = QRadioButton(text="Porshe")
        rb3_4 = QRadioButton(text="Zaz")
        vbox_5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox_5)
        vbox_5.addWidget(lbl5)
        vbox_5.addWidget(rb1_4)
        vbox_5.addWidget(self.rb2_4)
        vbox_5.addWidget(rb3_4)

        lbl6 = QLabel("Готовы увидеть свои результаты?")
        lbl6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        rb3_5 = QPushButton("Да")
        rb3_5.clicked.connect(self.activate_tab_v)
        rb3_5.clicked.connect(self.result)
        vbox6 = QVBoxLayout()
        widget6 = QWidget()
        widget6.setLayout(vbox6)
        vbox6.addWidget(lbl6)
        vbox6.addWidget(rb3_5)



        lbl7 = QLabel("Результаты теста:")
        self.otvet1 = QLabel()
        self.otvet2 = QLabel()
        self.otvet3 = QLabel()
        self.otvet4 = QLabel()
        self.otvet5 = QLabel()
        self.res = QLabel()
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addWidget(self.otvet1)
        vbox7.addWidget(self.otvet2)
        vbox7.addWidget(self.otvet3)
        vbox7.addWidget(self.otvet4)
        vbox7.addWidget(self.otvet5)
        vbox7.addWidget(self.res)
        btn_save = QPushButton("Сохранить")
        btn_save.clicked.connect(self.save)
        vbox7.addWidget(btn_save)


        pagelayout = QVBoxLayout()
        self.button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(self.stacklayout)
        pagelayout.addLayout(self.button_layout)

        self.btnb = QPushButton("back")
        self.btn = QPushButton("next")

        self.btnb.clicked.connect(self.activate_tab_b)
        self.btn.clicked.connect(self.activate_tab_v)

        self.stacklayout.addWidget(wid)
        self.button_layout.addWidget(self.btnb)
        self.button_layout.addWidget(self.btn)

        self.stacklayout.addWidget(widget)

        self.stacklayout.addWidget(widget2)

        self.stacklayout.addWidget(widget3)

        self.stacklayout.addWidget(widget4)

        self.stacklayout.addWidget(widget5)

        self.stacklayout.addWidget(widget7)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

        with open("style.css", "r") as css:
            self.setStyleSheet(css.read())

    def activate_tab_v(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()+1)

    def activate_tab_b(self):
        self.stacklayout.setCurrentIndex(self.stacklayout.currentIndex()-1)

    def result(self):
        if self.rb3.isChecked():
            self.otvet1.setText("1.Верно")
            a = 1
        else:
            self.otvet1.setText("1.Не верно")
            a = 0
        if self.rb3_1.isChecked():
            self.otvet2.setText("2.Верно")
            b = a + 1
        else:
            self.otvet2.setText("2.Не верно")
            b = a
        if self.rb3_2.isChecked():
            self.otvet3.setText("3.Верно")
            t = b + 1
        else:
            self.otvet3.setText("3.Не верно")
            t = b
        if self.rb3_3.isChecked():
            self.otvet4.setText("4.Верно")
            d = t + 1
        else:
            self.otvet4.setText("4.Не верно")
            d = t
        if self.rb2_4.isChecked():
            self.otvet5.setText("5.Верно")
            self.e = d + 1
        else:
            self.otvet5.setText("5.Не верно")
            self.e = d

        self.setFixedSize(400, 200)
        self.res.setText(f"Ваш результат:{self.e}")

    def save(self):
        info = f"Фамилия и Имя:{self.edit.text()} \n"
        cour = f"Группа:{self.edit1.text()} \n"
        txt = f"Ваш результат:{self.otvet1.text()} \n"
        txt1 = f"Ваш результат:{self.otvet2.text()} \n"
        txt2 = f"Ваш результат:{self.otvet3.text()} \n"
        txt3 = f"Ваш результат:{self.otvet4.text()} \n"
        txt4 = f"Ваш результат:{self.otvet5.text()} \n"
        txt5 = f"Ваш результат:{self.e} \n"

        with open("results.txt", "w", encoding="utf-8") as f:
            f.write(info)
            f.write(cour)
            f.write(txt)
            f.write(txt1)
            f.write(txt2)
            f.write(txt3)
            f.write(txt4)
            f.write(txt5)