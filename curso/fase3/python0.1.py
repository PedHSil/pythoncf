import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)

button = QPushButton('Texto do botão')
button.setStyleSheet('font-size: 12px; font-weight: bold; color: #fff')
'''button.show()''' # add o widget na hierarquia e exibe a janela

button2 = QPushButton('Texto do botão2')
button2.setStyleSheet('font-size: 14px; font-weight: bold; color: #fff')
'''button2.show()'''

central_widget = QWidget()

layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(button)
layout.addWidget(button2)

central_widget.show()
app.exec() # loop da aplicação  