import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QButtonGroup, QSizePolicy, QSpacerItem
)
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt, QSize

class ScreenshotToolUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot Options")
        
        # Set a fixed size appropriate for the simplified content
        self.setFixedSize(380, 250) 
        
        # --- QSS Styling for Dark Theme ---
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e; /* Dark background */
                color: #ffffff; /* White text */
                font-family: "Segoe UI", "Roboto", "Arial";
                font-size: 10pt;
            }
            /* Styling for the main action button */
            QPushButton#takeScreenshotButton {
                background-color: #3AA05B; /* Green */
                border-radius: 6px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12pt;
                min-width: 150px;
            }
            QPushButton#takeScreenshotButton:hover {
                background-color: #4CAF50; 
            }

            /* Section headers */
            QLabel.sectionHeader {
                font-size: 11pt;
                font-weight: bold;
                margin-top: 15px;
                margin-bottom: 5px;
            }

            /* Capture Area Buttons (Screen, Window, Selection) */
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
            /* Highlight style for the selected option */
            QPushButton.captureOption:checked { 
                background-color: #2F2F2F; 
                border: 2px solid #6c5ce7; /* Purple border */
            }
            QPushButton.captureOption QLabel {
                color: #ffffff;
                font-size: 9pt;
                padding-top: 5px;
            }
        """)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # 1. Capture Area Section (Top)
        main_layout.addWidget(self.create_capture_area_section())

        # 2. Take Screenshot Button (Bottom, Centered)
        btn_take_screenshot = QPushButton("Take Screenshot")
        btn_take_screenshot.setObjectName("takeScreenshotButton")
        
        # Layout to center the button horizontally
        button_layout = QHBoxLayout()
        button_layout.addStretch(1) # Spacer on the left
        button_layout.addWidget(btn_take_screenshot)
        button_layout.addStretch(1) # Spacer on the right
        
        main_layout.addLayout(button_layout)
        
        # Final stretch to ensure minimal vertical space is used
        main_layout.addStretch(1) 

    def create_capture_area_section(self):
        section_widget = QWidget()
        layout = QVBoxLayout(section_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        # Header Label
        header = QLabel("Capture Area")
        header.setProperty("class", "sectionHeader")
        layout.addWidget(header)

        # Button Row
        capture_buttons_layout = QHBoxLayout()
        capture_buttons_layout.setSpacing(10)

        # Group to ensure only one button is selected (radio behavior)
        self.capture_button_group = QButtonGroup(self)
        self.capture_button_group.setExclusive(True)

        def create_capture_button(text, icon_path=None, is_checked=False):
            btn = QPushButton()
            btn.setProperty("class", "captureOption")
            btn.setCheckable(True) 
            btn.setChecked(is_checked) 
            
            # Use an inner vertical layout to stack icon and text within the button
            btn_layout = QVBoxLayout(btn)
            btn_layout.setContentsMargins(5, 5, 5, 5) 
            
            # --- Icon Placeholder ---
            if icon_path:
                icon_label = QLabel()
                # Use QIcon() for placeholder, actual icons won't show unless paths are valid
                icon_label.setPixmap(QIcon(icon_path).pixmap(48, 48)) 
                icon_label.setAlignment(Qt.AlignCenter)
                btn_layout.addWidget(icon_label)
            
            # Text label
            text_label = QLabel(text)
            text_label.setAlignment(Qt.AlignCenter)
            btn_layout.addWidget(text_label)
            
            return btn

        # Create and add the three option buttons
        # NOTE: Placeholder paths used; replace with your actual icon file paths.
        btn_screen = create_capture_button("Screen", icon_path=":/icons/screen.svg") 
        btn_window = create_capture_button("Window", icon_path=":/icons/window.svg")
        btn_selection = create_capture_button("Selection", icon_path=":/icons/selection.svg", is_checked=True) 

        capture_buttons_layout.addWidget(btn_screen)
        capture_buttons_layout.addWidget(btn_window)
        capture_buttons_layout.addWidget(btn_selection)
        
        self.capture_button_group.addButton(btn_screen)
        self.capture_button_group.addButton(btn_window)
        self.capture_button_group.addButton(btn_selection)

        layout.addLayout(capture_buttons_layout)
        return section_widget


if __name__ == '__main__':
    # High DPI settings for better scaling on modern displays
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps) 

    app = QApplication(sys.argv)
    
    window = ScreenshotToolUI()
    window.show()
    sys.exit(app.exec_())