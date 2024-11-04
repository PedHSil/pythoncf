from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        # conf. basica do layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)
        
        # titulo
        self.setWindowTitle('Calculadora(mude se precisar)')
        
    def adjustFixedSize(self):
        # não mexer no momento
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)