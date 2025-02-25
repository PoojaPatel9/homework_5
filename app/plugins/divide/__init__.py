import sys
from app.commands import Command

# Command Implementations
class DivideCommand(Command):
    def execute(self,a,b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
