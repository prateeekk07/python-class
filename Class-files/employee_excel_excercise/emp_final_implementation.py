from emp_operation import ExcelFileOperation




if __name__ == "__main__":
    obj = ExcelFileOperation()
    obj.write_headers()
    obj.insert_records()
    print(obj.read_records())