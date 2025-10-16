from PyQt5.QtWidgets import QApplication, QDialog

class SaveDialog(QDialog):
    def __init__(self, screenshotPath, parent):
        super().__init__(parent)
        self.setWindowTitle("Save ScreenShot")
        self.resize(650, 550)

        self.screenshotPath = screenshotPath