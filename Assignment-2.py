

# Assignment - 2

# (Q_1) Write a Python program to get a list, sorted in increasing order by the last 
# element in each tuple from a given list of non-empty tuples



# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# a1 = list[a]
# a.sort()
# print(a1)
# a= list[a1]

# print(a)
def last (n):
    return n[-1]
def sort(tuples):
    return sorted(tuples, key=last)
a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print('sorted')
print(sort(a))

# a = [(0,1), (2,4), (3,3), (2,2)].sort()
# n =[list(i) for i in a]
# print(n)




# (Q_2) Write a Python program to print a dictionary whose keys should be the alphabet from a-z and 
#   the value should be corresponding ASCII values

my_dict = {}
for i in range(97, 97 + 26):
    my_dict[chr(i)] = i
print(my_dict)


