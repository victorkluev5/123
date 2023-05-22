import sys
from PyQt6.QtWidgets import *
import random
from PyQt6.QtCore import QTimer, Qt
from test_car import test_car
from PyQt6 import QtCore

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("окно")

        label_login = QLabel("Login:")
        self.login_edit = QLineEdit()
        label_password = QLabel("Password:")
        self.password_edit = QLineEdit()
        button_auth = QPushButton("Enter")
        button_exit = QPushButton("Exit")

        layout = QVBoxLayout()
        layout.addWidget(label_login)
        layout.addWidget(self.login_edit)
        layout.addWidget(label_password)
        layout.addWidget(self.password_edit)
        layout.addWidget(button_auth)
        layout.addWidget(button_exit)

        button_auth.clicked.connect(self.auth)
        button_exit.clicked.connect(self.exit)

        self.setLayout(layout)

        with open ('style.css') as style:
            self.setStyleSheet(style.read())

    def auth(self):
        if self.login_edit.text() == "user" and self.password_edit.text() == "user":
            self.okno = test_car()
            self.okno.show()
            self.close()

        else:
            self.test = Captcha()
            self.test.show()

    def exit(self):
        quit()

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(180,150)
        layout = QVBoxLayout()

        self.captcha = QLabel(str(random.randint(1000,9999)))
        self.captcha_edit = QLineEdit()
        self.label = QLabel("Каптча")
        self.captcha_btn = QPushButton("Проверить")
        self.timer_label = QLabel("Таймер: 10")
        self.count = 10
        self.timer_label.setText(str(self.count))
        self.timer = QTimer()

        layout.addWidget(self.label)
        layout.addWidget(self.captcha)
        layout.addWidget(self.captcha_btn)
        layout.addWidget(self.captcha_edit)
        layout.addWidget(self.timer_label)

        self.captcha_btn.clicked.connect(self.captcha_click)
        self.timer.timeout.connect(self.timer_tick)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        with open ('style.css') as style:
            self.setStyleSheet(style.read())

    def captcha_click(self):
        if self.captcha_edit.text() == self.captcha.text():
            QMessageBox.information(self, "Верно", "Верно")
            Captcha.close(self)
        else:
            self.captcha_edit.setDisabled(True)
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Ошибка")  

    def timer_tick(self):
        self.timer.start(1000)
        self.count -= 1
        self.timer_label.setText(str(self.count))

        if self.count == 0:
            self.timer.stop()
            self.captcha_edit.setDisabled(False)      

app= QApplication(sys.argv)
exe = Main()
exe.show()
app.exec()