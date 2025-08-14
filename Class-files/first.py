# print("Hello World")
# print("This is the first file in the Files folder")  # ctrl+?
# print("This file is located in the Files folder")
# print("This path is relative to the current working directory")
# print(2+2)

# numeric
    # integer
    # float
    # complex number

# sequence
    # string
    # list
    # tuple
    # set
    # frozenset
    # range
    # bytes
    # bytearray

# mapping
    # dictionary

# boolean

# NoneType



# Data Types
a = 10 # integer
a = 1564154 # integer
a = 10.5 # float
a = 45416545.41500 # float
a = 1+2j # complex number
a = "hgfvdvvdh6563456244#$%" # string # 'asdas', "adsad", '''asdasd''', """asdasd"""
a = "Python12345" # string
a = "12324" # string

a = [1,2,3,4,5] # list # square brackets
a = ["a", 12, "sdf", 20.5, 1+2j] # list

a = (1, 2, 3, 4, 5) # tuple # round brackets/parantheses
a = ("a", 12, "sdf", 20.5, 1+2j, "hgfhg") # tuple

a = {1, 2, 3, 4, 5,6, 7} # set # curly brackets
a = {"a", 12, "sdf", 1+2j, "hgfhg"} # set

a = {1: "a", 2: "b", 3: "c"} # dictionary # curly brackets with key-value pairs
a = {"name": "John", "age": 30, "city": "New York"} # dictionary

a = True # boolean
a = False # boolean

a = None # NoneType

a = range(1, 11) # range object # 1 2 3 4 5 6 7 8 9 10

a = bytes([4,5,6]) # bytes object
a = bytearray([1,2,3]) # bytearray object
a = frozenset([1, 2, 3]) # frozenset object


# A = 20
# print(a)
# print(A)

# ctrl+j

# E:\Python-B14\Files\first.py
# Files\first.py

# line by line execution
# python case sensitive
# portable
# easy 
# dynamic typing




# Identifiers
# Identifiers rules
# 1. Can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# 2. Cannot start with a digit.
# 3. Cannot contain special characters (e.g., @, #, $, %, etc.).
# 4. Cannot be a reserved keyword (e.g., if, else, for, while, etc.).
# 5. Case-sensitive (e.g., myVar and myvar are different identifiers).
# 6. Should be descriptive and meaningful.
# Examples of valid identifiers
# a = 10
# b = 20

# import keyword
# print(keyword.kwlist)

# and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# name = "ABC"
# num = 10

# sadhbcjshdgcwh = 500

# finally = 20
# print(and)

# 123num = 1245712
# print(_Num_123_)
# var = "Python"
# name = "Shivani"
# language = "Python"


# print(a+2)

# print(a*5)

# print(a)


# Error types
# SyntaxError: Invalid syntax



# mutable and im-mutable
# mutable: list, set, dictionary, bytearray
# im-mutable: int, float, complex, string, tuple, frozenset, bytes, range, None, boolean


# CRUD --> # Create, Read, Update, Delete




# Data Types
a = 10 # integer

a = 1564154 # integer
a = 10.5 # float
a = 45416545.41500 # float
a = 1+2j # complex number
a = "hgfvdvvdh6563456244#$%" # string # 'asdas', "adsad", '''asdasd''', """asdasd"""
a = "Python12345" # string
a = "12324" # string

a = [10,20,30,40] # same data types - homegeneous
# print(a)
# a = [10,20,30,1+2j,50,60.45, "abcd",10, 10, 20, 20] # list 
# a = [10, 20.5, 5+7j, "Python", [4,5,6], (7,8,9), {6,5,8}, frozenset({2,3,6,4,5}), range(0, 70), True, False, {"A": "Apple", "B": "Ball"}, None, bytes([5,6,6]), bytearray([5,6,6])]
# print(a)


# hetrogeneous # square brackets
# print(a)
# a[0] = 100 # update
# a[1] = 500
# del a[3]
# print(a)

# print(a[2:4]) # start:stop(excluded)
# 0th index

# properties of list
# square brackets
# mutable
# index based operation - positive and negative indexing
# ordered collection
# allowed duplicate values
# homegeneous and heterogeneous

# tuple
# im-mutable version of list
# round brackets/paranthesis
# index based operation - positive and negative indexing
# ordered collection
# allowed duplicate values
# homegeneous and heterogeneous

# a = (10,20,30,40,50,60)
# a[0] = 100 # TypeError tuple' object does not support item assignment
# print(a)

# print(a[2])  # IndexError


# print("Hello World")

# IndexError: tuple index out of range


# print(a)
a = ["a", 12, "sdf", 20.5, 1+2j] # list

a = (1, 2, 3, 4, 5) # tuple # round brackets/parantheses
a = ("a", 12, "sdf", 20.5, 1+2j, "hgfhg") # tuple

# set
# curly brace
# duplicates not allowed
# unordered collection
# - mutable
# - no indexing, no slicing
# homegeneous and heterogeneous but supports only immutable data types as elements



# a = {1, 2, 3, 4, 5,6, 7} # set # curly brackets
# a = {"a", 12, "sdf", 1+2j, "hgfhg", 12.545, 12, "12", [4,5,6, 7], {}, } # set
# print(type(a)) # <class 'set'>

# a.add(100)

# a = frozenset([1, 2, 3]) # frozenset object
# a.add(100)
# print()

# print(a[0])
# print(a)

# Properties of dictionary
# curly brackets with key-value pairs
# mutable
# ordered collection
# keys must be unique and immutable data types
# no indexing

# a = {1: "a", 2: "b", 3: "c"} # dictionary # curly brackets with key-value pairs
# print(type(a)) # <class 'dict'>
# l1 = [1, 2, 3] # mutable
# a = {l1: "John", "age": 30, "city": "New York", [100,2,3]: "Cena"} # dictionary
# print(a)

# lst = [1, 2, 3, 4, 5]
# lst[0] = 100
# print(lst)


# print(a)
# print(a)
# # print(a["city"])
# a["age"] = 31 # update
# print(a)


# a = True

# if True == True:
#     print("Valid")



a = True # boolean
a = False # boolean

a = None # NoneType

# a = range(1, 11) # range object # 1 2 3 4 5 6 7 8 9 10

# print(list(range(1, 1001)))

# type casting

# a = 10
# print(a)
# print(type(a))  # <class 'int'>
# b = str(a)
# print(b)
# print(type(b))  # <class 'str'>
# a = "abcd"
# print(a, type(a))
# b = int(a)
# print(b, type(b))

# a = "abcdefghijklmnopqrstuvwxyz"
# print(list(a))

# lst = [10,20,30,40,50,60,70,80,90,100]
# print(len(lst)) # 10

# t1 = (10,20,30,40)
# print(list(t1))



# task
# type casting


# operators
# Arithmetic operators
# 5. Assignment operators
# 2. Relational Operators or Comparison Operators
# 3. Logical operators
# 6. Special operators

# 4. Bitwise oeprators

# a = 154
# b = a**5
# print(b)

# a = "#"
# b = "@"
# print(a+b)  # operand


# a = 20
# # a = a + 10
# a *= 10  # a = a + 10
# print(a)

# special operators
    # membership operator - in, not in 
    # identity operator - is, is not

# print("100" not in {"10": "Ten", 20: "Twenty", 30: "Thirty"})  # True

a = 10
print(hex(id(a)))