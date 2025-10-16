import os
from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QSizePolicy, QMessageBox
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QDateTime
from PIL import Image
import pytesseract
from .ExtractTextViewDialog import TextExtractDialog
import os
from pathlib import Path

class SaveDialog(QDialog):
    def __init__(self, screenshotPath=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Save Screenshot")
        self.resize(650, 550)
        
        self.screenshotPath = screenshotPath
        self.originalPixmap = None

        self.setStyleSheet("""
            QDialog {
                background-color: #2e2e2e;
                color: #ffffff;
                font-family: "Segoe UI", "Roboto", "Arial";
                font-size: 10pt;
            }
            QPushButton {
                background-color: #4F4F4F;
                border: 1px solid #5F5F5F;
                border-radius: 4px;
                padding: 8px 15px;
                font-size: 10pt;
                color: #ffffff;
            }
            QPushButton:hover {
                background-color: #5A5A5A;
            }
            QPushButton#saveButton {
                background-color: #3AA05B;
                border: none;
            }
            QPushButton#saveButton:hover {
                background-color: #4CAF50;
            }
            QPushButton#cancelButton {
                background-color: #707070;
            }
            QPushButton#cancelButton:hover {
                background-color: #808080;
            }
            QLabel {
                color: #ffffff;
            }
            #previewLabel {
                background-color: #1a1a1a;
                border: 1px solid #5F5F5F;
                min-height: 250px; 
                max-height: 350px;
            }
        """)

        self.init_ui()
        self.load_screenshot_preview()

    
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        buttonLayout = QHBoxLayout()
        
        self.extractTextButton = QPushButton('Extract Text')
        self.extractTextButton.clicked.connect(self.extract_text)
        
        self.copyButton = QPushButton('Copy to Clipboard')
        self.copyButton.clicked.connect(self.copy_to_clipboard)
        
        self.saveButton = QPushButton('Save')
        self.saveButton.setObjectName('saveButton')
        self.saveButton.clicked.connect(self.save_screenshot)

        buttonLayout.addWidget(self.extractTextButton)
        buttonLayout.addWidget(self.copyButton)
        buttonLayout.addWidget(self.saveButton)

        layout.addLayout(buttonLayout)

        self.previewLabel = QLabel("Loading Screenshot...")
        self.previewLabel.setObjectName("previewLabel")
        self.previewLabel.setAlignment(Qt.AlignCenter)
        self.previewLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        layout.addWidget(self.previewLabel)
        
        layout.addStretch(1)


    def load_screenshot_preview(self):
        self.previewLabel.setText("No Screenshot Loaded")
        
        if self.screenshotPath and os.path.exists(self.screenshotPath):
            self.originalPixmap = QPixmap(self.screenshotPath)
            if not self.originalPixmap.isNull():
                self.display_pixmap(self.originalPixmap)
            else:
                self.previewLabel.setText("Failed to load screenshot from file.")
        
    def display_pixmap(self, pixmap):
        availableSize = self.previewLabel.size()
        
        scaled_pixmap = pixmap.scaled(
            availableSize, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        )
        self.previewLabel.setPixmap(scaled_pixmap)

    def resizeEvent(self, event):
        if self.originalPixmap and not self.originalPixmap.isNull():
            self.display_pixmap(self.originalPixmap)
        super().resizeEvent(event)

    def save_screenshot(self):
        if self.originalPixmap and not self.originalPixmap.isNull():
        
            picturesDir = Path.home() / "Pictures"
        
            targetDir = picturesDir / "Screenshots"

            try:
                targetDir.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                QMessageBox.critical(self, "Save Error", f"Failed to create directory: {targetDir}\nError: {e}")
                return
        
            timestamp = QDateTime.currentDateTime().toString('yyyy-MM-dd hh-mm-ss')
            fileName = f"Screenshot from {timestamp}.png"
            finalPath = str(targetDir / fileName)

            if self.originalPixmap.save(finalPath):
                QMessageBox.information(self, "Success", f"Screenshot saved to:\n{finalPath}")
                self.accept()
            else:
                QMessageBox.critical(self, "Save Error", f"Failed to save screenshot to:\n{finalPath}")
        else:
            QMessageBox.warning(self, "Error", "No screenshot available to save.")

    def copy_to_clipboard(self):
        if self.originalPixmap and not self.originalPixmap.isNull():
            QApplication.clipboard().setPixmap(self.originalPixmap)
            QMessageBox.information(self, "Copied", "Screenshot copied to clipboard!")
        else:
            QMessageBox.warning(self, "Error", "No screenshot to copy.")

    def extract_text(self):
        text = pytesseract.image_to_string(Image.open(self.screenshotPath))
        dialog = TextExtractDialog(extractText=text)
        dialog.exec_()