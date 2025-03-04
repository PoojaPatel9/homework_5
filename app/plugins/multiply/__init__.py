import logging
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, a, b):
        result = a * b
        logging.info(f"Executed MultiplyCommand: {a} * {b} = {result}")
        return result
