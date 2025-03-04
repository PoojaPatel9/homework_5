import logging
from app.commands import Command

class SubtractCommand(Command):
    def execute(self, a, b):
        result = a - b
        logging.info(f"Executed SubtractCommand: {a} - {b} = {result}")
        return result
