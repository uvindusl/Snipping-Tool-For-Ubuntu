from PyQt5.QtWidgets import QApplication
from src.GUI.MainWindow import SnappingTool
import sys
from PyQt5 import QtGui

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('Assets/snappingtool.png'))
    window = SnappingTool()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()