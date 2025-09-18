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

class Student:
    def __init__(self,name,job,mobile,email,address,dob):
        self.name = name
        self.job = job
        self.mobile = mobile
        self.email = email
        self.address = address
        self.dob = dob

    def __str__(self): #whenever you will print the object the str method will call
         return f"\n{self.__dict__}"
    
    def __repr__(self):
         return str(self)
    

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


#polymorphism

#duck typing philosphy
#method overloading
#method overriding
#construictor overloading
#operator overloading

