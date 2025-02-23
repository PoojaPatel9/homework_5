import sys
from app.commands import Command

# Command Implementations
# app/commands/add_command.py
class AddCommand:
    def execute(self, a, b):
        return a + b
    
# app/commands/add_command.py
class SubtractCommand:
    def execute(self, a, b):
        return a - b


class MultiplyCommand:
    def execute(self,a,b):
        return a * b

class DivideCommand:
    def execute(self,a,b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

