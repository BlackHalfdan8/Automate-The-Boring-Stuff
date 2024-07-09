import openpyxl
import os

def text_files_to_spreadsheet(directory):
    # Create a new workbook and select the active sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Get the list of text files in the directory
    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    # Loop through each text file
    for col_num, filename in enumerate(text_files, 1):
        with open(os.path.join(directory, filename), 'r') as file:
            lines = file.readlines()
            # Write each line to a row in the current column
            for row_num, line in enumerate(lines, 1):
                sheet.cell(row=row_num, column=col_num).value = line.strip()

    # Save the workbook
    workbook.save('text_files_to_spreadsheet.xlsx')

# Define the directory containing the text files
directory = 'text_files_directory'  # Replace with the actual directory path

# Convert text files to spreadsheet
text_files_to_spreadsheet(directory)
