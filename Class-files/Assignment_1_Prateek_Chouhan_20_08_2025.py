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



# if, elif, else

#if

# a = 21

#example 1
# if a==18:
#    print("hello world") #hello world only if a is equal to 18

#example 2
# games = ["rdr2","forza horizon","GTA"]

# if "rdr2" in games:
#     print("yes the game is in list")

#example 3
# num = 0

# if num != 1:
#     print("it is 0")



#if-else

#example 1
#if a <= 20:
#    print("you are correct")
#else:
#    print("you are wrong") 

#example - 2
#age = int(input("please enter your age"))

#if age >= 18:
#    print("you can drive the bike")
#else:
#    print("you are noob")

#example - 3

# switch = True

# if switch == True:
#     print("switch is ON")
# else:
#     print("switch is OFF")

#example - 4

# Player_name = "Cristiano Roanldo"

# user_input = input("Please enter player name")

# if user_input.lower() == Player_name.lower():
#     print(f"you are a {Player_name} Fan")
# else:
#     print(f"you are not a {Player_name} Fan")

#example - 5

# order = ["burger","cold coffee","french fires"]

# if "burgerr" in order:
#     print("order contains burger")
# else:
#     print("items missing in order")

#if else if

#example - 1

#marks = int(input("please enter your marks"))

#if marks >= 90:
#    print("you are top 1%")
#elif marks >= 80:
#    print("you are top 10%")
#elif marks >= 70:
#    print("you are top 30%")
#elif marks >= 60:
#    print("you are top 50%")
#else:
#    print("you are fail")

#example - 2

# username = "prateek"
# password = "p1234"

# entered_user = input("Enter username: ")
# entered_pass = input("Enter password: ")

# if entered_user == username and entered_pass == password:
#     print("Login successful!")
# elif entered_user == username and entered_pass != password:
#     print("Incorrect password.")
# else:
#     print("User not found.")

#example - 3

# temperature = 10

# if temperature > 35:
#     print("It's very hot")
# elif temperature > 20:
#     print("Nice weather")
# elif temperature > 10:
#     print("A bit cold")
# else:
#     print("Freezing")


#example - 4

# choice = input("Choose your coffee (espresso/latte/cappuccino): ").lower()

# if choice == "espresso":
#     print("Here’s your strong espresso")
# elif choice == "latte":
#     print("Here’s your creamy latte")
# elif choice == "cappuccino":
#     print("Here’s your frothy cappuccino")
# else:
#     print("Sorry, we don’t serve that drink")

# for and while loop

# for with all iterables

#list

# l1 = ["das",5415,"ttt",989,122,"aawd"]

# for i in l1:
#     print(i, end=" ") #das 5415 ttt 989 122 aawd 

#tuple 

# t1 = (2143,"rrt","dasd",98764,(88,99),"gg")

# for i in t1:
#     print(i , end="|") #2143|rrt|dasd|98764|(88, 99)|gg|

#range 

# for i in range(100):
#     print(i,end="-") #0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-18-19-20-21-22-23-24-25-26-27-28-29-30-31-32-33-34-35-36-37-38-39-40-41-42-43-44-45-46-47-48-49-50-51-52-53-54-55-56-57-58-59-60-61-62-63-64-65-66-67-68-69-70-71-72-73-74-75-76-77-78-79-80-81-82-83-84-85-86-87-88-89-90-91-92-93-94-95-96-97-98-99-

#string

# marvel = "i am batman"

# for i in marvel:
#     print(i, end="") #i am batman


#for loop with if statement

#example 1
# l1 = [11,22,33,44,55,66,7,88,99]

# for i in l1:
#     if i == 7:
#         print(f"breaking the loop for {i}")
#     else:
#         print(i)
# 11
# 22
# 33
# 44
# 55
# 66
# breaking the loop for 7
# 88
# 99

#example 2
# t1 = (321,3425,132,"ads",6521,34,"ttt")

# for i in t1:
#     if type(i) == str:
#         print(f"you are printing a string {i}")
#     else:
#         print(i)

#example 3
# games = ["gta","batman","fifa"]
# user_email = input("Please enter your stored game").lower()


# for i in games:
#     if i == "gta" and i == user_email:
#         print("you are gta game")
#     elif i == "batman" and i == user_email:
#         print("you are into batman game")
#     elif i == "fifa" and i == user_email:
#         print("you are into fifa game")

#while loop with ifinite

# while True:
#     print("This will run forever!")

#while loop wit counter

# c = 1

# while c <= 10:
#     print(c)
#     c += 1


#for loop with pass, continue, break

# for i in range(10):
#     if i == 5:
#         pass #will do nothing
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue #will skip it 
#     print(i)


# for i in range(100):
#     if i == 50:
#         break #will break the loop
#     print(i)

#while loop with pass, continue, break

# i = 0
# while i < 20:
#     if i == 16:
#         pass  # placeholder, loop just continues normally
#     print("Number:", i)
#     i += 1

# i = 0
# while i < 5:
#     i += 1
#     if i == 2:
#         continue  # skip printing when i = 2
#     print("Number:", i)

# i = 0
# while i < 5:
#     if i == 3:
#         break  # exit loop when i = 3
#     print("Number:", i)
#     i += 1
