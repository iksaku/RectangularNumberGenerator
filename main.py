import random
from datetime import datetime
from typing import List


def int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt + ' '))
        except ValueError:
            print('Por favor ingrese solamente un número entero.')


def number_generator(n: int) -> List[float]:
    for _ in range(n):
        random.seed(datetime.now().timestamp())
        yield random.uniform(0, 1)


N: int = int_input('¿Cuantos números desea generar?')

for i, value in enumerate(number_generator(N)):
    print('%d. %.5f' % (i + 1, value))
