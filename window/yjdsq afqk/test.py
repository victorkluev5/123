import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication, QLabel, QLayout, QPushButton, QVBoxLayout, QMainWindow, QRadioButton, QLineEdit, QWidget, QStackedLayout, QHBoxLayout, QStackedWidget, QMessageBox
from sqlalchemy import text
# from settings import session
import random, string
from test1 import TestWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
#Переменные

        self.layout = QVBoxLayout()
        lbl = QLabel("Логин")
        # self.login = QLineEdit()
        self.login_edit = QLineEdit()
        # self.login.setPlaceholderText("Login")
        lbl2 = QLabel("Пароль")
        # self.password = QLineEdit()
        self.password_edit = QLineEdit()
        # self.password.setPlaceholderText("Password")
        btn_auth = QPushButton("Войти")
        btn_exit = QPushButton("Выйти")
       
#Добавление виджетов
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)
        self.layout.addWidget(lbl)
        # self.layout.addWidget(self.login)
        self.layout.addWidget(self.login_edit)
        self.layout.addWidget(lbl2)
        # self.layout.addWidget(self.password)
        self.layout.addWidget(self.password_edit)
        self.layout.addWidget(btn_auth)
        self.layout.addWidget(btn_exit)
       
#Подлючение кнопок
        btn_auth.clicked.connect(self.auth)
        btn_exit.clicked.connect(self.exit)
       
#Покделючение стиля

        with open ("style.css", "r") as css:
            widget.setStyleSheet(css.read())   
#Функционал кнопок

    def auth(self):
        # self.window = TestWindow()
        # self.sw = SecondWindow()
        if self.login_edit.text() == "user" and self.password_edit.text() == "user":
            self.okno = TestWindow()
            self.okno.show()
            self.close()

        # sql = text("select * from auth")
        # obj = session.execute(sql)
        # for row in obj:
        #     for login in row:
        #         for password in row:
        #                 if self.login.text() == login and self.password.text() == password:
        #                     self.window.show()
        #                     self.sw.close()
        #                 else:
        # self.okno.show()
        else:
            self.test = Captcha()
            self.test.show()

    def exit(self):
        quit()       
#второе окно

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(180,150)
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
            QMessageBox.information(self, "Верно", "Верно")
            self.close()
        else:

            self.timer = QTimer()
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_timeout)
            self.btn1.setEnabled(False)
            QMessageBox.critical(self, "Ошибка", "Ошибка")  

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

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()