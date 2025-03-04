import pytest
from app import App
import logging

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
    
    # Check if the app exited gracefully
    assert e.value.code == 0

    # Capture the output and logs
    out, err = capture_logs.readouterr()
    assert "Result: 5.0" in out  # Expected result for 2 + 3

    # Check if the log contains the command execution details
    assert "Executed AddCommand" in out

def test_app_multiply_command(mock_input, capture_logs):
    """Test that the 'multiply' command correctly multiplies two numbers."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0

    # Capture the output and logs
    out, err = capture_logs.readouterr()
    assert "Result: 20.0" in out  # Expected result for 5 * 4

    # Check if the log contains the multiplication command execution
    assert "Executed MultiplyCommand" in out

def test_app_subtract_command(mock_input, capture_logs):
    """Test that the 'subtract' command correctly subtracts two numbers."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0

    # Capture the output and logs
    out, err = capture_logs.readouterr()
    assert "Result: 5.0" in out  # Expected result for 9 - 4

    # Check if the log contains the subtraction command execution
    assert "Executed SubtractCommand" in out

def test_app_divide_command(mock_input, capture_logs):
    """Test that the 'divide' command correctly divides two numbers."""
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0

    # Capture the output and logs
    out, err = capture_logs.readouterr()
    assert "Result: 5.0" in out  # Expected result for 10 / 2

    # Check if the log contains the divide command execution
    assert "Executed DivideCommand" in out

def test_app_invalid_input(mock_input, capture_logs):
    """Test that the app handles invalid input gracefully."""
    inputs = iter(['add', 'two', 'three', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0
    out, err = capture_logs.readouterr()
    assert "Invalid input!" in out  # Check for invalid input logging
