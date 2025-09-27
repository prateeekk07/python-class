# assignment 2
# - 6 decoators 
# - oops concept -- inheritance -- > 2 examples each for 5 types --
# asbtraction -- car, file -- > 2 examples 


#Single 

#EXample 1
# class Football_Club:
#     def __init__(self,name,positon):
#         self.name = name
#         self.positon = positon

#     def player_details(self):
#         return f"Name : {self.name} | Position : {self.positon}"
    

# class additonal_details(Football_Club):
#     def __init__(self,name,positon,salary):
#         super().__init__(name,positon)
#         self.salary = salary

#     def player_salary(self):
#         return f"{self.name} who plays as {self.positon} draws {self.salary}$."
    

# p1 = additonal_details("Prateek","Striker",50000)
# print(p1.player_details())
# print(p1.player_salary())
        
#EXample 2

# class Hospital:
#     def __init__(self, patient_name, disease):
#         self.patient_name = patient_name
#         self.disease = disease

#     def patient_record(self):
#         return f"Patient: {self.patient_name} | Disease: {self.disease}"


# class PatientDetails(Hospital):
#     def __init__(self, patient_name, disease, doctor):
#         super().__init__(patient_name, disease)
#         self.doctor = doctor

#     def assigned_doctor(self):
#         return f"{self.patient_name} is being treated for {self.disease} by Dr. {self.doctor}."


# p1 = PatientDetails("Rahul", "Flu", "Mehta")
# print(p1.patient_record())
# print(p1.assigned_doctor())

#Multilevel

#EXample - 1

# class Device:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         return f"Device: {self.name}"


# class SmartDevice(Device):
#     def __init__(self, name, wifi_enabled):
#         super().__init__(name)
#         self.wifi_enabled = wifi_enabled

#     def connectivity(self):
#         return f"{self.name} Wi-Fi Enabled: {self.wifi_enabled}"


# class SmartBulb(SmartDevice):
#     def __init__(self, name, wifi_enabled, brightness):
#         super().__init__(name, wifi_enabled)
#         self.brightness = brightness

#     def bulb_status(self):
#         return f"{self.name} brightness set to {self.brightness}%."


# b = SmartBulb("Philips Hue", True, 75)
# print(b.info())
# print(b.connectivity())
# print(b.bulb_status())
        
#example 2 
# class User:
#     def __init__(self, username):
#         self.username = username

#     def profile(self):
#         return f"User: {self.username}"


# class Customer(User):
#     def __init__(self, username, address):
#         super().__init__(username)
#         self.address = address

#     def delivery_address(self):
#         return f"Delivery Address: {self.address}"


# class PrimeCustomer(Customer):
#     def __init__(self, username, address, prime_points):
#         super().__init__(username, address)
#         self.prime_points = prime_points

#     def prime_info(self):
#         return f"Prime Points: {self.prime_points}"


# c = PrimeCustomer("JohnDoe", "New York, USA", 1200)
# print(c.profile())
# print(c.delivery_address())
# print(c.prime_info())

#Multiple

#example 1 

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         return f"Name: {self.name}"


# class Job:
#     def __init__(self, role):
#         self.role = role

#     def show_role(self):
#         return f"Role: {self.role}"


# class Employee(Person, Job):
#     def __init__(self, name, role, salary):
#         Person.__init__(self, name)
#         Job.__init__(self, role)
#         self.salary = salary

#     def show_salary(self):
#         return f"Salary: {self.salary}"


# e = Employee("Alice", "Developer", 70000)
# print(e.show_name())
# print(e.show_role())
# print(e.show_salary())


# example 2

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def student_info(self):
#         return f"{self.name} studies in Grade {self.grade}"


# class Sports:
#     def __init__(self, sport):
#         self.sport = sport

#     def sports_info(self):
#         return f"Plays {self.sport}"


# class ScholarAthlete(Student, Sports):
#     def __init__(self, name, grade, sport):
#         Student.__init__(self, name, grade)
#         Sports.__init__(self, sport)

#     def athlete_info(self):
#         return f"{self.name} is a scholar-athlete"


# sa = ScholarAthlete("Rohan", "10th", "Football")
# print(sa.student_info())
# print(sa.sports_info())
# print(sa.athlete_info())


# hierarchical 

#example 1 

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def info(self):
#         return f"Vehicle Brand: {self.brand}"


# class Car(Vehicle):
#     def wheels(self):
#         return "Car has 4 wheels"


# class Bike(Vehicle):
#     def wheels(self):
#         return "Bike has 2 wheels"


# class Truck(Vehicle):
#     def wheels(self):
#         return "Truck has 6 wheels"


# c = Car("Toyota")
# b = Bike("Honda")
# t = Truck("Volvo")

# print(c.info(), "-", c.wheels())
# print(b.info(), "-", b.wheels())
# print(t.info(), "-", t.wheels())

#abstraction

#example 

# from abc import ABC, abstractmethod

# class Payment(ABC):  # Abstract class
#     @abstractmethod
#     def pay(self, amount):
#         pass


# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         return f"Paid {amount}$ using Credit Card"


# class PayPalPayment(Payment):
#     def pay(self, amount):
#         return f"Paid {amount}$ using PayPal"


# # Usage
# p1 = CreditCardPayment()
# print(p1.pay(100))

# p2 = PayPalPayment()
# print(p2.pay(200))

#Decorators

# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished function: {func.__name__}")
#         return result
#     return wrapper

# @log
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
