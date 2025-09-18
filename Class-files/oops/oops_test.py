# 10  -- int

# Python
# 

# class Classname:
    # actions
    # variables


# int
def func():
    pass

# func()

# class Student:
#     def __init__(self, nm, ag, hght, cty="Dubai", *args, **kwargs): # method actions # magic method/dunder method
#         self.name = nm
#         self.age = ag
#         self.height = hght
#         self.city = cty
#         self.additional_info = kwargs

# class m


# s1 = Student("Aditya", 25, "5.11", salary=65000, native_place="Pune", surname="Patil")
# s2 = Student("B", 24, "5.06")
# s3 = Student("C", 23, "6.00", "Mumbai")
# print(s1.__dict__)
# print(s2.__dict__)
# print(s3.__dict__)

# s1.name = "Adi"

# s1.address = "Pune"
# s1.name = "Sayyad"
# print(s1.name)
# print(s1.age)
# print(s1)
# print(s1.__dict__) # magic variable
# s2 = Student("Prateek", 24)
# # s2.address = "Mumbai"
# print(s2.__dict__)
# s3 = Student("Aniket", 26)
# print(s3.__dict__)
# s4 = Student()
# s5 = Student()


# Human

# actions - walk, jump, talk

# attributes -- name, age, height, dob


# def func(a, b):
#     x = a
#     y = b
#     print(x+y)


# func(10,10)

# variables
    # - instance
    # - classlevel or static level

# methods
    # - instance method
    # - class method
    # - static method

# from faker import Faker

# - initialize instance variable
# - kab call hota hai?
# dunder method
# self keyword

class Student:
    college_name = "D.Y. Patil Pune"  # class level/static variable
    college_courses = ["Electrical", "IT", "Civil", "Mechanical"]
    def __init__(self, sid, nm, job, mob, email, addr, dob):
        self.sid = sid
        self.name = nm
        self.job = job
        self.date_of_birth = dob
        self.mobile = mob
        self.email = email
        self.address = addr

    @classmethod
    def get_college_name(cls): # class
        print(cls)
        print(cls.college_name)

    @classmethod
    def update_college_courses(cls, new_course):
        cls.college_courses.append(new_course)

    @classmethod
    def set_college_dept(cls, dept_list):
        cls.departments = dept_list

    @classmethod
    def test_class_method_m1(cls):
        print("in class method m1")

    @classmethod
    def test_class_method_m2(cls):
        cls.test_class_method_m1()
        print("in class method m2")

    def __str__(self):
        # print("in str method")
        return f"\n{self.__dict__}"

    def __repr__(self):
        # print("in repr method")
        return str(self) # + -- __add__  # str --> __str__

    def get_name(self):
        print(self.college_name)
    
    def update_name(self, nm): # update  setter/mutator
        print("INFO: update value of name")
        self.name = nm
    
    def delete_name(self):
        del self.name
    
    def fetch_details(self): # getter/accessor
        print("INFO: gettng all the details of student")
        print(f"""
Student ID:- {self.sid}
Student Name:- {self.name}
Student Job:- {self.job}
Student Mobile:- {self.mobile}
Student Email:- {self.email}
Student Address:- {self.address}
Student DOB:- {self.date_of_birth}
######################################
""")
     
    def test_m1(self):
        print("inside m1")

    def test_m2(self):
        self.test_m1()
        print("inside m2")

# print(Student.college_courses)
# Student.update_college_courses("Electronics")
# print(Student.college_courses)



# Student.delete_name()

# DRY
    # object/instance

# print(Student.college_name)

# s1 = Student(101, nm="A", job="Test Job", mob="+91-4655485545", email="a@gmail.com", addr="Pune", dob="26-05-1996")

# s1.test_m2()
# del s1.name
# s1.update_name("AAA")
# s1.get_name()
# s1.delete_name()
# s1.fetch_details()
# print(s1.job)
# s1.Job = "Python Developer"
# print(s1.__dict__)

# s2 = Student(102, nm="B", job="Test Job", mob="+91-4655458545", email="b@gmail.com", addr="Pune", dob="26-05-1996")
# print(s2.__dict__)

# s2.fetch_details()
# lst = [s1, s2]
# print(lst)
# print(s1)
# print(s2)



# Create a Faker instance
# type hint

# fake = Faker()

# def generate_students(num: int) -> list:
#     student_list = []
#     for i in range(1, num+1):
#         name = fake.name()
#         email_id = name.replace(" ", ".")
#         obj = Student(sid=100+i,nm=name, job=fake.job(), mob=fake.phone_number(), email=f"{email_id.lower()}@gmail.com", addr=fake.address(), dob=fake.date_of_birth(minimum_age=18, maximum_age=70))
        
#         student_list.append(obj)
#     return student_list


# stds = generate_students(100)


# for i in stds:
#     if i.name.split()[1].startswith("R"):
#         print(i)

# def get_std_with_name_a():
#     pass


# def get_stud_age_more_than_20_yers():
#     pass

# #10 # functions

# def get_with_50_k_more():
#     pass

class CommonMethod(object): # parent
    # def __str__(self):
    #     return f"\n{self.__dict__}"
    
    # def __repr__(self):
    #     return str(self)
    pass
class Address(CommonMethod): # child
    def __init__(self, area, pin, city, state):
        self.area = area
        self.pincode = pin
        self.city = city
        self.state = state

# a1 = Address("Karve Nagar", 411045, "Pune", "MH")
# a2 = Address("Wakad", 412157, "Pune", "MH")
# a3 = Address("Bavdhan", 412015, "Pune", "MH")
# a4 = Address("Katraj", 4157869, "Pune", "MH")

class Student(CommonMethod): # child
    def __init__(self, name, age, marks, address):
        self.name = name
        self.age = age
        self.marks = marks
        self.address = address

    # def __str__(self):
    #     return self.name

# class A:

s1 = Student("A", 21, 85, "Pune")

# print(s1)
# print(s1.address.pincode)
# s1.age = 23


# OOPs -- 4 pillar
# inheritance -- 
# polymorphism
# abstraction -- 
# encapsulation -- 


# class -- 
object


