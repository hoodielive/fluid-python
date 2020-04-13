odd_nums = filter(lambda x: x % 2, range(10))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))

odd_list = list(filter(lambda x: x % 2, range(10)))
print(odd_list)
