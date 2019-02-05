import packagename.modulename 
import name # absolute search
import .name # relative search
from .name import Foo # <- import module Foo
from .name import Foo as Bar # aliasing 

class Objectives: 
    def __init__(self, name)
        self.name = name 
    
    def findMain(self):
        pass

looking_for_main = Objectives('something')
