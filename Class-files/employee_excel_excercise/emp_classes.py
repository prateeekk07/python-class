class Employee:
    def __init__(self, name, sname, salary, address, email, dob):
        self.name = name
        self.sname = sname
        self.salary = salary
        self.email = email
        self.address = address
        self.dob = dob


    def __str__(self):
        return f"\n{self.__dict__}"

    def __repr__(self):
        return str(self)
    

# if __name__ == "__main__":
#     obj1 = Employee("A", 25, 65000, "Pune")
#     obj2 = Employee("B", 26, 45000, "Pune")
#     obj3 = Employee("C", 28, 95000, "Pune")

    # print([obj1, obj2, obj3])