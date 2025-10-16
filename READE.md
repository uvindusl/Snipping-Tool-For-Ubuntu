# Snipping Tool for Ubuntu

A dedicated, modern screenshot and Optical Character Recognition (OCR) utility designed specifically for Debian and Ubuntu-based Linux distributions.

## Features

- **Custom Capture Modes:** Quickly capture the full screen, the active window, or a specific area selection.
- **Integrated OCR:** Extract text directly from any captured image selection.
- **Modern UI:** Clean, intuitive interface built using PyQt5.

## Installation

### Prerequisites

This application requires two essential system dependencies:

1.  **`tesseract-ocr`**: Required for the text extraction (OCR) feature.

### Recommended Installation (Automatic Dependencies)

The easiest way to install the application and ensure all required dependencies are installed automatically is by using the `apt` package manager with the provided `.deb` file.

1.  **Download:** Download the latest stable `.deb` file from the **[Releases Page](https://github.com/uvindusl/Snipping-Tool-For-Ubuntu/releases)**.

2.  **Install:** Open your terminal, navigate to the download directory, and run the installation command (replacing the file name with the latest version):

    ```bash
    sudo apt install ./snippingtool-LATEST_VERSION.deb
    ```

---

## 🚀 Usage

1.  Launch the application from your application menu (search for "Snipping Tool").
2.  Select your desired **Capture Area** (Screen, Window, or Selection).
3.  Click the **"Take Screenshot"** button.
4.  Your selection will be captured and the result will be displayed for saving or OCR.

---

## 🛠️ Contributing and Reporting Bugs

If you encounter any issues, please report them on the [Issues Page](https://github.com/uvindusl/Snipping-Tool-For-Ubuntu/issues).

### Reporting Guidelines:

1.  **Check Existing Issues:** Search to see if the bug has already been reported.

---

## 🏗️ Building From Source

If you wish to modify the code or rebuild the package:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/uvindusl/Snipping-Tool-For-Ubuntu.git
    cd Snipping-Tool-For-Ubuntu
    ```
2.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run Locally (for development):**
    ```bash
    python3 SnappingTool.py
    ```
