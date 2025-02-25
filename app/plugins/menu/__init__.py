import sys
from app.commands import Command


class MenuCommand(Command):
    def execute(self):
        print(f'Menu\n \n1. greet\n2. goodbye\n3. discord\n4. email\n\n \nCALCULATOR\n5. add\n6. subtract\n7. multiply\n8. divide\n9. exit ')
    