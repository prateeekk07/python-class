# def function_name(parameters):
#     """docstring (optional): describes what the function does"""
#     # function body
#     return value

# def → keyword to define a function

# function_name → identifier (must follow variable naming rules)

# parameters → inputs (optional)

# return → sends result back to the caller (optional)

#Simple function example
# def greet():
#     print("Hello Sir")
# greet()

#function example with parameter
# def greet(name):
#     print(f"Hello {name}")

# greet("prateek")

#function example with return

# def num1(n):
#     return n

# b = num1(5)
# print(b)

#function example of default parameter

# def switch(s="off"): #default value
#     print(f"switch is {s}")

# switch() # uses default "Guest"
# switch("on") # overrides default

#functions with multiple return values

# def table(a,b):
#     sum = a + b
#     sub = a - b
#     mul = a * b
#     return (f"sum = {sum}, sub = {sub}, mul = {mul}")

# final_result = table(5,4)

# print(final_result)

#variable length arguments(*args & *kwargs)

# def number(*args):
#     # for i in args:
#     #     print(i,end="")
#     print(type(args))

# number(1,2,3,6,5,8)

# def username(**kwargs):
#     print(kwargs)

# username(name = "yashi",age=17)