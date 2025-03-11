import PyPDF2
import argparse
import os

def create_password_protected_pdf(input_pdf, output_pdf, password):
    """
    Encrypts a given PDF with a password and saves it as a new file.
    """
    try:
        with open(input_pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_writer = PyPDF2.PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            pdf_writer.encrypt(password)

            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

        print(f"✅ Password-protected PDF saved as: {output_pdf}")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_pdf}' was not found.")
    except PyPDF2.errors.PdfReadError:
        print(f"❌ Error: The file '{input_pdf}' is not a valid PDF.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    try:
        parser = argparse.ArgumentParser(description="PDF Password Protector")
        parser.add_argument("-i", "--input", help="Input PDF file", required=False)
        parser.add_argument("-o", "--output", help="Output encrypted PDF file", required=False)
        parser.add_argument("-p", "--password", help="Password for the PDF", required=False)

        args = parser.parse_args()

        if not args.input:
            args.input = input("Enter the input PDF file path: ").strip()

        if not os.path.exists(args.input):
            print("❌ Error: The specified PDF file does not exist.")
            return

        if not args.output:
            args.output = input("Enter the output PDF file name (or press Enter to use default): ").strip()
            if not args.output:
                args.output = "protected_" + os.path.basename(args.input)

        if not args.password:
            args.password = input("Enter a password for the PDF: ").strip()

        create_password_protected_pdf(args.input, args.output, args.password)

    except KeyboardInterrupt:
        print("\n⚠️ Process interrupted by user. Exiting...")

if __name__ == "__main__":
    main()
