from functools import reduce

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
new_list = []
new_list = [el for el in range(100, 1001) if el % 2 == 0]
print('Контрольный список: ', new_list)

# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
# reduce(function, iterable[, initializer])
answer = reduce(lambda x, y: x * y, new_list)
print('Произведение всех элементов: ', answer)
