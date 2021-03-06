"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count
from itertools import cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

my_list = ['Hello', 123, 4.5, True, None]
c = 1
for el in cycle(my_list):
    if c > 10:
        break
    print(el)
    c += 1
