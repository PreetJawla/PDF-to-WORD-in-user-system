# PDF-to-WORD in User System

A web-based application that converts PDF files to editable Word documents. This system is designed to offer users an intuitive interface for uploading PDFs and receiving Word files quickly. Built with Python, it leverages modern web frameworks and libraries to ensure smooth and efficient conversions.

![Python Version](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Easy File Conversion:** Quickly convert PDFs into Word documents.
- **User-Friendly Interface:** A clean UI for uploading files and receiving results.
- **Automated Processing:** Handles file conversion automatically and stores converted files in a designated folder.
- **Cross-Platform:** Works on multiple operating systems with minimal configuration.

---

## Prerequisites

Before you get started, ensure you have met the following requirements:

- Python 3.x installed on your system.
- A working knowledge of basic command-line operations.
- (Optional) Familiarity with virtual environments to manage dependencies.

---

## Installation

### Set Up Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Install Dependencies

If you have a requirements.txt, install the dependencies using:

```bash
pip install -r requirements.txt
```

If no `requirements.txt` file is available:

```bash
pip install flask pdf2docx
```

---

## Usage

### Run the Application

```bash
python app.py
```

### Open in Browser

Navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Convert Files

- Upload a PDF.
- Click “Convert”.
- Download the converted Word file from the link or `converted_files/` folder.

---

## Project Structure

```
PDF-to-WORD-in-user-system/
├── .venv/                  # Virtual environment directory
├── converted_files/        # Folder for storing converted Word documents
├── static/                 # Static assets (CSS, JS)
├── templates/              # HTML templates
├── venv/                   # (if applicable)
└── app.py                  # Main application file
```

---

## Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a branch:

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes:

```bash
git commit -m "Add feature"
```

4. Push to the branch:

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Contact

**Preet Jawla**  
Email: [your.email@example.com](mailto:your.email@example.com)

---

*Happy Converting!*
