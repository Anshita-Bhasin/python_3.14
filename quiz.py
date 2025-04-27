import sys

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[1] = 5
print(my_list)

#my_tuple[1]=5
print(my_tuple)


# sys.getsizeof()

print(" Memory used by List ",sys.getsizeof(my_list) )
print(" Memory used by Tuple ",sys.getsizeof(my_tuple) )