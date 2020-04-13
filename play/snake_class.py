class Snake:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @property
    def get_breed(self):
        return self.name

# instanitate the class 
snake1 = Snake('python', 'constrictor')
snake1.get_breed
