# first class functions and classes - can be manipulated by another object

def foo():
    pass

foo()

bar = foo
print(bar)

foo = 5
print(foo)

print(bar.__name__)

bar.plugin_name = 'demo'
print(bar.plugin_name)

import collections

# make a default parameter
d = collections.defaultdict(list)
d = collections.defaultdict(tuple)
d = collections.defaultdict(set)
d = collections.defaultdict(dict)
d['not in here']
print(d)
