import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import (QApplication, QLabel, QLayout, 
                            QPushButton, QVBoxLayout, QMainWindow, QRadioButton, QLineEdit, QWidget, QStackedLayout, QHBoxLayout, QStackedWidget)
from sqlalchemy import text
from settings import session
import random, string


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
#Переменные

        self.layout = QVBoxLayout()
        lbl = QLabel("Логин")
        self.login = QLineEdit()
        self.login.setPlaceholderText("Login")
        lbl2 = QLabel("Пароль")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        btn_auth = QPushButton("Войти")
        btn_exit = QPushButton("Выйти")
       
#Добавление виджетов
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(lbl)
        self.layout.addWidget(self.login)
        self.layout.addWidget(lbl2)
        self.layout.addWidget(self.password)
        self.layout.addWidget(btn_auth)
        self.layout.addWidget(btn_exit)
       
#Подлючение кнопок
        btn_auth.clicked.connect(self.btn_auth)
        btn_exit.clicked.connect(self.btn_exit)
       
#Покделючение стиля

        with open ("style.css", "r") as css:
            widget.setStyleSheet(css.read())
       
    
#Функционал кнопок

    def btn_auth(self):
        self.window = TestWindow()
        self.sw = SecondWindow()
        sql = text("select * from auth")
        obj = session.execute(sql)
        for row in obj:
            for login in row:
                for password in row:
                        if self.login.text() == login and self.password.text() == password:
                            self.window.show()
                            self.sw.close()
                        else:
                            self.sw.show()

        
    def btn_exit(self):
        quit()
              
       
#второе окно

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
#Переменные
        len = 4
        captcha = string.ascii_uppercase + string.digits
        self.rnd_strings = ''.join(random.sample(captcha, len))
        layoy = QVBoxLayout()
        self.lbl = QLabel()
        self.kaptcha = QLineEdit()
        self.timer_lbl = QLabel("")
        self.btn1 = QPushButton("Проверить")
        self.lbl.setText(str(self.rnd_strings))
        
#Добавление виджетов
        widget = QWidget()
        widget.setLayout(layoy)
        self.setCentralWidget(widget)
        layoy.addWidget(self.lbl)
        layoy.addWidget(self.kaptcha)
        layoy.addWidget(self.timer_lbl)
        layoy.addWidget(self.btn1)
        
        
        self.btn1.clicked.connect(self.btn_ver)
        with open ("style.css", "r") as css:
            widget.setStyleSheet(css.read())
        
         
    def btn_ver(self):

        if self.kaptcha.text() == self.lbl.text():
            self.close()
        else:


            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_timeout)
            self.btn1.setEnabled(False)

            self.seconds = 10
            self.timer.start()



    def timer_timeout(self):
        self.seconds -= 1
        self.timer_lbl.setText(f"Осталось {self.seconds}")
        if self.seconds == 0:
            len = 4
            capthca = string.ascii_uppercase + string.digits
            rnd_string = ''.join(random.sample(capthca, len))
            self.timer.stop()
            self.timer_lbl.setText("")
            self.btn1.setEnabled(True)

            self.lbl.setText(str(rnd_string))

             
#третье окно
class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,150)

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

        lbl1 = QLabel("1.Что такое sigmod?")
        self.rb1 = QRadioButton(text="Функция активации")
        rb2 = QRadioButton(text="Что?")
        rb3 = QRadioButton(text="Прикольное слово)")
        vbox = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(vbox)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.rb1)
        vbox.addWidget(rb2)
        vbox.addWidget(rb3)

        lbl2 = QLabel("2.Основателем какой компании был Стив Джобс?")
        rb1_1 = QRadioButton(text="Fix Price")
        self.rb2_1 = QRadioButton(text="Apple")
        rb3_1 = QRadioButton(text="BMW")
        vbox2 = QVBoxLayout()
        widget2 = QWidget()
        widget2.setLayout(vbox2)
        vbox2.addWidget(lbl2)
        vbox2.addWidget(rb1_1)
        vbox2.addWidget(self.rb2_1)
        vbox2.addWidget(rb3_1)

        lbl3 = QLabel("3.Сколько будет 10-7?")
        self.rb1_2 = QRadioButton(text="3")
        rb2_2 = QRadioButton(text="0")
        rb3_2 = QRadioButton(text="21")
        vbox3 = QVBoxLayout()
        widget3 = QWidget()
        widget3.setLayout(vbox3)
        vbox3.addWidget(lbl3)
        vbox3.addWidget(self.rb1_2)
        vbox3.addWidget(rb2_2)
        vbox3.addWidget(rb3_2)

        lbl4 = QLabel("4.Сколько стоит бутылка воды?")
        rb1_3 = QRadioButton(text="0")
        rb2_3 = QRadioButton(text="Она бесплатная")
        self.rb3_3 = QRadioButton(text="100р")
        vbox4 = QVBoxLayout()
        widget4 = QWidget()
        widget4.setLayout(vbox4)
        vbox4.addWidget(lbl4)
        vbox4.addWidget(rb1_3)
        vbox4.addWidget(rb2_3)
        vbox4.addWidget(self.rb3_3)

        lbl5 = QLabel("5. Когда была выпущена первая серия питона?")
        rb1_4 = QRadioButton(text="1991г")
        self.rb2_4 = QRadioButton(text="Сегодня")
        rb3_4 = QRadioButton(text="5 лет назад")
        vbox5 = QVBoxLayout()
        widget5 = QWidget()
        widget5.setLayout(vbox5)
        vbox5.addWidget(lbl5)
        vbox5.addWidget(rb1_4)
        vbox5.addWidget(self.rb2_4)
        vbox5.addWidget(rb3_4)

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
        self.v6 = QLabel()
        self.v2 = QLabel()
        self.v3 = QLabel()
        self.v4 = QLabel()
        self.v5 = QLabel()
        self.res = QLabel()
        vbox7 = QVBoxLayout()
        widget7 = QWidget()
        widget7.setLayout(vbox7)
        vbox7.addWidget(lbl7)
        vbox7.addWidget(self.v6)
        vbox7.addWidget(self.v2)
        vbox7.addWidget(self.v3)
        vbox7.addWidget(self.v4)
        vbox7.addWidget(self.v5)
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

        self.stacklayout.addWidget(widget6)

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
        if self.rb1.isChecked():
            self.v6.setText("1.Верно")
            a = 1
        else:
            self.v6.setText("1.Не верно")
            a = 0
        if self.rb2_1.isChecked():
            self.v2.setText("2.Верно")
            b = a + 1
        else:
            self.v2.setText("2.Не верно")
            b = a
        if self.rb1_2.isChecked():
            self.v3.setText("3.Верно")
            t = b + 1
        else:
            self.v3.setText("3.Не верно")
            t = b
        if self.rb3_3.isChecked():
            self.v4.setText("4.Верно")
            d = t + 1
        else:
            self.v4.setText("4.Не верно")
            d = t
        if self.rb2_4.isChecked():
            self.v5.setText("5.Верно")
            self.e = d + 1
        else:
            self.v5.setText("5.Не верно")
            self.e = d

        self.setFixedSize(400, 200)
        self.res.setText(f"Ваш результат:{self.e}")
    def save(self):
        info = f"Фамилия и Имя:{self.edit.text()} \n"
        cour = f"Группа:{self.edit1.text()} \n"
        txt = f"Ваш результат:{self.v6.text()} \n"
        txt1 = f"Ваш результат:{self.v2.text()} \n"
        txt2 = f"Ваш результат:{self.v3.text()} \n"
        txt3 = f"Ваш результат:{self.v4.text()} \n"
        txt4 = f"Ваш результат:{self.v5.text()} \n"
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


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
