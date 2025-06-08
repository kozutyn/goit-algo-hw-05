import re

from typing import Callable

def generator_numbers(text: str):
    for number in re.findall(r'\s\d+\.\d+\s', text):
        yield float(number.strip())

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

if __name__ == "__main__":
    text = "Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, дополненный дополнительными поступлениями 27.45 и 324.00 долларов."
    total_income = sum_profit(text, generator_numbers)
    print(f"Общий доход: {total_income}")
