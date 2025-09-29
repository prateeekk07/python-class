from emp_abstraction import FileOperation
from emp_data import generate_emps
from emp_excel_file import load_work_book, FILE_PATH

class ExcelFileOperation(FileOperation):

    def generate(self,num):
            return generate_emps(num)

    def write_headers(self):
           workbook, sheet = load_work_book()
           sheet.cell(row=1, column=1).value = "name"
           sheet.cell(row=1, column=2).value = "name"
           sheet.cell(row=1, column=3).value = "dob"
           sheet.cell(row=1, column=4).value = "email"
           sheet.cell(row=1, column=5).value = "address"
           sheet.cell(row=1, column=6).value = "salary"
           workbook.save(FILE_PATH)
           
    
    def insert_records(self):
            pass


    def read_records(self):
            pass