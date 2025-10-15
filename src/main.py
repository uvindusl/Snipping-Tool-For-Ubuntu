from .GUI.SnappingTool import QApplication, SnappingTool
import sys

def main():
    app = QApplication(sys.argv)
    window = SnappingTool()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()