# set
# curly brace
# duplicates not allowed
# unordered collection
# - mutable
# - no indexing, no slicing
# homegeneous and heterogeneous but supports only immutable data types as elements

s1 = {515,54,54,541,88,88}
# print(s1) #{88, 515, 541, 54}

# s2 = {"ad",342,5.8,"98"}
# print(s2) #{'98', 'ad', 5.8, 342}

# s3 = {[3214],(3434)}
# print(s3) #TypeError: unhashable type: 'list'

print(dir(s1))