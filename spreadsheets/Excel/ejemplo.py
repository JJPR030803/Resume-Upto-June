import openpyxl
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the Excel file
file_path = os.path.join(current_dir, 'spreadsheets', 'ejemplo.xlsx')

try:
    wb = openpyxl.load_workbook(file_path)
    print(wb.sheetnames)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except openpyxl.utils.exceptions.InvalidFileException:
    print(f"Invalid Excel file: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")