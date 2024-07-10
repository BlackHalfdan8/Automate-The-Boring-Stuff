import os
import PyPDF2
import sys

def encrypt_pdf(input_file, output_file, password):
    pdf_reader = PyPDF2.PdfReader(input_file)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    pdf_writer.encrypt(password)
    
    with open(output_file, 'wb') as f:
        pdf_writer.write(f)
    print(f'Encrypted {input_file} and saved as {output_file}')

def decrypt_pdf(input_file, output_file, password):
    pdf_reader = PyPDF2.PdfReader(input_file)
    
    if pdf_reader.is_encrypted:
        pdf_reader.decrypt(password)
    
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    
    with open(output_file, 'wb') as f:
        pdf_writer.write(f)
    print(f'Decrypted {input_file} and saved as {output_file}')

def process_pdfs(folder, password, operation):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                input_file = os.path.join(foldername, filename)
                output_file = os.path.join(foldername, f'{"encrypted_" if operation == "encrypt" else "decrypted_"}{filename}')
                
                if operation == 'encrypt':
                    encrypt_pdf(input_file, output_file, password)
                elif operation == 'decrypt':
                    decrypt_pdf(input_file, output_file, password)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('Usage: python pdf_paranoia.py <encrypt|decrypt> <folder> <password>')
        sys.exit(1)
    
    operation = sys.argv[1]
    folder = sys.argv[2]
    password = sys.argv[3]
    
    if operation not in ['encrypt', 'decrypt']:
        print('Invalid operation. Use "encrypt" or "decrypt".')
        sys.exit(1)
    
    process_pdfs(folder, password, operation)
