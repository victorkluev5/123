import sys
from PyQt6.QtWidgets import *

class test_car(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Тест по выбору автомобиля")
        self.setFixedSize(400, 300)

        self.current_question = 0
        self.total_questions = 3
        self.answers = []

        self.label = QLabel()
        self.btn_next = []
        self.next_button = QPushButton("Далее")
        self.next_button.setDisabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        for i in range(4):
            radio_button = QRadioButton()
            radio_button.clicked.connect(self.enable_next_button)
            self.btn_next.append(radio_button)
            layout.addWidget(radio_button)

        layout.addWidget(self.next_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.questions = [
            {
                "question": "Какой тип автомобиля вы предпочитаете?",
                "answers": ["Седан", "Хэтчбек", "Внедорожник", "Купе"]
            },
            {
                "question": "Какой бюджет у вас на автомобиль?",
                "answers": ["До 300 000 руб", "300 000 руб - 700 000 руб", "700 000 руб - 1 000 000 руб", "Более 1 000 000 руб"]
            },
            {
                "question": "Какие опции вам необходимы?",
                "answers": ["Кондиционер", "Навигационная система", "Камера заднего вида", "Круиз-контроль"]
            }
        ]

        self.load_question(self.current_question)

        self.next_button.clicked.connect(self.next_question)

        with open ('style.css') as style:
            self.setStyleSheet(style.read())

    def load_question(self, question_index):
        self.label.setText(self.questions[question_index]["question"])
        answers = self.questions[question_index]["answers"]

        for i in range(4):
            if i < len(answers):
                self.btn_next[i].setText(answers[i])
                self.btn_next[i].setChecked(False)
                self.btn_next[i].setHidden(False)
            else:
                self.btn_next[i].setHidden(True)

    def enable_next_button(self):
        self.next_button.setDisabled(False)

    def next_question(self):
        self.answers.append(self.get_selected_answer())
        self.current_question += 1

        if self.current_question < self.total_questions:
            self.load_question(self.current_question)
            self.next_button.setDisabled(True)
        else:
            self.show_result()

    def get_selected_answer(self):
        for i in range(4):
            if self.btn_next[i].isChecked():
                return self.btn_next[i].text()

    def show_result(self):
        result = "Результаты:\n"
        for i in range(self.total_questions):
            result += f"Вопрос {i+1}: {self.questions[i]['question']}\n"
            result += f"Ответ: {self.answers[i]}\n\n"
        QMessageBox.information(self, "Результаты", result)
       
        with open('resultate.txt', 'w') as f: 
            resultat = [result] 
            f.writelines(resultat)