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

# list = []
# print(dir(list))

#'append','insert, 'clear', 'copy', 'count', 'extend', 'index', ', 'pop', 'remove', 'reverse', 'sort']

# Add → append, extend, insert
# l1 = [34,55,77,44,322,33,88]
# l2 = [5,6,9,0]

# l1.append(99)
# print(l1)
# l1.extend(l2)
# print(l1)
# l1.insert(6,"abhijeet")
# print(l1)

# Remove → pop, remove, clear

# out=l1.pop(3)  we can do it with index value #stores 44 the value as well
# print(l1) #[34, 55, 77, 322, 33, 88]

# l1.remove(44) #we can do it with index value #no value stored in this
# print(l1) #[34, 55, 77, 322, 33, 88]

# l1.clear()
# print(l1) #[]

# Info → index, count

# Order → reverse, sort
l1 = [34,55,77,44,322,33,88]
l2 = [5,6,9,0]

l1.sort()
l1.sort(reverse=True) 
print(l1)


# Copy → copy






