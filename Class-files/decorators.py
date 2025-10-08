
# closure

# def outer(f_adr): # f_adr--> func memory address
#     print("outer")
#     def inner():
#         print("*"*10) # *
#         f_adr()
#         print("*"*10)
#     return inner

# @outer  # outer(func)  # outer(func)
# def func(): # func:- inner
    # print("Hello Everyone!!")

# print(func)
# func()

# outer(func)()


# def outer(f): # f --> addition address
#     def inner(v1, v2):
#         print("calling function")
#         f(v1, v2) # 10, 20
#         print("called function")
#     return inner

# @outer   # --> outer(addition) --> returned inner address
# def addition(a, b):  # addition --> inner
#     print(a+b)

# addition(10, 20)


# def upper(f): # f --> test_string address
#     def inner(s1):
#         returned_string = f(s1)  # "prateek"
#         print(returned_string.upper())
#     return inner

# # @upper  # upper(test_string)  --> returned inner address
# def test_string(s):  # test_string --> inner
#     return s

# test_string("prateek") # inner("prateek")



# monkey patching

# def func1():
#     print("in func1")

# def func2():
#     print("in func2")

# func2 = func1

# func1()
# func2()

# a = 10
# b = 10
# c = b


class Calculator:
    def add(self, x, y):
        return x + y

# c = Calculator()
# print(c.add(2, 3))  # 5

# # Monkey patch: replace 'add' method at runtime
# def new_add(self, x, y):
#     print("Adding numbers differently")
#     return x + y + 10

# Calculator.add = new_add   # patch

# print(c.add(2, 3))  # Adding numbers differently -> 15


# 
# print("start")
# import time
# time.sleep(4)

# print("end")
import time

# t1 = time.time() # 10
# print(t1)
# time.sleep(2) # 2
# t2 = time.time() # 12
# print(t2)
# print(t2-t1)


# def time_execution(f):
#     def inner():
#         t1 = time.time()
#         f()
#         t2 = time.time()
#         print(f"Time taken by {f.__name__} is {t2-t1}")
#     return inner


# @time_execution
# def time_taking_func1():
#     time.sleep(4)
    
# time_taking_func1()
# @time_execution
# def time_taking_func2():
#     time.sleep(2)

# time_taking_func2()

# @time_execution
# def time_taking_func3():
#     time.sleep(7)

# time_taking_func3()



# credentials = {"sanchita": "sanchita@123", "saad": "saad@456", "rohit": "Rohit@789", "surbhi": "surbhi@4862"}


# def authenticate(f):
#     def wrapper(usrnm, passwd):
#         if credentials.get(usrnm) == passwd:
#             f(usrnm, passwd)
#         else:
#             print("Invalid Credentials!!")
#     return wrapper


# @authenticate
# def login(username, password):
#     print("Login successfull!!")


# login("sanchita", "sanchita@123")


# class based decorators

class MyDecorator:
    def __init__(self, func): # say_hello
        # this runs when the decorator is applied
        self.func = func   # say_hello

    def __call__(self, *args, **kwargs): # 
        # this runs when the decorated function is called
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result

# @MyDecorator
# def say_hello(name): # MyDecorator object
#     print(f"Hello {name}!")

# # print(say_hello)
# say_hello("HIIII") # MyDecorator object
# say_hello("Shivali")

# class Student:
#     def __call__(self):
#         print("in call method")

# obj = Student()
# obj()


# def decor:
#     print("funcio ", a)
    #  def inner(a, b, c):
    #     if 

# def func(a, b, c):
#     pass



