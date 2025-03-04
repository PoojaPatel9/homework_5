# tests/test_app.py
"""
Test cases for the app module, including command handling and environment variable loading.
"""
import pytest
from app import App

def test_app_get_environment_variable():
    """Test to retrieve and validate environment variable."""
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env.upper() in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit) as excinfo:
        app = App()
        app.start()
    assert excinfo.value.code == 0

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "Unknown command: unknown_command. Type 'exit' to quit." in captured.out
