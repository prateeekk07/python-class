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
        sheet.cell(row=1, column=2).value = "sname"
        sheet.cell(row=1, column=3).value = "dob"
        sheet.cell(row=1, column=4).value = "email"
        sheet.cell(row=1, column=5).value = "address"
        sheet.cell(row=1, column=6).value = "salary"
        workbook.save(self.file_path)


    def insert_records(self):
        workbook, sheet = load_work_book()
        emps = self.generate(20)

        for idx, record in enumerate(emps, start=2):  # start=2 means row 2
            sheet.cell(row=idx, column=1).value = record.name
            sheet.cell(row=idx, column=2).value = record.sname
            sheet.cell(row=idx, column=3).value = record.dob
            sheet.cell(row=idx, column=4).value = record.email
            sheet.cell(row=idx, column=5).value = record.address
            sheet.cell(row=idx, column=6).value = record.salary

        workbook.save(self.file_path)

    def read_records(self):
        _, sheet = load_work_book()
        emp_list = [
        Employee(
            sheet.cell(row=i, column=1).value,   # name
            sheet.cell(row=i, column=2).value,   # sname
            sheet.cell(row=i, column=6).value,   # salary
            sheet.cell(row=i, column=5).value,   # address
            sheet.cell(row=i, column=4).value,   # email
            sheet.cell(row=i, column=3).value    # dob
        )
        for i in range(2, sheet.max_row + 1)  # include last row
    ]
        return emp_list


    def filter_data(self):
        pass


