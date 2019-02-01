import itertools 

even_list = list(itertools.filterfalse(lambda x: x % 2, range(10)))
print(even_list)
