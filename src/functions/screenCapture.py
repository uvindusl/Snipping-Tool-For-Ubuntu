import tempfile
import os
from datetime import datetime
import subprocess

def screenshot_capture(mode):
    tempDir = tempfile.gettempdir()
    tempFileName = os.path.join(tempDir, f"screenshot_temp_{datetime.now()}.png")

    command = ["gnome-screenshot", "-f" , tempFileName]

    if mode == "screen":
        pass
    elif mode == "window":
        command.append("-w")
    elif mode == "area":
        command.append("-a")

    subprocess.run(command, check=True)

    print(f"Screenshot successfully saved to: {tempFileName}")