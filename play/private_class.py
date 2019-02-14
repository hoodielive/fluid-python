class MyComplex:
    def __init__(self, real_part, imaginary_part):
        self.r = real_part
        self.i = imaginary_part

class PrivateClass:
    __a_ = 'I am a private class'

complex_num = MyComplex(2, 3)
print(complex_num)
