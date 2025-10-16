# Contributing to Snipping Tool for Ubuntu

Thank you for considering contributing to the Snipping Tool for Ubuntu\! Whether you're reporting a bug, suggesting a new feature, or submitting code, your help is invaluable.

## Bug Reports

If you've found a bug in the application, please submit a detailed report on the GitHub [Issues Page](https://github.com/uvindusl/Snipping-Tool-For-Ubuntu/issues).

**When submitting a bug report, please include:**

1.  **Clear Title:** A concise description of the issue (e.g., "App crashes when selecting 'Window' mode").
2.  **Steps to Reproduce:** Numbered steps that reliably cause the bug.
3.  **Expected Behavior:** What you expected to happen.
4.  **Actual Behavior:** What actually happened (e.g., "The application froze and closed").

    ```bash
    /usr/bin/SnappingTool/SnappingTool
    ```

5.  **Environment:** Your OS version (e.g., Ubuntu 22.04), Desktop Environment (GNOME/KDE), and Display Server (Xorg/Wayland).

## Feature Requests

We welcome suggestions for new features or enhancements. Please open a new issue and label it as "enhancement." Clearly describe the feature and why it would be useful.

## Code Contributions

If you'd like to contribute code, please follow this workflow:

### 1\. Setup Your Development Environment

You'll need Python 3.x, `pip`, and Git installed.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/uvindusl/Snipping-Tool-For-Ubuntu.git
    cd Snipping-Tool-For-Ubuntu
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install System Dependencies (Required for Testing):**
    Ensure you have the core system dependencies installed:

    ```bash
    sudo apt install tesseract-ocr libx11-6
    ```

### 2\. Make Your Changes

1.  **Create a new branch:** Use a descriptive name (e.g., `feature/add-resize-handle` or `fix/crash-on-selection`).
    ```bash
    git checkout -b your-branch-name
    ```
2.  **Code:** Implement your fix or feature. Remember to keep the existing code style consistent.
3.  **Test:** Verify that your changes work and that you haven't introduced any new bugs.
4.  **Commit:** Write clear, concise commit messages.

### 3\. Submit Your Work (Pull Request)

1.  **Push your branch** to your fork of the repository:
    ```bash
    git push origin your-branch-name
    ```
2.  **Open a Pull Request (PR):** Go to the main GitHub repository page, and you should see a prompt to open a PR.
3.  **Describe your changes** clearly in the PR description, referencing any related issues (e.g., "Fixes \#10").

I will review your PR, provide feedback, and merge it when ready\!
