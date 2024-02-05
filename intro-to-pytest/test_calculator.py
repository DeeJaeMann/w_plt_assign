#!/usr/bin/env python3.12
import calculator
import pytest

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

# Add more functional tests for subtract, multiply, and divide

def test_terminal_output(capsys):
    str_output = calculator.calculate(10, 2, "multiply")
    print("Result:", str_output)
    captured = capsys.readouterr()
    assert captured.out == "Result: 20\n"



def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0

# Add more tests to cover edge cases and negative scenarios

# Divide by zero test
    
def test_divide_by_zero():
    #assert calculator.calculate(1, 0, "divide") == "Cannot divide by zero"
    with pytest.raises(ZeroDivisionError):
        calculator.calculate(2, 0, "divide")

