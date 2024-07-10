import PyPDF2

def read_passwords(password_file):
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

def brute_force_pdf(pdf_file, password_list):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    if not pdf_reader.is_encrypted:
        print(f'{pdf_file} is not encrypted.')
        return
    
    for password in password_list:
        try:
            pdf_reader.decrypt(password)
            # Check if the password is correct
            if pdf_reader.getPage(0):
                print(f'Success! The password is: {password}')
                return
        except Exception as e:
            continue
    
    print('Failed to find the password.')

if __name__ == "__main__":
    pdf_file = 'encrypted.pdf'
    password_file = 'passwords.txt'
    
    passwords = read_passwords(password_file)
    brute_force_pdf(pdf_file, passwords)
