import pkgutil
import importlib
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        """Initialize the application with a command handler."""
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically loads all available plugins."""
        plugins_package = 'app.plugins'
        package_path = plugins_package.replace('.', '/')

        for _, plugin_name, _ in pkgutil.iter_modules([package_path]):
            module = importlib.import_module(f"{plugins_package}.{plugin_name}")
            for item_name in dir(module):
                item = getattr(module, item_name)
                if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                    self.command_handler.register_command(plugin_name, item())

    def start(self):
        """Starts the application with a REPL (Read-Eval-Print-Loop)."""
        self.load_plugins()
        print("\nSimple Plugin-Based \n Type 'menu' to menu.\n")
        
        while True:
            command = input("Enter command : ").strip().lower()
            
            if command == "exit":
                print("Goodbye!")
                break
            
            if command in self.command_handler.commands:
                try:
                    # Handle arithmetic operations requiring input
                    if command in ["add", "subtract", "multiply", "divide"]:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        result = self.command_handler.execute_command(command, a, b)
                        print(f"Result: {result}")
                    else:
                        # Handle plugins that don't require input
                        self.command_handler.execute_command(command)
                except ValueError:
                    print("Invalid input! Please enter numeric values.")
            else:
                print(f"Unknown command: {command}. Type 'exit' to quit.")
