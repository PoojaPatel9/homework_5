from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Register a command with its name."""
        self.commands[name] = command

    def execute_command(self, command_name, *args):
        """Execute a command with provided arguments."""
        if command_name in self.commands:
            command = self.commands[command_name]
            return command.execute(*args)  # Pass all arguments (a and b) to execute()
        else:
            raise ValueError(f"Command '{command_name}' not found.")
