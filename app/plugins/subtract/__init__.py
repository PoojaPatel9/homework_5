import sys
from app.commands import Command

# Command Implementations
class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

