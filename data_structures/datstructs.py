# Dictionary
example_dict = { 'a': 1, 'b': 2, 'c': 3}
another_dict = dict() # use the dictionary class constructor
print(another_dict)
print(example_dict.get('c'))

# Lists
example_list = ['a', 'b', 'c']
another_list = list() # use the list class constructor
print(example_list[0])
another_list[-1].append('some data')

# Tuple | rows in a database
example_tuple = ('hello', 12, None)
another_tuple = tuple([1,2,3,4,5, 'jump'])
print(example_tuple[1])

# Set (collection of data values without keys)
example_set = {'a', 'b', 'c'}
another_set = set()
example_set.add('b')
example_set.discard('b')
print('b' in example_set)

# List Comprehensions (listcomps)
# formula for deriving an uppercased list of example_list
capitals = [x.upper() for x in example_list]
print(capitals)

# Dictionary comprehensions
squares = {k: v ** 2 for k, v in example_dict.items()}
print(squares)

# Set Comprehensions
codes = {ord(x) for x in example_set}
print(codes)

# create a set pulled from the result of dictionary
capital_keys = {x.upper() for x in example_dict.keys()}
print(capital_keys)

# tuple comprehension - generator expression to a tuple constructor
stringfield = tuple(str(x) for x in example_tuple)
print(stringfield)
