from emp_abstraction import FileOperation
from emp_data import generate_emps
from emp_excel_file import load_work_book, FILE_PATH
from emp_classes import Employee

class ExcelFileOperation(FileOperation):
    def __init__(self):
        self.file_path = FILE_PATH

    def generate(self, num):
        return generate_emps(num)

    def write_headers(self):
        workbook, sheet = load_work_book()
        sheet.cell(row=1, column=1).value = "name"
        sheet.cell(row=1, column=2).value = "dob"
        sheet.cell(row=1, column=3).value = "email"
        sheet.cell(row=1, column=4).value = "address"
        sheet.cell(row=1, column=5).value = "salary"
        workbook.save(self.file_path)


    def insert_records(self):
        workbook, sheet = load_work_book()
        emps = self.generate(20)
        c = 2
        for record in emps: # enumerate -- 2 index
            sheet.cell(row=c, column=1).value = record.name
            sheet.cell(row=c, column=2).value = record.dob
            sheet.cell(row=c, column=3).value = record.email
            sheet.cell(row=c, column=4).value = record.address
            sheet.cell(row=c, column=5).value = record.salary
            c += 1
        workbook.save(self.file_path)

    def read_records(self):
        _, sheet = load_work_book()
        emp_list = [] # [Employee(sheet.cell(row=i, column=1).value, salary, address, email, dob=sheet.cell(row=i, column=2).value) for i in range(2, sheet.max_row)]
        for i in range(2, sheet.max_row):
            name = sheet.cell(row=i, column=1).value
            dob = sheet.cell(row=i, column=2).value
            email = sheet.cell(row=i, column=3).value
            address = sheet.cell(row=i, column=4).value
            salary = sheet.cell(row=i, column=5).value
            emp_obj = Employee(name, salary, address, email, dob)
            emp_list.append(emp_obj)
        return emp_list

    def filter_data(self):
        pass


