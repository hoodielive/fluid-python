def squares(value=0):
    while True:
        value = value + 1
        yield (value - 1) * (value - 1)

generator = squares()
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
