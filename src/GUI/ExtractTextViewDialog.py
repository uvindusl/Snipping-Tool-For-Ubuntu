from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, 
    QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt

class TextExtractDialog(QDialog):
    def __init__(self, extractText="", parent=None):
        super().__init__(parent)
        self.setWindowTitle("Extracted Text")
        self.resize(500, 400)
        self.extractText = extractText
        
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
            QPushButton#copyButton {
                background-color: #1E88E5; /* Blue tone */
                border: none;
            }
            QPushButton#copyButton:hover {
                background-color: #42A5F5;
            }
            QTextEdit {
                background-color: #1a1a1a;
                border: 1px solid #5F5F5F;
                color: #ffffff;
                padding: 10px;
            }
        """)
        
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        self.textEditor = QTextEdit()
        self.textEditor.setText(self.extractText)
        self.textEditor.setReadOnly(True)
        layout.addWidget(self.textEditor)
        
        buttonLayout = QHBoxLayout()
        self.copyButton = QPushButton("Copy Text")
        self.copyButton.setObjectName("copyButton")
        self.copyButton.clicked.connect(self.copy_text_to_clipboard)
        
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(self.copyButton)
        
        layout.addLayout(buttonLayout)
        
    def copy_text_to_clipboard(self):
        QApplication.clipboard().setText(self.extractText)
        QMessageBox.information(self, "Copied", "Extracted text copied to clipboard!")
        
