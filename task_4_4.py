"""
Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел,
соответствующих требованию. Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = (src[i] for i in range(len(src)) if src.count(src[i]) == 1)
print(type(result), list(result))
