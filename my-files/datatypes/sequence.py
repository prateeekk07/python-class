#sequence datatypes

#string

fullname = "Prateek Chouhan"

print(fullname) #Prateek Chouhan

#list

fruites = ["apple","orange","banana","jaamun"] 

print(fruites) #['apple', 'orange', 'banana', 'jaamun']

ids = [55,84,44,1,5,44]

print(ids) #[55, 84, 44, 1, 5, 44]

#tuple

cars = ("i20","nexon","baleno","jaguar","g-wagon")

print(cars) #('i20', 'nexon', 'baleno', 'jaguar', 'g-wagon')

tids = (45,12,22,32,98,3,6)

print(tids) #(45, 12, 22, 32, 98, 3, 6)

#set 

games = {"cricket","football", "pickleball"}

print(games) #{'football', 'cricket', 'pickleball'} unordered

localids = {23,324,1234,44,312,12}

print(localids) #{1234, 324, 23, 312, 12, 44} unordered

#frozenset

pcparts = frozenset(["ram","ssd","graphics card","motherboard"])

print(pcparts) #frozenset({'graphics card', 'ram', 'motherboard', 'ssd'})

pcspecs = frozenset([45,22,11,32,41,88,99,45])

print(pcspecs) #frozenset({32, 99, 41, 11, 45, 22, 88})

#range

r = range(1,10)

print(r) #range object 1 2 3 4 5 6 7 8 9 

#byte

a = bytes([4,5,6]) # bytes object

#bytearray

b = bytearray([1,2,3]) # bytearray object
