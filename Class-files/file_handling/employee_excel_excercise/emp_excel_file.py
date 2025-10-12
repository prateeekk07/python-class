import openpyxl

FILE_PATH = r"E:\Python-B14\Files\file_handling\employee_excel_excercise\employees.xlsx"

def load_work_book():
    wb = openpyxl.load_workbook(filename=FILE_PATH)
    sheet = wb.active
    return wb, sheet