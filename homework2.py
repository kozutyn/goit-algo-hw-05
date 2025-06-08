import re
from typing import Callable

def generator_numbers(text: str):
    matches = re.findall(r' (?P<number>\d+\.\d+) ', text)
    for number in matches:
        yield float(number)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Общий доход работника состоит из нескольких частей: 1000.01 как основной доход, дополненный дополнительными поступлениями 27.45 и 324.00 долларов."
total_income = sum_profit(text, generator_numbers)
print(f"Общий доход: {total_income}")
