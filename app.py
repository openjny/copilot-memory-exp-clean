"""Simple calculator application."""
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

    def get_history(self) -> list[str]:
        """Return calculation history."""
        return list(self.history)

    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()


if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(10, 20))
    print(calc.multiply(3, 7))
    print(f"History: {calc.get_history()}")
