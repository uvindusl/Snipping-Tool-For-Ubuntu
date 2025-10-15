import tempfile
import os
from datetime import datetime
import subprocess

def screenshot_capture(mode):
    tempDir = tempfile.gettempdir()
    tempFileName = os.path.join(tempDir, f"screenshot_temp_{datetime.now()}.png")

    command = ["gnome-screenshot", "-f" , tempFileName]

    if mode == "window":
        command.append("-w")
    elif mode == "area":
        command.append("-a")

    subprocess.run(command, check=True)

    print(tempfile)