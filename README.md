# semantic-forest

This project utilises Python 3.12 and Poetry for dependency management. It leverages TensorFlow and Hugging Face for machine learning workflows.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### 1. Python 3.12
You must have Python 3.12 installed on your system.

* **Windows:**
    * Download the installer from [Python.org](https://www.python.org/downloads/).
    * **Important:** During installation, check the box **"Add Python to PATH"**.
* **macOS:**
    * Recommended using Homebrew:
        ```bash
        brew install python@3.12
        ```
* **Linux (Ubuntu/Debian):**
    ```bash
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.12 python3.12-venv python3.12-dev
    ```

### 2. Poetry
Install Poetry (the dependency manager) globally.

* **Official Installer (Recommended):**
    ```bash
    curl -sSL [https://install.python-poetry.org](https://install.python-poetry.org) | python3 -
    ```
    *Note: On Windows, you might use PowerShell:*
    ```powershell
    (Invoke-WebRequest -Uri [https://install.python-poetry.org](https://install.python-poetry.org) -UseBasicParsing).Content | py -
    ```

---

## 🚀 Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/silent-j-12345/semantic-forest.git](https://github.com/silent-j-12345/semantic-forest.git)
    cd semantic-forest
    ```

2.  **Configure Poetry to use Python 3.12**
    Tell Poetry specifically to use the 3.12 version you installed earlier.
    ```bash
    poetry env use 3.12
    ```

3.  **Install Dependencies**
    This command reads `pyproject.toml` and installs all required libraries (TensorFlow, Hugging Face, etc.) into a virtual environment.
    ```bash
    poetry install
    ```

---

## 🔐 Configuration

This project uses environment variables for sensitive data (API keys, DB credentials).

1.  **Create your .env file**
    Duplicate the example file to create your local configuration.
    ```bash
    cp .env.example .env
    ```
    *(Note: If you are on Windows, simply copy and rename the file manually).*

2.  **Edit the .env file**
    Open `.env` in your text editor and add your specific keys:
    ```ini
    HUGGING_FACE_TOKEN=hf_your_token_here
    DATABASE_URL=...
    ```

---

## 🏃‍♂️ Usage

There are two ways to run scripts with Poetry:

### How to run the scripts using `poetry run`
You can prefix your python commands with `poetry run`. This ensures the script runs inside the virtual environment.

```bash
poetry run python main.py