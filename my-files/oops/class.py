from faker import Faker
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
    # - instance method (wherever self ke yword is there it is called as instance method)
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