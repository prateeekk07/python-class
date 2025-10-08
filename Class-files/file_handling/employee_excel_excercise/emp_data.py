from emp_classes import Employee
from faker import Faker
import random


fake = Faker()

def generate_emps(num: int) -> list:
    emp_list = []
    for _ in range(1, num+1):
        name = fake.name()
        email_id = name.replace(" ", ".")
        obj = Employee(name=name,salary=random.randint(25000,99000), email=f"{email_id.lower()}@gmail.com", address=fake.address(), dob=fake.date_of_birth(minimum_age=18, maximum_age=70))
        emp_list.append(obj)
    return emp_list


# if __name__ == "__main__":
#     print(generate_emps(10))