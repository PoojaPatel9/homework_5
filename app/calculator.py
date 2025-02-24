from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

commands = {
    "add": AddCommand(),
    "subtract": SubtractCommand(),
    "multiply": MultiplyCommand(),
    "divide": DivideCommand()
}

def menu():
    """Returns the menu as a string (for testing purposes)."""
    menu_text = "Available commands:\n"
    menu_text += "\n".join(f"-> {cmd}" for cmd in commands.keys())
    menu_text += "\n- menu (show commands)\n- exit (quit the program)"
    return menu_text

def process_command(user_input):
    """Processes user input and returns output for easier testing."""
    user_input = user_input.strip().lower()

    if user_input == "exit":
        return "Exiting the calculator. Goodbye!"
    elif user_input == "menu":
        return menu()
    elif user_input in commands:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            # Prevent division by zero
            if user_input == "divide" and b == 0:
                return "Error: Division by zero is not allowed."

            result = commands[user_input].execute(a, b)
            return f"Result: {result}"
        except ValueError:
            return "Invalid input. Please enter numbers only."
    else:
        return "Unknown command. Type 'menu' to see available commands."

def main():
    """Main function to run the calculator application."""
    print("Welcome to the Command Pattern Calculator!")
    print(menu())  # Show available commands

    while True:
        user_input = input("\nEnter command: ")
        response = process_command(user_input)
        print(response)
        if response == "Exiting the calculator. Goodbye!":
            break
