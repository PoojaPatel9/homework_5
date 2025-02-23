from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        """Easier to ask for forgiveness than permission (EAFP) - Use when it's going to most likely work"""
        try:
            return self.commands[command_name].execute(*args)
        except KeyError:
            print(f"No such command: {command_name}")
            