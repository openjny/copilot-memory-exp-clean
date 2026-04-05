"""Simple calculator application."""
import math
from dataclasses import dataclass


@dataclass
class Calculator:
    """A basic calculator that tracks history."""
    history: list[str]

    def __init__(self) -> None:
        self.history = []

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ValueError if b is zero."""
        if math.isclose(b, 0.0, abs_tol=1e-10):
            raise ValueError("Division by zero is not allowed.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def power(self, base: float, exponent: float) -> float:
        """Raise base to the given exponent. Supports negative exponents."""
        if math.isclose(base, 0.0, abs_tol=1e-10) and exponent < 0:
            raise ValueError("Zero cannot be raised to a negative exponent.")
        result = base ** exponent
        self.history.append(f"{base} ** {exponent} = {result}")
        return result

    def format_result(self, result: float) -> str:
        """Return a formatted string representation of a result."""
        return f"Result: {result}"

    def get_history(self) -> list[str]:
        """Return calculation history."""
        return list(self.history)

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()


if __name__ == "__main__":
    calc = Calculator()
    print(calc.format_result(calc.add(10, 20)))
    print(calc.format_result(calc.multiply(3, 7)))
    print(calc.format_result(calc.subtract(15, 5)))
    print(calc.format_result(calc.divide(20, 4)))
    print(calc.format_result(calc.power(2, -3)))
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print(f"History: {calc.get_history()}")
