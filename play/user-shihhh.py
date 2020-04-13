from getpass import getpass
from pprint import pprint
import cmd

password = getpass('Password: ')
pprint([{1: 2, 3: 4}, {5: 6, 7: list(range(25))}])

class Interface(cmd.Cmd):
    prompt = 'Command: '

    def do_foo(self, arg):
        print(arg)

interface = Interface()
interface.cmdloop()
