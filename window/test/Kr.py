import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class Test(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(700,500)

        self.name = QLabel("Фио")
        self.edit_name = QLineEdit()
        self.course = QLabel("Группа")
        self.edit_course = QLineEdit()

        layout = QVBoxLayout()
        widget  = QWidget()

        widget.setLayout(layout)
        layout.addWidget(self.name)
        layout.addWidget(self.edit_name)
        layout.addWidget(self.course)
        layout.addWidget(self.edit_course)


        lbl1 = QLabel("Какого цвета зеленное яюлоко ?")
        btn1 = QRadioButton("Красное")
        btn2 = QRadioButton("Желтое")
        self.btn3 = QRadioButton("Зеленое")

        layout_1 = QVBoxLayout()
        widget_1 = QWidget()

        widget_1.setLayout(layout_1)
        layout_1.addWidget(lbl1)
        layout_1.addWidget(btn1)
        layout_1.addWidget(btn2)
        layout_1.addWidget(self.btn3 )


        lbl2 = QLabel("Какой длинны 20см линейка")
        btn2_1 = QRadioButton("20 см")
        self.btn2_2 = QRadioButton("22 см")
        btn2_3 = QRadioButton("15см")

        layout_2 = QVBoxLayout()
        widget_2 = QWidget()

        widget_2.setLayout(layout_2)
        layout_2.addWidget(lbl2)
        layout_2.addWidget(btn2_1)
        layout_2.addWidget(self.btn2_2)
        layout_2.addWidget(btn2_3)


        lbl3 = QLabel("Сколько букв в алфавите")
        btn3_1 = QRadioButton("34")
        self.btn3_2 = QRadioButton("33")
        btn3_3 = QRadioButton("32")

        layout_3 = QVBoxLayout()
        widget_3 = QWidget()

        widget_3.setLayout(layout_3)
        layout_3.addWidget(lbl3)
        layout_3.addWidget(btn3_1)
        layout_3.addWidget(self.btn3_2)
        layout_3.addWidget(btn3_3)

    

main = QApplication(sys.argv)
exe = Test()
exe.show()
main.exec()
