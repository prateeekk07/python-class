import openpyxl

FILE_PATH = r"D:\python b14\python-class\Class-files\employee_excel_excercise\employees.xlsx"

def load_work_book():
    wb = openpyxl.load_workbook(filename=FILE_PATH)
    sheet = wb.active
    return wb, sheet