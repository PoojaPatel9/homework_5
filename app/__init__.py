import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command

class App:
    def __init__(self):
        """Initialize the application with logging, environment variables, and a command handler."""
        os.makedirs('logs', exist_ok=True)  # Ensure logs directory exists
        self.configure_logging()
        load_dotenv()  # Load environment variables
        self.settings = self.load_environment_variables()
        self.command_handler = CommandHandler()

    def configure_logging(self):
        """Sets up logging configuration."""
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler("logs/app.log"),
                    logging.StreamHandler()
                ]
            )
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Loads all environment variables into a dictionary."""
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """Returns a specific environment variable, defaulting to 'ENVIRONMENT'."""
        return self.settings.get(env_var, 'ENVIRONMENT')

    def load_plugins(self):
        """Dynamically loads all available plugins from the 'app.plugins' directory."""
        plugins_package = 'app.plugins'
        plugins_path = os.path.join(os.path.dirname(__file__), 'plugins')

        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    plugin_module = importlib.import_module(f"{plugins_package}.{plugin_name}")
                    self.register_plugin_commands(plugin_module, plugin_name)
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        """Registers commands from a plugin module."""
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        """Starts the application with a REPL (Read-Eval-Print-Loop)."""
        self.load_plugins()
        logging.info("Application started. Type 'exit' to quit.")
        logging.info("Simple Plugin-Based Calculator - Type 'exit' to quit.")

        try:
            while True:
                command = input("Enter command: ").strip().lower()

                if command == "exit":
                    logging.info("Application exit.")
                    sys.exit(0)

                if command in self.command_handler.commands:
                    try:
                        if command in ["add", "subtract", "multiply", "divide"]:
                            a = float(input("Enter first number: "))
                            b = float(input("Enter second number: "))
                            result = self.command_handler.execute_command(command, a, b)
                            logging.info(f"Result: {result}")
                        else:
                            self.command_handler.execute_command(command)
                    except ValueError:
                        logging.error("Invalid input! Please enter numeric values.")
                else:
                    logging.error(f"Unknown command: {command}. Type 'exit' to quit.")
                    print(f"Unknown command: {command}. Type 'exit' to quit.")  # Ensures the message is visible to user
        except KeyboardInterrupt:
            logging.info("Application interrupted. Exiting gracefully.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")
