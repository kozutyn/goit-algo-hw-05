import re

from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    for number in re.findall(r'(?<=\s)(\d+\.\d+)(?=\s)', text):
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

text = "Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, дополненный дополнительными поступлениями 27.45 и 324.00 долларов."
total_income = sum_profit(text, generator_numbers)
print(f"Общий доход: {total_income}")
