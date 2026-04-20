from dataclasses import dataclass


@dataclass
class Calculator:
    number1: float
    number2: float

    def __add__(self, other: "Calculator") -> "Calculator":
        return Calculator(self.number1 + other.number1, self.number2 + other.number2)

    def __sub__(self, other: "Calculator") -> "Calculator":
        return Calculator(self.number1 - other.number1, self.number2 - other.number2)

    def __mul__(self, other: "Calculator") -> "Calculator":
        return Calculator(self.number1 * other.number1, self.number2 * other.number2)

    def __truediv__(self, other: "Calculator") -> "Calculator":
        return Calculator(self.number1 / other.number1, self.number2 / other.number2)

    def __pow__(self, other: "Calculator") -> "Calculator":
        return Calculator(self.number1**other.number1, self.number2**other.number2)


class CalculatorFactory(Calculator):
    def __init__(self, number1: float, number2: float, computations: str):
        super().__init__(number1, number2)
        self.computations = computations

    def prompt_user(self) -> None:
        computation_list = []


def main():
    pass


if __name__ == "__main__":
    main()
