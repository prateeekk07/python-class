# Control Flow->

# conditional statement -- if, elif, else
# iterative statement -- for, while loop
# transfer statement  -- break, continue, pass


# a = int(input("Enter a number: "))  # str
# if a == 20:
#     print("twenty")
# elif a == 30:
#     print("thirty")
# elif a == 40:
#     print("forty")
# else:
#     print("invalid num")

# str, list, tuple, set, frozenset, bytes, bytearray, dict, range
# - iterables

# for num in [10,20,30,40,50]: # i = 
#     print(num)

# for i in range(-6, -2, 2): # 0 3 6 9 12
#     print(i)

# for i in ["a", "b", "c", [1,2,3], "e"][0:5]:
#     print(i)


# print(ord("A")) # 65

# chr(97) - A

# for i in range(97, 123):
#     print(chr(i), end=" ")

# star patterns

# for i in range(1, 11): # 3
#     print("* " * i) 

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A+")
# elif marks >= 75:
#     print("Grade: A")
# elif marks >= 60:
#     print("Grade: B")
# elif marks >= 45:
#     print("Grade: C")
# else:
#     print("Grade: Fail")

# light_color = input("Enter traffic light color (Red/Yellow/Green): ").strip().lower()

# if light_color == "red":
#     print("Stop! Wait until the light turns green.")
# elif light_color == "yellow":
#     print("Slow down and prepare to stop.")
# elif light_color == "green":
#     print("Go! You can proceed.")
# else:
#     print("Invalid color. Please enter Red, Yellow, or Green.")


# Predefined username and password
# correct_username = "admin"
# correct_password = "12345"

# Take user input
# username = input("Enter username: ")
# password = input("Enter password: ")

# # Check credentials
# if username == correct_username and password == correct_password:
#     print("✅ Login successful! Welcome,", username)
# elif username != correct_username:
#     print("❌ Invalid credentials!")
# elif password != correct_password:
#     print("❌ Invalid credentials!")
# else:
#     print("❌ Login failed! Please try again.")


# if True:
#     if True:
#         print("pass")
#     else:
#         print("fail")
# else:
    # fail


# if graduation:
#     if basic comp_kno;
#         if python:
#             if oops:
#                 flask
#             else;
#                 learn oops
#         else;
#             learn basic python
#     else:
#         get some basic knowldge
# else:
#     no entry


# age = int(input("Enter your age: "))
# income = int(input("Enter your monthly income: "))

# if age >= 18:
#     if income >= 25000:
#         print("✅ You are eligible for the loan.")
#     else:
#         print("❌ You must have a minimum income of 25,000.")
# else:
#     print("❌ You must be at least 18 years old to apply for a loan.")





# Predefined users (username: [password, role])
# users = {
#     "admin": ["12345", "Administrator"],
#     "manager": ["mng@2025", "Manager"],
#     "user": ["user@123", "General User"]
# }

# # Get login credentials
# username = input("Enter username: ")
# password = input("Enter password: ")

# # Outer if-elif-else: Check username
# if username in users:
#     # Inner if-elif-else: Check password
#     if password == users[username][0]:
#         print(f"✅ Login successful! Welcome {username}.")
        
#         # Nested role check
#         role = users[username][1]
#         if role == "Administrator":
#             print("🔹 Access granted: Full system control.")
#         elif role == "Manager":
#             print("🔹 Access granted: Manage reports and users.")
#         elif role == "General User":
#             print("🔹 Access granted: View dashboard and profile.")
#         else:
#             print("⚠ Role not recognized.")
#     else:
#         print("❌ Incorrect password.")
# else:
#     print("❌ Username not found.")


# nested for loop
# for i in range(1, 6): # 1
#     for j in range(1, 6):  # 1
#         print(f"{i}-{j}", end=" ") # 11 12 13 14 15 
#     print()

# while loop

# while condition:  # True or False
    # statement

# a = 0
# while a < 10: 
#     a += 1 
#     print(a) 
#     print("Hello") 


# print("before loop")

# while True:
#     user_input = input("Enter your name:- ").lower()
#     if user_input == "aniket":
#         print("Hello Aniket")
#         break
#     else:
#         print("Bye bye", user_input)

# print("After loop")

# count = 1

# while count <= 5: # 1 <= 5
#     if count % 2 == 0:
#         print(count, "is even")
#     else:
#         print(count, "is odd")
#     count += 1


# password = ""

# while password != "admin123": # "" != "admin123"
#     password = input("Enter password: ") # admin123
#     if password != "admin123":
#         print("Wrong password, try again!")

# print("Access Granted ✅")

# for i in "abcdefghi":
#     if i == "d":
#         # TODO: testing is done with dummy data, awaiting for final data
#         pass
#     print(i) # abc
