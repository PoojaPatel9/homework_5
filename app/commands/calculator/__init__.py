import sys
from app.commands import Command

# Command Implementations
class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"Result: {self.a + self.b}")

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"Result: {self.a - self.b}")

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        print(f"Result: {self.a * self.b}")

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            print("Error: Division by zero")
        else:
            print(f"Result: {self.a / self.b}")
            