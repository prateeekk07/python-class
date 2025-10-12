import csv
FILE_PATH = r"E:\Python-B14\Files\file_handling\csv_excercise\test2.csv"

# with open(FILE_PATH, "r") as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#     print(headers)
#     print("#############")
#     for row in reader:
#         print(row)

# import csv
# with open(FILE_PATH, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#     writer.writerow([3, "Guido van Rossum", "Python Programming"])

# row_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
# with open(FILE_PATH, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(row_list)

# import csv

# with open(FILE_PATH, 'w', newline='') as file:
#     fieldnames = ['player_name', 'fide_rating']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
#     writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
#     writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})


import csv

class EmployeeCSVHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    # --- Using csv.reader ---
    def read_with_reader(self):
        """Read CSV using csv.reader (returns list of rows)"""
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)  # first row is header
            rows = [row for row in reader]
        return header, rows

    # --- Using csv.DictReader ---
    def read_with_dictreader(self):
        """Read CSV using csv.DictReader (returns list of dicts)"""
        with open(self.file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = [row for row in reader]
        return rows

    # --- Filter data ---
    def filter_by_company(self, rows, company_name):
        """Filter rows (list of dicts) by company name"""
        return [row for row in rows if row['Company'] == company_name]

    def filter_by_salary_above(self, rows, threshold):
        """Filter rows (list of dicts) by salary above threshold"""
        return [row for row in rows if int(row['Salary']) > threshold]

    # --- Using csv.writer ---
    def write_with_writer(self, file_path, header, rows):
        """Write rows (list of lists) using csv.writer"""
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)

    # --- Using csv.DictWriter ---
    def write_with_dictwriter(self, file_path, fieldnames, rows):
        """Write rows (list of dicts) using csv.DictWriter"""
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)


import pandas as pd

CSV_PATH = r"E:\Python-B14\Files\file_handling\csv_excercise\employees.csv"
df = pd.read_csv(CSV_PATH)
# print(dir(df))
# print(df.head())
# print(df.tail())
# print(df.shape)
# columns = df.columns.tolist()
# print(columns)

# info = df.dtypes.to_dict()
# print(info)

# describe = df.describe().to_dict()
# print(describe)

# print(df["Salary"].min())

# data = df[df['Age'] > 50].head()
# print(data)

# data = df.sort_values(by="Salary")
# print(data)

# data = df.groupby("Company")["Age"].mean()
# print(data.to_dict())

# data = df["Salary"]
# print(data)

# df["Name_Company"] = df['Name'] + "-" + df["Company"]
# print(df)

# df["Bonus"] = 0
# df.to_csv(CSV_PATH)
# print(df)
# print(df)
# df["Age"] = df["Age"].fillna(25)
# print(df)