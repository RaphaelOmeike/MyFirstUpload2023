# Lists
# mylist = ["banana", "cherry", "apple"]
# print(mylist)
# mylist2 = [5, True, "apple"]
# Ways to copy all elements of a list to a new list.
# item = mylist[:]
# item2 = mylist.copy()
# item3 = list(mylist)


# te = [1, 2, 3, 4, 7]
# v = [i * i for i in te] # List Comprehension.
# print(v)
# print(len(mylist))
# if "apple" in mylist:
#     print("Yes")
# else:
#     print("No")
# # To add to list
# mylist.append("lemon")

# mylist.insert(1, "blueberry")

# print(mylist)
# # To remove last item and get the value
# item  = mylist.pop()
# mylist3 = [1, 7, 3, 6]
# mylist3.sort()
# new_list = sorted(mylist3)
# print(mylist, mylist3)
# # To remove specified item
# mylist.remove("banana")
# print(mylist)
# yeah = [1] * 3 
# # A list is ordered, mutable and it allows duplicate elements.
# yeah1 = [0 for i in range(3)]
# print(yeah)
# new_yeah = mylist + yeah1
# print(new_yeah)
# # Slicing
# a = new_yeah[::-1] # Trick to reverse list
# n = new_yeah[::2]
# print(a, n)

# Tuple: ordered, immutable, allows duplicate elements, already defined elements cannot be changed.
# mytuple = ("Max", "p", "jay", "jsa", "p")
# mytuple1 = tuple(mylist)
# for item in mytuple:
#     print(item)

# if "Jaf" not in mytuple:
#         print("ooh")
# print(mytuple.count("p"))
# print(mytuple.index("p"))
# Tuples can also be sliced, and they are immutable.
# Unpacking
# my_tuple = "Max", 28, "udhg"
# name, age, place = my_tuple
# print(name)
# mytup = (0, 1, 2, 3, 4, 5)
# i1, *i2, i3 = mytup
# print(i1, i2, i3)
# Working with Tuples is more efficient than Working with Lists

# Dictionaries: Key-Value pairs, Unordered, Mutable
# mydict = {"name": "Max", "age" : 28, "city":"New York"}


# value = mydict["age"]
# mydict["email"] = "max@xyz.com"
# mydict["email"] = "emax@xyz.com"
# To remove elements from a dictionary
# del mydict["city"]
# mydict.pop("age")
# mydict.popitem()
# if "name" in mydict:
#     print(mydict["name"])
# print(mydict)
# for key in mydict.keys(): # To print keys in a dictionary
#     print(key)
# for value in mydict.values(): # To print values in a dictionary
#     print(value)
# for key, value in mydict.items(): # To print key-value pair in a dictionary
#     print(key, "-", value)

# To copy a dictionary
# mydict_cpy = mydict.copy()
# mydict2 = dict(mydict)
# my_dict_2 = dict(name="Mary", age=27, city="Boston")
# To merge a dictionary to another.
# mydict.update(my_dict_2)
# print(mydict, my_dict_2)

#Note that a list cannot be used as a key in a dictionary
#Sets: unordered, mutable, no duplicate elements 
# myset = {1, 2, 3, 1, 2}
# print(myset)
# myset = set("Hello")
# myset1 = set() # For an empty set you declare it like this.
# myset1.add(1) # To add elements to a Set.
# myset1.add(2)

# myset1.remove(2)
# myset.discard(1) # safer
# myset.clear() # To clear the set

# print(myset1.pop()) # remove arbitrary item from the set and return the value

# print(myset1)
# Iterating through elements of a set 
# for x in myset:
#     print(x)

# if 'l' in myset:
#     print("yess")

# Union and Intersection of sets
# odds = {1, 3, 5, 7, 9}
# evens = {0, 2, 4, 6, 8}
# primes = {2, 3, 5, 7}

# u = odds.union(evens)
# print(u)

# i = odds.intersection(primes)
# print(i)
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# setB = {1, 2, 3, 10, 11, 12}

# setB = {1, 2, 3}
# setC = {7, 8}
# diff = setB.difference(setA)
# yeha = setA.symmetric_difference(setB)
# print(diff)
# print(yeha)

# setA.update(setB) # To add a set to an existing set
# setA.intersection_update(setB) # To update a with intersection
# setA.difference_update(setB) # To update a with difference
# setA.symmetric_difference_update(setB) # To update a with symmetric

# print(setA)

# Subset and superset methods
# print(setB.issubset(setA)) # Returns boolean value
# print(setB.issuperset(setA))

# To Check if two sets are disjoint i.e have no intersection
# print(setB.isdisjoint(setC))

# To Actually Copy a set
# setB = set(setA)
# setB =  setA.copy()
# print(setB)


# The frozen set - immutable type/version of set Union, intersection and difference methods only would work.
# # a = frozenset([1, 2, 3, 4])
# print(a)

# Diamond triangle
# i = 1 
# input = 6
# while i < input:
#     print(" " * (input - i), "# " * i)
#     i += 1

# Strings: ordered, immutable, text representation
# my_string = """Hello \
# World"""
# print(my_string)

# my_string = "Hello World" + "tom"
# char = my_string[::-1]
# print(char)
greeting = "Hello    "
print(greeting.strip()) # Doesn't change original string in place unless assigned
# if "oell" in greeting:
#     print("Yes")
# String Methods.
# print(greeting.upper())
# print(greeting.startswith("H"))
# print(greeting.endswith("f"))
# print(greeting.find("oello")) # returns -1 if not found
# print(greeting.count("l"))
# my_string = "Hello World"
# print(my_string.replace("World", "Nigeria"))
# hdbf = "how,are,you,doing"
# my_list = hdbf.split(",") # These are very useful
# print(my_list)
# new_string = " ".join(my_list) # Converting a List to a string. It is a very important method.
# print(new_string)

# Itertools Contd
# Combinations
# from itertools import permutations
# b = [1, 2, 3, 4]
# perm = permutations(b, 2)
# print(list(perm))
# from itertools import combinations, combinations_with_replacement 
# combination with replace ment allows for repitition of same number twice
# no repititions
# a = [1, 2, 3, 4]
# comb = combinations(a, 2) # Length argument is compulsory
# print(list(comb))
# comb_wr = combinations_with_replacement(a, 2)
# print(list(comb_wr))

# Stopp

# Accumulate Computes sums of elements by default, compares elements and performs operation on it
# from itertools import accumulate
# import operator
# a = [1, 2, 5, 3, 4]
# # acc = accumulate(a, func=operator.mul)
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))

# Group by returns keys from an iterable
# from itertools import groupby

# a = [1, 2, 3, 4]
# group_obj = groupby(a, key=lambda x: x < 3)
# for key, value in group_obj:
#     print(key, list(value))

# Count, cycle, repeat
from itertools import count, cycle, repeat
a = [1, 2, 3]
# for i in count(10):
#     print(i)
#     if i == 15:
#         break
# for i in cycle(a):
#     print(i)

# for i in repeat(1, 4):
#     print(i)

# Lambda arguments: expression | simpler functions 
# add10 = lambda x: x + 10
# print(add10(5))

# mult = lambda x, y: x * y
# print(mult(2, 7))

# sorted method with lambda
# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D, key= lambda x: x[0] + x[1])
# print(points2D)
# print(points2D_sorted)

# map function map(function, sequence)
# a = [1, 2, 3, 4, 5]
# b = map(lambda x: x * 2, a)
# print(list(b))
# OR
# c = [x * 2 for x in a]
# print(c)

# Filter function filter(function, sequence) 
# returns all elements for which the function evaluates to True and dumps the false
# a = [1, 2, 3, 4, 5]
# b = filter(lambda x: x % 2 == 0, a)
# print(list(b))
# OR
# c = [x for x in a if x % 2 == 0]
# print(c)

#  Reduce function  
# syntax reduce(function, sequence) 
# sums up all elments based on operation performed
from functools import reduce
a = [1, 2, 3, 4]

product_a = reduce(lambda x, y: x * y, a) 
print(product_a) # prints 24 = 1 * 2 * 3 * 4

# Errors and Exceptions tomorrow
# Raising an exception
x = -5
# if x < 0:
#     raise Exception('x should be positive')
# assert (x >= 0), "x is not positive"

try:
    a = 5 / 0

except Exception as e:
    print(e) 
