import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import subprocess
from datetime import datetime
import time
import os
import tempfile 
from PIL import Image

class ImageDisplayWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Captured Screenshot")
        self.layout = QVBoxLayout(self)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)
        
        self.load_image(image_path)
        
    def load_image(self, image_path):
        try:
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                self.image_label.setText("Error: Could not load image file.")
                return

            self.image_label.setPixmap(pixmap)
            self.resize(pixmap.size())
            
        except Exception as e:
            self.image_label.setText(f"An error occurred: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Snipping Tool")
        self.setGeometry(100, 100, 400, 250)
        self.image_window = None
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["fullscreen", "window", "area"])
        layout.addWidget(QLabel("Select Mode:"))
        layout.addWidget(self.mode_combo)
        
        self.status_label = QLabel("Ready.")
        layout.addWidget(self.status_label)

        button = QPushButton("Get Screen Shot and Open")
        button.clicked.connect(self.button_clicked_event)
        layout.addWidget(button)

    def button_clicked_event(self):
        mode = self.mode_combo.currentText()

        temp_dir = tempfile.gettempdir()
        temp_filename = os.path.join(temp_dir, f"screenshot_temp_{datetime.now()}.png")
        

        self.hide()
        time.sleep(0.3)

        cmd = ["gnome-screenshot", "-f", temp_filename]
            
        if mode == "window":
            cmd.append("-w")
        elif mode == "area":
            cmd.append("-a")
            
        subprocess.run(cmd, check=True)

        self.show()
        self.image_window = ImageDisplayWindow(temp_filename)
        print(temp_filename)
        self.image_window.show()

        # if os.path.exists(temp_filename):
                
        #     if self.image_window is not None:
        #         self.image_window.close()
        #         self.image_window = None
                
        #     self.image_window = ImageDisplayWindow(temp_filename)
        #     self.image_window.show()
                
        # else:
        #     self.status_label.setText("Operation cancelled or screenshot failed.")
            
        if os.path.exists(temp_filename):
                os.remove(temp_filename)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()