PDF Protector

PDF Protector is a Python script that encrypts PDF files with a password to enhance security.

🚀 Features

Encrypts any PDF file with a password

Prevents unauthorized access

Simple command-line interface (CLI)

📌 Requirements

Python 3.x

PyPDF2 module

🔧 Installation

Clone the repository and install dependencies:

# Clone the repository
git clone https://github.com/safaYa12/pdf_protector.git
cd pdf_protector

# Create a virtual environment (optional but recommended)
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

# Install required packages
pip install -r requirements.txt

🔑 Usage

To encrypt a PDF, run:

python pdf_protector.py -i input.pdf -o output.pdf -p yourpassword

If no arguments are provided, the script will prompt for input interactively.

📂 Example

python pdf_protector.py -i myfile.pdf -o secure_myfile.pdf -p secret123

This will generate secure_myfile.pdf, which is password-protected with secret123.

🛠 Troubleshooting

Ensure PyPDF2 is installed: pip install PyPDF2

If running inside a virtual environment, activate it before executing the script.PDF Protector
