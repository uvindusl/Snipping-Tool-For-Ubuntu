from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

def capture_button(text, icon_path, ischecked=False):
    btn = QPushButton()
    btn.setProperty("class", "captureOption")
    btn.setCheckable(True)
    btn.setChecked(ischecked)

    btnLayout = QVBoxLayout(btn)
    btnLayout.setContentsMargins(5,5,5,5)

    if icon_path:
        iconLabel = QLabel()
        iconLabel.setPixmap(QIcon(icon_path).pixmap(48,48))
        iconLabel.setAlignment(Qt.AlignCenter)
        btnLayout.addWidget(iconLabel)

    textLabel = QLabel(text)
    textLabel.setAlignment(Qt.AlignCenter)
    btnLayout.addWidget(textLabel)

    return btn