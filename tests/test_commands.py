"""Unit tests for the App class handling REPL commands."""

import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand
from app.commands.calculator import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

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

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

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
