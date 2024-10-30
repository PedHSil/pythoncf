import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Meu Primeiro App com PySide6")
        self.setGeometry(100, 100, 300, 200)  # x, y, width, height

        button = QPushButton("Clique em mim!", self)
        button.clicked.connect(self.show_message)
        button.setGeometry(100, 80, 100, 30)  # x, y, width, height

    def show_message(self):
        QMessageBox.information(self, "Mensagem", "Você clicou no botão!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_app = MyApp()
    my_app.show()
    sys.exit(app.exec())
