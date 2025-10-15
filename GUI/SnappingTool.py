import sys
from PyQt5.QtWidgets import QApplication, QWidget

class SnappingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snipping Tool")
        self.setFixedSize(300,250)

def main():
    app = QApplication(sys.argv)
    window = SnappingTool()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()