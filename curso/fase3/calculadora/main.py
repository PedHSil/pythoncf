import sys

from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH 

if __name__ == '__main__':
    try:
        # Cria a aplicação
        app = QApplication(sys.argv)
        window = MainWindow()

        # Define o ícone
        icon = QIcon(str(WINDOW_ICON_PATH))
        window.setWindowIcon(icon)
        app.setWindowIcon(icon)

        # Display
        display = Display()
        window.addToVLayout(display)

        # Executa tudo
        window.adjustFixedSize()
        window.show()

        sys.exit(app.exec())
    except Exception as e:
        print(f"An error occurred: {e}")
