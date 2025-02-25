import sys
from app.commands import Command
from app.commands.discord import DiscordCommand
from app.commands.exit import ExitCommand
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.calculator import main as calculator_main


class MenuCommand(Command):
    def __init__(self):
        self.commands = {}
        self._build_commands()
    def execute(self):
        print("Available commands:")
        for command in self.commands:
            print(f"- {command}")
        print("- calculator")
    
    def _build_commands(self):
        self.commands = {
            'greet': GreetCommand(),
            'goodbye':GoodbyeCommand(),
            'discord':DiscordCommand(),
            'exit':ExitCommand(),
            'menu': self.execute
        }

    