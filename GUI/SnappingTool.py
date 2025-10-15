import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel

class SnappingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snipping Tool")
        self.setFixedSize(300,250)

        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: "Segoe UI", "Roboto", "Arial";
                font-size: 10pt;
            }
            QPushButton#takeScreenshotButton {
                background-color: #3AA05B; 
                border-radius: 6px;
                padding: 10px 20px;
                font-size: 10pt;
                min-width: 100px;
            }
            QPushButton#takeScreenshotButton:hover {
                background-color: #4CAF50; 
            }

            QLabel.sectionHeader {
                font-size: 11pt;
                font-weight: bold;
                margin-top: 15px;
                margin-bottom: 5px;
            }

            QPushButton.captureOption {
                background-color: #3C3C3C;
                border: 1px solid #555555;
                border-radius: 6px;
                padding: 10px 5px;
                min-width: 90px;
                max-width: 120px;
                min-height: 80px;
                text-align: center;
            }
            QPushButton.captureOption:hover {
                background-color: #4F4F4F;
            }
                           
            QPushButton.captureOption:checked { 
                background-color: #2F2F2F; 
            }
            QPushButton.captureOption QLabel {
                color: #ffffff;
                font-size: 9pt;
                padding-top: 5px;
            }
        """)

        self.ui()

    def ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(20)

        screenshotButton = QPushButton("Take Screenshot")
        screenshotButton.setObjectName("takeScreenshotButton")

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(screenshotButton)
        buttonLayout.addStretch(1)

        layout.addLayout(buttonLayout)

        layout.addStretch(1)

    def select_component(self):
        section = QWidget()
        layout = QVBoxLayout(section)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)

        header = QLabel("Capture Area")
        header.setProperty("class", "sectionHeader")
        layout.addWidget(header)

        capture_button_layout = QHBoxLayout()
        capture_button_layout.setSpacing(10)

        

def main():
    app = QApplication(sys.argv)
    window = SnappingTool()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()