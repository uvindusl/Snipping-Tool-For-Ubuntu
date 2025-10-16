from PyQt5.QtWidgets import QApplication
from .GUI.MainWindow import SnappingTool # Assuming SnappingTool is the main window class
import sys
# Import QPixmap alongside QIcon
from PyQt5.QtGui import QIcon, QPixmap 
import os
from pathlib import Path

# ... basedir is not strictly needed ...

def main():
    app = QApplication(sys.argv)
    
    # --- PATH CONSTRUCTION (VERIFIED) ---
    # Running from root, so we explicitly include 'src'
    project_root = Path(os.getcwd())
    icon_path = str(project_root / 'src' / 'Assets' / 'SnappingTool.png')
    
    # --- ROBUST ICON LOADING ---
    
    # 1. Load the image using QPixmap
    pixmap = QPixmap(icon_path)
    
    if not pixmap.isNull():
        # 2. If QPixmap successfully read the file, wrap it in a QIcon
        app_icon = QIcon(pixmap)
        app.setWindowIcon(app_icon)
        # Optional: Print success if you want confirmation
        # print("SUCCESS: Application icon loaded via QPixmap wrapper.")
    else:
        # 3. If loading fails, print a definitive error message
        print(f"\nFATAL ICON ERROR: The path is correct, but PyQt cannot read the image file format at:\n{icon_path}")
        print("Please ensure the image (SnappingTool.png) is a standard, uncorrupted PNG.")

    # -----------------------------
    
    window = SnappingTool()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()