import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            logging.error("Attempted division by zero: {} / {}".format(a, b))
            return "Error: Division by zero"
        result = a / b
        logging.info(f"Executed DivideCommand: {a} / {b} = {result}")
        return result
