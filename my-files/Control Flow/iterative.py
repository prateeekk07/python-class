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






