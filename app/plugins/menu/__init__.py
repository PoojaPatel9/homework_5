import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'Menu\n \n1. greet\n2. goodbye\n3. discord\n4. calculator\n5. email\n6. exit\n ')
    