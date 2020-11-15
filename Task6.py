# Реализовать два небольших скрипта:
#
#
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# itertools.count(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step.
# itertools.cycle(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз.

import itertools

# а) итератор, генерирующий целые числа, начиная с указанного,
user_list1 = []
user_lenght = int(input('Введите количество элементов массива: '))
user_number = int(input('Введите число c которого начнется отсчет: '))
for i in itertools.islice(itertools.count(user_number), user_lenght):
    user_list1.append(i)
print("========================================\n"
      "оператор itertools.count\n", user_list1)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
user_list2 = []
step = 0
user_step = int(input('Введите количество повторений: '))
for item in itertools.cycle(user_list1):
    if step < len(user_list1 * user_step):
        user_list2.append(item)
        step = step + 1
    else:
        break

print("========================================\n"
      "оператор itertools.cycle\n", user_list2)