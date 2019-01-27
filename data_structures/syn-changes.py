
# Matrix operations -> 5 @ 10 # a valid python expression as of 3.5

def needs_params(a,b,c):
    print(a,b,c)

values = [1,2,3]

needs_params(*values)

partial_values1 = [1,2]
partial_values2 = [3]
needs_params(*partial_values1, *partial_values2)
needs_params(*partial_values2, *partial_values1)

combined_values = [*partial_values1, *partial_values2]

# Now includes typing (support type hints)
# zipapp - manage executable python zip archives
