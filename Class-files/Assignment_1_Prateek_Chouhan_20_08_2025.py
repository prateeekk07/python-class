# Idenrtifiers Rules

#1. Can contain letters (A–Z, a–z), digits (0–9), and underscore (_).
#Ex:rollno_1 , userName, _age.

#2. Cannot start with a digit.
# 1variable (wrong)
# variable1 (correct)

#3. Cannot conatin special characters.
# my-id, roll# (wrong) 

#4. Cannot be a reserved keyword
#if, while, class, for etc. cannot be used as identifiers.

#5. Case-Sensitive
# age, Age, and AGE are three different identifiers.

#6. No spaces allowed
#student name (wrong)
#student_name (correct)

#----------------------------------------

#datatypes

#Numeric datatypes

#Integer  

# numb1 = 123
# numb2 = 234

# print(numb1) #123
# print(numb2) #234

#float

# numb3 = 45.5
# numb4 = 66.6

# print(numb3) #45.5 
# print(numb4) #66.6

#complex numbers

# numb5 = 2+3j

# print(numb5) #2+3j

#----------------------------------------

#sequence datatypes

#string
# Properties of string
# ordered collection
# immutable
# index based and Sliceable

# fullName = "Prateek"
# print(fullName) #Prateek
 
# username = "xyz123"
# u = username[3]
# print(u) #1

# age = "20"
# print(age)

#----------------------------------------

#list

# properties of list
# square brackets
# mutable
# index based operation - positive and negative indexing
# ordered collection
# allowed duplicate values
# homegeneous and heterogeneous

# l1 = [23,"per",34,[54,45,88],{"name":"Prateek"}]

# print(l1) #[23, 'per', 34, [54, 45, 88], {'name': 'Prateek'}]

# print(l1[2]) #34

# print(l1[1:3]) #['per', 34] 3 is excluded

# print(l1[-4:-1]) #['per', 34, [54, 45, 88] -1 is excluded

# l1[0] = 2

# print(l1) #[2, 'per', 34, [54, 45, 88], {'name': 'Prateek'}]

# fruits = ["apple","mango","apple","graphes"]
# print(fruits)

# datatypes  =[True,"string",23,(51,24,51),{"ads","das","fff"}]

# print(datatypes)

#tuple

# tuple
# im-mutable version of list
# round brackets/paranthesis
# index based operation - positive and negative indexing
# ordered collection
# allowed duplicate values
# homegeneous and heterogeneous


# cars = ("das",34132,{"abc" : 123},555)
# c = cars[2]
# print(c) # {'abc': 123}
# print(cars) #('das', 34132, {'abc': 123}, 555)

# movies = ("thor","ironmman", "captain america")
# print(movies) #("thor","ironmman", "captain america")

#set 
# set
# curly brace
# duplicates not allowed
# unordered collection
# - mutable
# - no indexing, no slicing
# homegeneous and heterogeneous but supports only immutable data types as elements

# s1 = {515,54,54,541,88,88}
# print(s1) #{88, 515, 541, 54}

# s2 = {"ad",342,5.8,"98"}
# print(s2) #{'98', 'ad', 5.8, 342}

# s3 = {[3214],(3434)}
# print(s3) #TypeError: unhashable type: 'list'

# games = {"cricket","football", "pickleball"}

# print(games) #{'football', 'cricket', 'pickleball'} unordered

# localids = {23,324,1234,44,312,12}

# print(localids) #{1234, 324, 23, 312, 12, 44} unordered

#frozenset

# pcparts = frozenset(["ram","ssd","graphics card","motherboard"])

# print(pcparts) #frozenset({'graphics card', 'ram', 'motherboard', 'ssd'})

# pcspecs = frozenset([45,22,11,32,41,88,99,45])

# print(pcspecs) #frozenset({32, 99, 41, 11, 45, 22, 88})

#range

r = range(1,10)

print(r) #range object 1 2 3 4 5 6 7 8 9 

h1 = range(-10,-1)
print(h1) #-10, -9, -8, -7, -6, -5, -4, -3, -2



# #byte

# a = bytes([4,5,6]) # bytes object

# #bytearray

# b = bytearray([1,2,3]) # bytearray object



