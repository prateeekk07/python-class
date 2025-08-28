# user defined functions


# students data  -- 100


# def funcion_name(args):
#     statements

# print("before defining greet")
# def greet(): # function
#     print("Hey")
#     print("Good Evening")
#     print("How are you!")
#     print("##############")

# print("after defining greet")
# print(id(greet))
# print("before calling greet")
# greet() # call the function
# print("after calling greet")
# greet()
# greet()


#interview: function first class object
# - function can be taken as argument
# - function can return a function
# - function can be assigned to a variable

# function me koi return statement nahi hai 
# to None
# return 

# def square(num):
#     print(num**2)

# lst = [square(1), square(2), square(3)]
# print(lst)
# res = square(10)
# print(res)



# my_dict = {}
# for i in range(1, 51): # 1
#     my_dict[i] = square(i)
# print(my_dict)



# res = square(10)
# print(res)
# res = square(25)
# print(res)
# res = square(45)
# print(res)
# res = square(65)
# print(res)





# lst = [square(), square(), square()] # None, None, None
# print(lst)
# for index, _ in enumerate(range(1, 11), start=1):
#     print(index)
#     square()







# if condition:
    # statem


# for var in iterables:
    # statemen

# can we have multiple return statement inside a function

# def square_dict(num):
#     if not isinstance(num, int):
#         return "Invalid number passed. Only integer supported."
#     my_dict = {}
#     for i in range(1, num+1): # 1
#         my_dict[i] = i**2 
#     return my_dict

# res = square_dict("asd")
# print(res)

# task --> square, cube

# def square_dict(num):
#     if not isinstance(num, int):
#         return "Invalid number passed. Only integer supported."
#     return {i**2 for i in range(1, num+1)}
# l1 = [10,20,30]

# res = square_dict("asd")
# print(res)



# def func():
#     return "a", "b", "c", [1,2,3], (4,5,6), 1454

# res = func()
# print(res)


# ternary operator


# a = 10
# def func():
#     return "Hello"

# print(globals())
# res = func
# res1 = res
# print(res1())


# 25-08-2025

# def func():
#     return "abc"


# res = func()
# print(res)

# arguments
# formal
# actual
#  - positional
#  - default
#  - keyword
#  - variable length
#  - variable length keyword

#  - positional
# def func(a, b, c):
#     print("inside function")
#     print(a, b, c)

# func(10, 20, 30)


#  - default
# def func(a, c, b=20): # default arg
#     print("inside function")
#     print(a, b, c)

# func(10, 30)

#  - keyword

# def func(a, b, c, d, e=100):
#     print(a, b, c, d, e)

# func(900, c=30,b=20,d=40) # 

# variable length arg - min 0, max - infinite
# def func(a,b,c,d=100, *args): # 
#     print("positional:- ", a, b, c, d)
#     print(args) # tuple
#     print(sum(args))

# func(10,20,30)

# 5! = 5*4*3*2

# def multiplication(*args):
#     n = 1
#     for i in args:
#         n *= i # 
#     print(n)

# multiplication(20,50,40,10,1,6)


# variable length keyword
# dict
# def func(var1, var2, *args,**kwargs): # min -0, max - infinite
#     print(var1, var2)
#     print("args", args)
#     print("kwargs", kwargs)

# func(1,o=2,q=3,z=4, a=10,b=20, c=30, d=40, e=100)


# Example 1
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# student_info(name="David", age=22, course="Python")

# Example 2
def print_details(**details):
    print("Details received:")
    for k, v in details.items():
        print(f"{k} -> {v}")

# print_details(city="Bangalore", language="Python", level="Beginner")


def demo_function(name, age, city="Delhi", *args, country="India", **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Country: {country}")
    
    if args:
        print("Hobbies:", args)
    
    if kwargs:
        print("Extra Info:", kwargs)

# Call 1
# demo_function("Alice", 25, "Mumbai", "Reading", "Music", country="USA", profession="Engineer", married=False)

# print("----")

# Call 2
# demo_function("Bob", 30, hobby="Cricket", skill="Python")


def log(message, level="INFO", timestamp=True):
    from datetime import datetime
    prefix = f"[{datetime.now()}] " if timestamp else ""
    print(f"{prefix}{level}: {message}")


# def func(a, b, c):
#     print(sum([a,b, c]))

# func(10,20,30)
# log("called addition func with values")
# l = [12,2,5,[1,2,2]]



# print("started") # 1
# print("before defining func1") # 2
# def func1():
#     print("inside func1")
#     def func2():
#         print("inside func2")
#     print("before func2 call")
#     func2()
#     print("after func2 call")

# print("before func1  call")
# func1()
# print("after func1  call")
# print("completed")


# JUGAD

# def func1():
#     print("inside func1")
#     def func2():
#         print("inside func2")
#         return "abcd"
#     return func2()  # memory location

# res = func1() # func2 memory location
# print(res) # 

# closure

# def func1():
#     print("inside func1")
#     def func2():
#         print("inside func2")
#         return "abcd"
#     return func2

# res = func1() # func2 memory location
# print(res) # 


# variables 
    # - global
    # - local
    # - nonlocal

z = "zebra"
# a = 10  # global variable
# print(a)
def func():
    global z
    z = "zepto"  
    z = "zzzz"
    print(z) # local

# func()
# print(z) # zebra

# print(a)
# a = 20
# l = [a, a, a]
# print(l)


# decorators
# recursive


# interview: function first class object
# - function can be passed as argument to another func
# - function can return a function
# - function can be assigned to a variable
# - function can be stored in any datatype



# def func():
#     print("inside func")


# l = [func(), func(), func()]
# print(l)



def add(a, b):
    return a+b

def substract(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a//b

# lst = [add, substract, multiplication, division]

# for f in lst:
#     print(f.__name__, f(20, 10))


def func(fn): # fn --> greet ka memory location
    return fn() + " How are you"

def greet():
    return "Hello Everyone! "

res = func(greet)
print(res)

