import pymysql
from faker import Faker
import random
import toml
# host
# port
# username
# password
# database

# dir(pymysql)

# db_conn = pymysql.connect(host="localhost", user="root", password="root", database="b14_test", port=3306)
# print(db_conn)



class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email





fake = Faker()

def generate_emps(num: int) -> list:
    emp_list = []
    for _ in range(1, num+1):
        name = fake.name()
        email_id = name.replace(" ", ".")
        obj = Employee(name=name,salary=random.randint(25000,99000), email=f"{email_id.lower()}@gmail.com")
        emp_list.append(obj)
    return emp_list

emp_records = generate_emps(20)

class MySQLOperations:
    def __init__(self):
        data = self.read_credentials()
        self.host = data.get("host")
        self.port = data.get("port")
        self.username = data.get("username")
        self.password = data.get("password")
        self.database = data.get("db")
    
    def read_credentials(self):
        try:
            with open(file=r'E:\Python-B14\Files\sql\config.local.toml', mode='r') as f:
                data = toml.load(f)
                return data.get("database")
        except FileNotFoundError:
            print("File doesn't exist. Please provide valid toml path.")
            return {} 


    def get_db_connection(self):
        conn = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database, port=self.port)
        print("Database connected successfully!")
        return conn

    def get_databases(self):
        GET_DATABASES_QUERY = "show databases;"
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute(GET_DATABASES_QUERY)
        dbs = cursor.fetchall()
        db_conn.close()
        # print(list(map(lambda x: x[0], dbs)))


    def get_tables(self):
        GET_TABLES_QUERY = "show tables;"
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute(GET_TABLES_QUERY)
        dbs = cursor.fetchall()
        db_conn.close()
        print(list(map(lambda x: x[0], dbs)))

    def create_table(self):
        CREATE_TABLE_QUERY = "create table employee (id int auto_increment primary key," \
        "name varchar(100) not null," \
        "salary decimal," \
        "email varchar(100) unique)"
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute(CREATE_TABLE_QUERY)
        print("Table created successfully!")
        db_conn.close()


    def insert_record(self): 
        INSERT_QUERY = """insert into employee (name, salary, email) values ('A', 25000, 'a@gmail.com'), ('B', 45000, 'b@gmail.com'), ('C', 65458, 'c@gmail.com')"""
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute(INSERT_QUERY)
        print("Records inserted successfully!")
        db_conn.commit()
        db_conn.close()

    def get_records(self): # all
        GET_QUERY = """select * from employee"""
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute(GET_QUERY)
        data = cursor.fetchmany(10) # fetchall()
        print(data)
        # data1 = cursor.fetchone()
        # data2 = cursor.fetchone()

        # print(data1)
        # print(data2)

        db_conn.close()

    def get_record(self, record_id):
        GET_ONE_QUERY = f"""select * from employee where id={record_id}"""
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        cursor.execute(GET_ONE_QUERY)
        data = cursor.fetchone()
        print(data)
        db_conn.close()

    def delete_record(self, record_id):
        pass

    def update_record(self, record_id):
        pass


    def insert_record_dynamic(self): 
        INSERT_QUERY = """insert into employee (name, salary, email) values (%s, %s, %s)"""
        db_conn = self.get_db_connection()
        cursor = db_conn.cursor()
        records = [(emp.name, emp.salary, emp.email) for emp in emp_records] # [('A', 54545, 'a@gmail.com'), (), (), (), ()...20]
        cursor.executemany(INSERT_QUERY, records)
        print("Records inserted successfully!")
        db_conn.commit()
        db_conn.close()

if __name__ == "__main__":
    op_obj = MySQLOperations()
    # op_obj.get_databases()
    # op_obj.get_tables()
    # op_obj.create_table()
    # op_obj.insert_record()
    # op_obj.get_record(8)
    # op_obj.insert_record_dynamic()
    op_obj.read_credentials()





# Task
# - get all tables from all databases
# - conf file based credentials
#  delete , update
# convert read data into Employee object
