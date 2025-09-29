import openpyxl

FILE_PATH = r"D:\python b14\python-class\my-files\file_handling\employee_excel_exercise\employees.xlsx"

def load_work_book():
    wb = openpyxl.load_workbook(FILE_PATH)
    sheet = wb.active
    return wb, sheet