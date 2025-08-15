print("Hello World")

# Numeric
    # integer
    # float
    # complex number

# Sequence
    # string
    # list
    # tuple
    # set
    # frozenset
    # range
    # bytes
    # bytearray

# Mapping
    # dictionary

# Boolean

# NoneType

fullName = "Prateek" #string 

phoneNumber = 9856213012 #integer

currency = 65.5 #float

abc = 55+65j #complex number

fruits = ["orange","mango","cherry","banana"] #list

cars = ("xuv","i20","g-wagon","thar") #tuple

r = range(1,11) #range 1 2 3.. 10

biks = {"pulsar","bullte","apache"} #set

userInfo = {"name": "prateek", "age" : 18, "email" : "prateek@abc.com"} #dict (key value pair)

switch = True #boolean 

empty = None #Nonetype

ghg = bytes([4,5,6]) # bytes object
yhy = bytearray([1,2,3]) # bytearray object
ada = frozenset([1, 2, 3]) # frozenset object


# Identifiers rules
# 1. Can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# 2. Cannot start with a digit.
# 3. Cannot contain special characters (e.g., @, #, $, %, etc.).
# 4. Cannot be a reserved keyword (e.g., if, else, for, while, etc.).
# 5. Case-sensitive (e.g., myVar and myvar are different identifiers).
# 6. Should be descriptive and meaningful.


# mutable and im-mutable
# mutable: list, set, dictionary, bytearray
# im-mutable: int, float, complex, string, tuple, frozenset, bytes, range, None, boolean



#properties of list
    #square brakets
    #index based operation
    #mutable 
    #allowed duplicate values
    #order colection

a = [12,23,12,23,34,123,32414]
a[0] #12
c = a[2:5] #[12, 23, 34]
print(c)

#properties of tuple
    #inmutable version of list
    #round brackets/paranthesis
    #index based operation
    #ordered collection
    #allowed duplicate values

#properties of set
    #curly brace
    #duplicate values not allowed
    #unordered colection
    #mutable
    #no indexing,no slicing
    #homegenous and hetrogeneous 

#properties of dict
    #curly brackets with key-value pairs
    #mutable
    #ordered collection
    #keys must be unique and immutable datatypes
    #no indexing

#hello i am making some changes

#memory location 
numb1 = 10000 
numb2 = 4314
list1 = [32,23,23,23]
list2 = [32,23,23,23]

print(id(numb1)) 
print(id(numb2))

#operators

#identity operators (is, is not) memory address comparison
print(numb1 is numb2) #false
print(numb1 is not numb2) #true
print(list1 is list2) #false

#Comparison (Relational) Operators content comparison
print(list1 == list2) #true
print(list1 != list2) #false
print(numb1 > numb2) #true

#logical operators 
print(not ["das","da"]) #false
print(not "") #true

#control flow
#conditional statement-- if, elsif, else
#iterative statement-- for, while loop
#transfer statemen-- break,continue, pass 