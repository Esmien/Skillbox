import sys

some_list = [num for num in range(10 ** 8)]
some_tuple = tuple(some_list)
print(sys.getsizeof(some_list))
print(sys.getsizeof(some_tuple))