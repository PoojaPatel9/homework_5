# app/calculator.py
from app.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

commands = {
    "add": AddCommand(),
    "subtract": SubtractCommand(),
    "multiply": MultiplyCommand(),
    "divide": DivideCommand()
}

def menu():
    print("Available commands:")
    for cmd in commands.keys():
        print(f"- {cmd}")
    print("- menu (show commands)")
    print("- exit (quit the program)")

def main():
    print("Welcome to the Command Pattern Calculator!")
    menu()  # Show available commands

    while True:
        user_input = input("\nEnter command: ").strip().lower()

        if user_input == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == "menu":
            menu()
        elif user_input in commands:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = commands[user_input].execute(a, b)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        else:
            print("Unknown command. Type 'menu' to see available commands.")

if __name__ == "__main__":
    main()
