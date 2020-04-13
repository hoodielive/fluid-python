pets = ['dogs', 'cats', 'lizards', 'pythons']
pet_enum = enumerate(pets)
print(next(pet_enum))

pet_enum2 = enumerate(pets, start=5)
print(next(pet_enum2))

pet_list = list(enumerate(pets))
print(pet_list)
