import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r' (?P<number>\d+\.\d+) '
    for match in re.finditer(pattern, text):
        yield float(match.group('number'))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

if __name__ == "__main__":
    text = ("Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, "
            "дополненный дополнительными поступлениями 27.45 и 324.00 долларов.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Общий доход: {total_income}")
