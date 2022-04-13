print("=====================<EXERCÍCIO 10>=====================")

import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b * b - 4 * a * c

if delta < 0:
    print("IMPOSSÍVEL resolver a equação!")
else:
    x_1 = (-b - math.sqrt(delta))
    x_2 = (-b + math.sqrt(delta))
    print(x_1, x_2)