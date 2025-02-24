import sys
from app.commands import Command

# Command Implementations
class AddCommand(Command):
    def execute(self, a, b):
        return a + b
    
class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b


class MultiplyCommand(Command):
    def execute(self,a,b):
        return a * b

class DivideCommand(Command):
    def execute(self,a,b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

