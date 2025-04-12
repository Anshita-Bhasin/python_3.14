
""" list - A list is a collection of items that is:
Ordered
Mutable (you can change it)
Can contain elements of different data types
"""

name=["Alex","Tom","Sam","Shreya"]
print(name)

mixed=[1,"Tom",False,122.99,["1","Anshita"]]
print(mixed)

# Accessing elements from List

# Indexing, index starts from 0

print(mixed[-3])

# Negative Indexing => -1

# Mutable

numbers=[10,12,99,100]
print("Before: ", numbers)

numbers[1]=15
print("After: ", numbers)


# Slicing -> Slicing means accessing a portion (subset) of a list 
# list[start_index:ending_index] - ending_index is not included

cities=["Delhi","Mumbai","Bangalore","Pune"] #4
print(cities[0:3])
print(cities[2:])
print(cities[:4])
print(cities[:])

#len() => Returns the length of the list
print(len(cities)) #4

# List Methods 

# append(x) – Adds item x to the end

num=["11","99.9","15","20","30"]
num.append(40)

print(num)

# insert(i, x) – Inserts x at index i
num.insert(2,30) #
print(num)

# remove(x) – Removes the first occurrence of x
num.remove(30)
print(num)


# pop() – Removes and returns the last item
print(num.pop()) #40 
print(num)

# pop(i) – Removes and returns item at index i

print(num.pop(1)) 
print(num)

# clear() – Removes all elements

num.clear()
print("after clear:" , num)

# index(x) – Returns index of first occurrence of x

numbers1 = [5, 10, 5, 20, 15]

print(numbers1.index(5)) #0

# count(x) – Counts how many times x appears
print(numbers1.count(5)) #2

# sort() – Sorts the list in ascending order

numbers1.sort()
print(numbers1)

# reverse () - Reverses the list in-place
numbers1.reverse()
print(numbers1)

# copy() – Returns a shallow copy of the list
numbers_copy=numbers1.copy()
print("copy list ", numbers_copy)

# extend() – Adds elements from another list

extra=[25,99]
numbers1.extend(extra)

print(numbers1)

# Practice Question 

# Combine 2 list

n1=[10,20,30]
n2=[56,90,100]
n3=n1+n2
print(n3)