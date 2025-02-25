'''test for commands'''
import pytest
from app import App
from app.plugins.discord import DiscordCommand
from app.plugins.email import EmailCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

from app.calculator import process_command, menu

def test_greet_command(capfd):
    """Test if GreetCommand prints 'Hello, World!'"""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"

def test_goodbye_command(capfd):
    """Test if GoodbyeCommand prints 'Goodbye'"""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"

def test_discord_command(capfd):
    """Test if DiscordCommand prints 'i send message on discord'"""
    command = DiscordCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "i send message on discord\n", "The discordCommand should print 'i send message on discord'"

def test_email_command(capfd):
    """Test if DiscordCommand prints 'i send mail on email'"""
    command = EmailCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "i send mail on email\n", "The discordCommand should print 'i send mail on email'"

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    # Check for the expected exit code
    assert e.value.code == 0  # or assert str(e.value) == '0'

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    # Check for the expected exit code
    assert e.value.code == 0  # or assert str(e.value) == '0'

def test_add():
    """Test addition operation."""
    assert AddCommand().execute(5, 3) == 8

def test_subtract():
    """Test subtraction operation."""
    assert SubtractCommand().execute(10, 4) == 6

def test_multiply():
    """Test multiplication operation."""
    assert MultiplyCommand().execute(2, 3) == 6

def test_divide():
    """Test division operation, including handling division by zero."""
    assert DivideCommand().execute(10, 2) == 5
    assert DivideCommand().execute(10, 0) == "Error: Division by zero", "Should handle division by zero properly"

# Test the menu function to ensure it returns the correct string
def test_menu():
    """Test the 'menu' function for expected output."""
    result = menu()
    assert "add" in result
    assert "subtract" in result
    assert "multiply" in result
    assert "divide" in result
    assert "menu" in result
    assert "exit" in result

# Test process_command function with valid commands
def test_process_add_command(monkeypatch):
    """Test processing the 'add' command."""
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Mock user input to return 5
    result = process_command("add")
    assert result == "Result: 10.0"

def test_process_subtract_command(monkeypatch):
    """Test processing the 'subtract' command."""
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Mock user input to return 5
    result = process_command("subtract")
    assert result == "Result: 0.0"

def test_process_multiply_command(monkeypatch):
    """Test processing the 'multiply' command."""
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Mock user input to return 5
    result = process_command("multiply")
    assert result == "Result: 25.0"

def test_process_divide_command(monkeypatch):
    """Test processing the 'divide' command."""
    monkeypatch.setattr('builtins.input', lambda _: '5')  # Mock user input to return 5
    result = process_command("divide")
    assert result == "Result: 1.0"

# Test division by zero error handling
def test_process_divide_by_zero_command(monkeypatch):
    """Test processing division by zero error."""
    monkeypatch.setattr('builtins.input', lambda _: '0')  # Mock user input to return 0
    result = process_command("divide")
    assert result == "Error: Division by zero is not allowed."

# Test handling invalid input (non-numeric input)
def test_process_invalid_input(monkeypatch):
    """Test processing invalid non-numeric input."""
    monkeypatch.setattr('builtins.input', lambda _: 'invalid')  # Mock user input to return non-numeric input
    result = process_command("add")
    assert result == "Invalid input. Please enter numbers only."

# Test unknown command
def test_process_unknown_command():
    """Test processing an unknown command."""
    result = process_command("unknown_command")
    assert result == "Unknown command. Type 'menu' to see available commands."

# Test exit command
def test_process_exit_command():
    """Test processing the 'exit' command."""
    result = process_command("exit")
    assert result == "Exiting the calculator. Goodbye!"

# Test menu command
def test_process_menu_command():
    """Test processing the 'menu' command."""
    result = process_command("menu")
    assert "add" in result
    assert "subtract" in result
    assert "multiply" in result
    assert "divide" in result
