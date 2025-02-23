# app/commands/discord/__init__.py
from app.commands import Command

class DiscordCommand(Command):
    def execute(self):
        return "I will send something to Discord"
    