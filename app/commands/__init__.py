from abc import ABC, abstractmethod

class Command(ABC):
    """Base Command class defining a common interface for all commands."""
    def execute(self, *args):
        raise NotImplementedError("Execute method must be implemented in subclasses.")


class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, command_name, *args):
        if command_name in self.commands:
            return self.commands[command_name].execute(*args)
        else:
            print(f"No such command: {command_name}")
