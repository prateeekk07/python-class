# from faker import Faker
# class student:
#      def __init__(self): #method actions # magic method/dunder method #self always point to the current object
#           print("in init method")
#           self.name = "Prateek" #construct #static value

# s1 = student() #refernce vairiable
# print(s1.__dict__) 

# #whenever the object is created the init method will call automatically.

#-----------------------------------------------

# class student:
#      def __init__(self,name,age):
#           self.name = name
#           self.age = age

# s1 = student("Prateek",23) 
# print(s1.__dict__) 

# s2 = student() #requires postinal arguments
# print(s2.__dict__) 

#-----------------------------------------------

# class Student:
#     def __init__(self,name,job,mobile,email,address,dob):
#         self.name = name
#         self.job = job
#         self.mobile = mobile
#         self.email = email
#         self.address = address
#         self.dob = dob

#     def __str__(self): #whenever you will print the object the str method will call
#          return f"\n{self.__dict__}"
    
#     def __repr__(self):
#          return str(self)
    

# s1 = Student(name="Prateek",job="SD1",mobile=9876543210,email="prateekc53@gmail.com",address="indore",dob=25)
# s2 = Student(name="abhiraj",job="SD",mobile=88879845120,email="abc@gmail.com",address="bhopal",dob=18)
# # print(s1.__dict__)
# # print(s2.__dict__)

# l1 = [s1,s2]
# print(l1)



#Create a Faker instance

# def generate_students(num):
#      fake = Faker()
#      student_list = []
#      for _ in range(1,num+1):
#           name = fake.name()
#           email_id = name.replace(" ",".")
#           obj = Student(name=name, job=fake.job(), mobile=fake.phone_number(), email=f"{email_id.lower()}@gmail.com", address=fake.address(), dob=fake.date_of_birth())
#           student_list.append(obj)
#      return student_list

# stds = generate_students(100)

# print(stds)

# What is __init__
 # - initialize instance vairiable
 # - kab call hota hai jab object banta hai
 # - dunder method
 # - self keyword



# vairiables 
    # -instance 
    #   - attached to instance 
    #   - where to declare
    #   - inside the class
    #       - instance method -- using self
    #           -print(self.name), self.name = "New name", del self.name,self.new_attr = value
    #   - outside the class -- using refernce variable
    #       -print(s1.name), s1.name = "New name", del s1.name,s1.new_attr = value
    #########
    # -classlevel or static level 
    #   -attached to class, commome for all the instances
    #   - where to declare/acess/delete/update
    #       -inside the class
    #           -class method -- using cls
    #               -print(cls.College_name), cls.college_name = "New college name" 
    #       -outside the class -- using classname
    #           -print(Student.College_name), Student.College_name = "New name", del Student.College_name, Student.new_attr = value

# methods 
    # - instance method (wherever self keyword is there it is called as instance method)
        # - to derclare/acces/update/delete instance vairiable 
        # self is reserved
        # how to call
            # outside the classs -- using refernce variable s1
                # s1.set_name(), s1.get_details()
            # inside the class -- using self in a instance method
            #    self.test_m1
    
    
    # - class method
    #    - to declare/access/update/delete class level variable
    #    - cls is reserved
    #    - use @classmethod decorator
    #    - how to call 
    #       - outside the class -- using class name
    #           print(classname.college_name), classname.college_address = "Pune"
    #       - inside the class -- using cls in classmethod
    #           cls.test_class_method_m1()       

# class Student:
#     # Class variable
#     school_name = "Greenwood High"

#     def __init__(self, name, age):
#         # Instance variables
#         self.name = name
#         self.age = age

#     # Instance method (works on object/instance level)
#     def display_info(self):
#         return f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}"

#     # Class method (works on class level, not instance level)
#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name
#         return f"School name changed to {cls.school_name}"

#     # Static method (general utility function, no self or cls needed)
#     @staticmethod
#     def is_adult(age):
#         return age >= 18


# # Example usage
# # Creating objects
# s1 = Student("Alice", 17)
# s2 = Student("Bob", 19)

# # Using instance method
# print(s1.display_info())  
# print(s2.display_info())

# # Using class method
# print(Student.change_school("Sunrise Academy"))
# print(s1.display_info())

# # Using static method
# print(Student.is_adult(20))   # True
# print(Student.is_adult(15))   # False

# class BankAccount:
#     # Class variable (same for all accounts)
#     bank_name = "National Bank"
#     interest_rate = 3.5   # default interest rate

#     def __init__(self, account_holder, balance=0):
#         # Instance variables (unique for each account)
#         self.account_holder = account_holder
#         self.balance = balance

#     # Instance method → works with individual account
#     def deposit(self, amount):
#         self.balance += amount
#         return f"{self.account_holder} deposited {amount}. New balance: {self.balance}"

#     def withdraw(self, amount):
#         if amount > self.balance:
#             return f"Insufficient funds for {self.account_holder}!"
#         self.balance -= amount
#         return f"{self.account_holder} withdrew {amount}. New balance: {self.balance}"

#     # Class method → changes class-level details (affects all accounts)
#     @classmethod
#     def set_interest_rate(cls, new_rate):
#         cls.interest_rate = new_rate
#         return f"Interest rate updated to {cls.interest_rate}% for all accounts."

#     # Static method → utility method (not tied to account or class variables)
#     @staticmethod
#     def calculate_interest(balance, rate):
#         return (balance * rate) / 100


# # Example usage
# # Creating accounts
# acc1 = BankAccount("Alice", 1000)
# acc2 = BankAccount("Bob", 500)

# # Instance methods
# print(acc1.deposit(200))
# print(acc2.withdraw(100))

# # Class method (update interest rate for all)
# print(BankAccount.set_interest_rate(5.0))

# # Static method (calculate interest without needing an object)
# print("Interest on 1000 at 5%:", BankAccount.calculate_interest(1000, 5))

# class Bank:
#     employee_id = 1
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show_name(self,upname):
#         self.name = upname  
#         print(f"name is updated : {upname}")
        
#     def show_id(cls):
#         print(cls.employee_id)


# o1 = Bank("prateek",22)
# o1.show_name("Abhijeet")
# o1.show_id()
    
# class Bank:
#     employee_id = 1

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_name(self, upname):
#         self.name = upname  
#         print(f"name is updated : {upname}")

#     @classmethod
#     def show_id(cls):
#         print(f"Employee ID: {cls.employee_id}")

#     @staticmethod
#     def bank_policy():

#         print("Bank policy: Minimum balance must be ₹1000.")

# # Create object
# o1 = Bank("Prateek", 22)

# # Call instance method
# o1.show_name("Abhijeet")

# Call class method
o1.show_id()

# Call static method (can be called on class or object)
Bank.bank_policy()
o1.bank_policy()
