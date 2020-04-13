import pathlib 

p = pathlib.Path('.')
for child in p.iterdir():
    # Do something 
    my_func(child)
