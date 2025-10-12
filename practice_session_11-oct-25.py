# var = "a" #allowed
# s_no = 1 #allowed
# 1var = 10 #not allowed
# 4@name = "abc" #not allowed
# _salary = 50000 #allowed
# name1 = "Prateek" #allwoed
# ab%c = "hello" #not allowed
# batchno_ = 7 #allowed 



#Methods of data types

# #numric
# int 
# float
# complex

# #squence
# string
# tuple
# list
# set
# frozenset
# bytearray
# range

# #mapping
# dict

# #bolean true false


# name = "praTeek"
# name1 = " The dog is runing  "


# print(name.lower()) #prateek
# print(name.upper()) #PRATEEK
# print(name.count("e")) #2
# print(name.capitalize()) #Prateek
# print(name.startswith("a")) #false
# print(name.endswith("k")) #true
# print(name.index("T")) #3
# print(name1.split(" ")) #['The', 'dog', 'is', 'runing']
# print(name1.lstrip()) #The dog is runing
# print(name1.rstrip()) #The dog is runing
# print(name1.replace("dog","cat")) #The cat is runing

# l1 = [44,55,66,22,12,10,44,85]
# print(dir(l1))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


# l1.append(("prateek",(66,55)))
# l1.append({5,10,(55,12)})
# l1.append({"sno.":"23"})
# l1.append("hello")
# l1.append(True)
# print(l1)

# l1 = [44,55,66,22,12,10,44,85]
# l1.extend(["abhijeet","ganesh",(9,0,1),{"name":"raju"}])
# l1.extend((77,89,10))
# l1.extend({"updated":"mehul","salary":5000})
# l1.extend("PRATEEK")
# print(l1)

# l1 = [44,55,66,22,12,10,44,85,{"name":"prateek"},(66,88,77)]
# l1.insert(1,66)
# l1.insert(0,{"name": "prateek"})
# l1.insert(4,(9,0,77,1))


# l1 = [44,55,66,22,12,10,44,85,{"name":"prateek"},(66,88,77)]
# print(l1.pop(8))
# l2 = l1.pop()
# print(l1)

# l1 = [44,55,66,22,12,10,44,85]

# l1.remove((66,88,77))
#l1.remove({"name":"prateek"})
# l1.remove(44)
# print(l1)

# l1 = [44,55,66,22,12,10,44,85]
# l1.sort()
# l1.sort(reverse=True)
# print(l1)

# l1.clear()
# print(l1)

# new_list = l1.copy()
# print(new_list)


# s1 = {55,"sa","kl",66,88,(9,0)}

# s1.add(11)
# s1.add((78,99))
# s1.add("gahe")
# print(s1)

# s1.remove("kl")
# s1.pop()
# print(s1)



# d1 = {"name":"Prateek", "salary":50000, "job":"sd"}
# print(dir(d1))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


# d1 = {"name":"Prateek", "salary":50000, "job":"sd"}
# res = d1.keys()
# res = d1.values()
# res = d1.pop("name")
# print(res)
# res = d1.popitem()
# print(res)

# d1 = {"name":"Prateek", "salary":50000, "job":"sd", "education": ""}
# d1.update({"name":"abhijeet", "education": "MBA"})

# key = d1.get("salary")
# value = d1.items()
# print(value)



# a = 77
# b = 55

# if a > b:
#     print("a")
# else:
#     print("b")


# a  = 0

# if a < 9:
#     a = a + 9
# if a < 30:
#     a = a + 3
# else:
#     print("you are wrong")

# print(a)

# age = int(input("enter your age"))

# if age >= 18:
#     print("you can drive")
# else:
#     print("you can not drive")


# username = input("Enter you username")
# role = input("enter your role").lower()

# if role == "admin":
#     print(f"welcome {username}, You have {role} access")
# elif role == "view":
#     print(f"welcome {username}, You have {role} access")
# elif role == "subscribe":
#     print(f"welcome {username}, You have {role} access")
# else:
#     print(f"welcome {username}, You have Do not have any access.")


# for i in "abcdefghijklmnopqrstuvwxyz":
#     print(i, end=" ")

# for i in range(1,10):
#     print(i,end="-")

# for i in {55,66,888,77,0,66}:
#     print(i, end=" ")
    
# lst = [33,56,88,[99,66],55,77,[11,44]]
# for i in lst[3]:
#     print(i,end=",")

# lst = [(33,56,88),[99,66],55,77,[11,44]]

# for i in lst[0]:
#     print(i)

# d1 = {"name":"Prateek", "salary":50000, "job":"sd", "education": ""}

# for i in d1.keys():
#     print(i)

# for i in d1.values():
#     print(i)

# for i in d1.items():
#     print(i)

# l1= [44,55,66,12,22]
# l2 = "abcdefghijk"
# for i in l2:
#     l1.append(i)

# print(l1)


# a = "*"

# for i in range(6):
#     print(i * a)

# for i in range(0, 15, 3):
#     print(i)


# for i in range(97,123):
#     print(chr(i), end="-")


