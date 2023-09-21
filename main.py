from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from random import randint

app = QApplication([])

window = QWidget()
window.setWindowTitle('Визначити переможця')
window.resize(400,200)
window.show()


winner = QLabel('Натисни,щоб дізнатися переможця:')
answer = QLabel('?')

button = QPushButton('Згенерувати')

line = QVBoxLayout()

line.addWidget(winner,alignment=Qt.AlignCenter)
line.addWidget(answer,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)

window.setLayout(line)

def show_winner():
    num = randint(1,100)
    winner.setText('Переможець:')
    answer.setText(str(num))

button.clicked.connect(show_winner)

app.exec_()

