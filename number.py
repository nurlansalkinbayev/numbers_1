import math

num_1 = int(input('Введите целое положительное число:'))
num_2 = int(input('Введите целое положительное число:'))
sum = num_1 + num_2
mines = num_1 - num_2
multipley = num_1 * num_2
num_log = round(math.log10(num_1), 3)
num_degree = num_1 ** num_2
print(f'Сумма чисел равна:{sum}.')
print(f'Разность чисел равна:{mines}.')
print(f'Произведение чисел равна:{multipley}.')
print(f'Десятичный логариф числа {num_1} равен:{num_log}.')
print(f'Степень числа {num_1} в {num_2} равна:{num_degree}.')
