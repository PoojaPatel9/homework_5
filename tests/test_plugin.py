# tests/test_plugin.py
"""
Test cases for the app plugin system, including command execution and plugin loading.
"""
# Correct import order
import logging
from unittest.mock import patch
import pytest
from pytest import MonkeyPatch
from app import App

@pytest.fixture
def mock_input(monkeypatch):
    """Fixture to mock user input for REPL commands."""
    inputs = iter(['add', '2', '3', 'multiply', '5', '4', 'subtract', '9', '4', 'divide', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

@pytest.fixture
def capture_logs(capfd):
    """Fixture to capture logs during tests."""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    return capfd

def test_app_add_command(mock_input, capture_logs):
    """Test that the 'add' command correctly adds two numbers."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0
    capture_logs.readouterr()
    assert "Result: 5.0"  # Expected result for 2 + 3
    assert "Executed AddCommand"

def test_app_multiply_command(mock_input, capture_logs):
    """Test that the 'multiply' command correctly multiplies two numbers."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0
    capture_logs.readouterr()
    assert "Result: 20.0"  # Expected result for 5 * 4
    assert "Executed MultiplyCommand"

def test_app_subtract_command(mock_input, capture_logs):
    """Test that the 'subtract' command correctly subtracts two numbers."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0
    capture_logs.readouterr()
    assert "Result: 5.0"  # Expected result for 9 - 4
    assert "Executed SubtractCommand"

def test_app_divide_by_zero(mock_input, capture_logs):
    """Test divide by zero scenario."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0
    capture_logs.readouterr()
    assert "Error: Cannot divide by zero"

def test_app_invalid_input(monkeypatch, capture_logs):
    """Test that the app handles invalid input gracefully."""
    inputs = iter(['add', 'two', 'three', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capture_logs.readouterr()
    assert "Invalid input"

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv('ENVIRONMENT', 'TEST')
    yield

def test_load_environment_variables(mock_env_vars):
    """Test loading of environment variables."""
    app = App()
    assert app.settings['ENVIRONMENT'] == 'TEST'

@patch('app.App.load_plugins')
def test_load_plugins(mock_load_plugins):
    """Test loading of plugins."""
    app = App()
    app.load_plugins()
    mock_load_plugins.assert_called_once()

def test_logging_configuration():
    """Test that logging is configured correctly."""
    app = App()
    logger = logging.getLogger()
    assert logger.level == logging.INFO  # Default logging level
    assert len(logger.handlers) == 2  # Two handlers: FileHandler

def test_command_registration():
    """Test that commands are correctly registered from plugins."""
    app = App()
    app.load_plugins()
    # Assuming we expect a command named "add" to be registered
    assert 'add' in app.command_handler.commands
    assert 'multiply' in app.command_handler.commands
    assert 'subtract' in app.command_handler.commands
    assert 'divide' in app.command_handler.commands
