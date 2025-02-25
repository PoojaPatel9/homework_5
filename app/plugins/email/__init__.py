from app.commands import Command


class EmailCommand(Command):
    def execute(self):
        print("i send mail on email")
        