import re
from typing import Callable

def generator_numbers(text: str):
    for number in re.findall(r'\b\d+\.\d+\b', text):
        yield float(number)

def sum_profit(text: str, func: Callable):
    return sum(func(text))
