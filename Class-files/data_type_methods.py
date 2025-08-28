a = "Do you-want me to-also show-real-world web-application"
# lst = a.split("-")
# print(lst)
# print(a.index("Z"))
# print(a.find("o", 2, 5)) # index if char present, nahi hai to -1

# a = "sd f e ve  c e vfrrewgrtg "

# usr_inp1 = input("Enter first:- ")
# usr_inp2 = input("Enter second:- ")
# new = f"Hi All This is {usr_inp1}.. I am here to guide {usr_inp2}."
# print(new)
# print(new.format("Vishnu", "You"))


# print(id(a))
# s1 = a.replace("show", "see")
# print(id(s1))

 # immutable -- 


# lst = ["a", "b","c","d"]
# s1 = "-".join(lst)
# print(s1)

# s1 = "abcd"
# print(list(s1))


# print(a.endswith("Do you want me to also show real-world web application"))



# print(a.title())  a-z, A-Z, 0-9
# print(a.isalnum()) # True or False

# print(dir(a)) # 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill'

# list methods

# print(dir(l1))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# DRY - Don't Repeat Youself

# copy, clone, alias, shallow copy, deep copy

# l1 = [10,20,30,40,50,60,70]
# l2 = l1
# l3 = l2
# l2 = l1[::] # mem diff
# l3 = l1[::]

# l1[0] = 100
# print(l1)
# print(l2)
# print(l3)

# alis -- memory loc sam
# clone -- memory loc diff
# copy -- memor loc diff
import copy

# l1 = [10,20,30,40,["a", "b", "c"]]
# l2 = copy.deepcopy(l1) # shallow copy

# print(id(l1[4]), id(l2[4]))
# l1[4][0] = "A"
# print(l1)
# print(l2)

# print(l1[4][3])



# print(l1[::]) # start:stop:stepsize






# print(l1.index("20"))

# l1.insert(5, "Python")
# print(l1)
# l1[0] = 400

# del l1[0]

# l1.remove()
# print(l1)


# removed_element = l1.pop(-2)
# print(removed_element)
# remove last element by default if index is not provided
# remove the element which is present on provided index position
# if provided index does not exist, IndexError pop index out of range




# l1.pop()
# l1.pop()
# print(l1)

# l1.reverse()
# print(l1)
# l1.sort(reverse=True) # ascending/descending
# print(l1)

# print(l1.count(50))
# l1.clear()
# print(l1)
# l1.extend([1,2,3,4]) # extend --> iterable - string, lst, 
# print(l1)
# l1.append([1,2,3,4,5])
# print(l1)
# l1.append(50)  # add at last
# print(l1)
# l1.append(60)  # add at last
# print(l1)
# l1.append(70)  # add at last
# print(l1)

# print(l1[8])
# l1[0] = 100
# print(l1)



# print(l1, id(l1), type(l1))


# KISS -> keep it simple stupid

# set
# set()
# {}

# s1 = {10,20,30,40} # set()
# s2 = {30,40,50,60}
# s3 = s1.intersection(s2)    # + --> union, - (difference)
# print(s3)
# s1.pop()
# s1.remove(20)
# print(s1)

# print(dir(s1))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update
# s1.clear()
# print(s1)

# s1.add()
# s1.update(100) # extend
# print(s1)

# no index
# key value pair
# no duplicate key
# key should be immutable

# dictionary methods
# d1 = {"name": "ABC", "age": 25, "city":"Pune", "salary": 65000}
# print(d1.pop("name11")) # del d1["name"]
# d1.popitem()
# d1.popitem()
# d1.popitem()
# d1.popitem()
# d1.popitem()

# print(d1)
# key_value_pair = list(d1.items())
# print(key_value_pair)

# d3 = {}.fromkeys(["a", "b", "c", "d", "e"], "")
# print(d3)

# print(d1.setdefault("company", "infy"))
# d2 = d1.copy()
# print(id(d1), id(d2))
# print(d1)
# d1.clear()
# print(d1)
# all_values = list(d1.values())
# print(all_values)

# value = d1.get("name", 0)
# print(value)

# del d1["name"]
# d1["company"] = "Infy"
# d1["surname"] = "xyz"
# d1["mobile"] = 514514548
# d1["name"] = "abc"

# print(d1)
# d2 = {"company": "Infy", "surname": "xyz", "mobile": 5454441848}
# d2.update(d1)
# print(d2)

# print(d1)
# d1["company"] = "Infy"
# print(d1)

# print(d1.get("company", "TCS"))
# print(d1["name"])

# print("After")

# print(d1["company"]) # d1["key"] - nahi hai to KeyError


# print(dir(d1))
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


# (p[])
# l1 = [10,20,30, ("a", "b", "c")]
# l1[3] = "Python"
# print(l1)


# l1 = []  # list()
# for i in range(10, 51):
#     l1.append(i)
# print(l1)

# l2 = list(range(10, 51))
# print(l2)

# list comprehension
# l1 = [i for i in range(10,51)]
# print(l1)

# letters = [chr(i) for i in range(97, 123)]
# print(letters)

# letters = []
# for i in range(97, 123):
#     letters.append(chr(i))
# print(letters)

# lst = [i for i in range(1, 51) if i%3==0]
# print(lst)

# lst = []
# for i in range(1, 51):
#     if i%3 == 0:
#         lst.append(i)
# print(lst)

# set {}

# {a: "A", "b": "B"}

# d = {}
# d["name"] = "abcd"
# d["age"] = 25
# for i in range(1, 27):
    # d[chr(96+i)] = chr(64+i)
# print(d)

# d1 = {chr(97+i): chr(65+i) for i in range(0, 26)}
# print(d1)

# original_lst = [[1,2,3, ["a", "b"]], [4,5,6], [7,8], [9],[]]

# flattened_lst = []

# for lst in original_lst:
#     for j in lst: # []
#         flattened_lst.append(j)

# print(flattened_lst)

# lst = [(1,2), (3,4), (5,6), (7,8)]
# for i, j in lst:
    # print(i, j)
# list of tuple

# d1 = {"name": "ABC", "age": 25, "city":"Pune", "salary": 65000}
# for key, value in d1.items():
#     print(key, "--", value)

# student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
# inverted = {v: k for k, v in student_scores.items()}
# print(inverted)

# t1 = tuple((i for i in range(1, 11)))
# print(t1) # generator