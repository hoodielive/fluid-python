class Example:
    class_trait = 5
    def __init__(self):
        self.instance_trait = 7

print(Example)

# Beware self because this function will now act as if it was defined
def new_function(self):
    print(self.instance_trait, self.class_trait)

# Bind new function to Example class "__main__.Example object"
Example.added = new_function
x = Example()
print(x.added())
