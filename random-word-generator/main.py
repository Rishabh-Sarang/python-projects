from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("myapp")
main_window.resize(444,222)

title = QLabel("random")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("click")
button2 = QPushButton("click")
button3 = QPushButton("click") 

my_words = ['asdf', 'wirb', 'ret', 'cxvb', 'fj']

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

def random_word1():
	word = choice(my_words)
	text1.setText(word)
def random_word2():
	word = choice(my_words)
	text2.setText(word)
def random_word3():
	word = choice(my_words)
	text3.setText(word)

button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

main_window.show()
app.exec_()
