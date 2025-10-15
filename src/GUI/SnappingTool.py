import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QButtonGroup
from .captureButton import capture_button
from ..functions.screenCapture import screenshot_capture

class SnappingTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snipping Tool")
        self.setFixedSize(360,250)

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
                margin-top: 5px; 
                margin-bottom: 5px;
            }

            QPushButton.captureOption {
                background-color: transparent; 
                border: none; 
                padding: 0px; 
                min-width: 90px;
                max-width: 120px;
                min-height: 80px;
                text-align: center;
            }
            QPushButton.captureOption:hover {
                background-color: #4F4F4F;
            }
                           
            QPushButton.captureOption:checked { 
                background-color: #3C3C3C;
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

        layout.addWidget(self.select_component())

        screenshotButton = QPushButton("Take Screenshot")
        screenshotButton.setObjectName("takeScreenshotButton")
        screenshotButton.clicked.connect(lambda: screenshot_capture(self.get_selected_mode()))

        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(screenshotButton)
        buttonLayout.addStretch(1)

        layout.addLayout(buttonLayout)

        layout.addStretch(1)

    def get_selected_mode(self):
        if not self.captureButtonGroup:
            return "screen"
        
        checkedButton = self.captureButtonGroup.checkedButton()
        if checkedButton:
            buttonText = checkedButton.text().lower()

            if "screen" in buttonText:
                return "screen"
            elif "window" in buttonText:
                return "window"
            elif "selection" in buttonText:
                return "selection"
            
        return "screen"

    def select_component(self):
        section = QWidget()
        layout = QVBoxLayout(section)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)

        header = QLabel("Capture Area")
        header.setProperty("class", "sectionHeader")
        layout.addWidget(header)

        captureButtonLayout = QHBoxLayout()
        captureButtonLayout.setSpacing(10)

        self.captureButtonGroup = QButtonGroup(self)
        self.captureButtonGroup.setExclusive(True)

        btnScreen = capture_button("Screen", icon_path="../Assets/screen.png", ischecked=True)
        btnWindow = capture_button("Window", icon_path="../Assets/window.png")
        btnSelection = capture_button("Selection", icon_path="../Assets/selection.png")

        captureButtonLayout.addWidget(btnScreen)
        captureButtonLayout.addWidget(btnWindow)
        captureButtonLayout.addWidget(btnSelection)

        self.captureButtonGroup.addButton(btnScreen)
        self.captureButtonGroup.addButton(btnWindow)
        self.captureButtonGroup.addButton(btnSelection)

        layout.addLayout(captureButtonLayout)

        return section