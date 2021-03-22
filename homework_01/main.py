"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*num):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n ** 2 for n in num]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def filter_numbers(*args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    num = args[0]
    _type = args[1]
    if _type == EVEN:
        # return [n for n in num if n % 2 == 0]
        return list(filter(lambda n: n % 2 == 0, num))
    elif _type == ODD:
        # return [n for n in num if n % 2 != 0]
        return list(filter(lambda n: n % 2 != 0, num))
    else:
        # return [n for n in num if is_prime(n)]
        return list(filter(lambda n: is_prime(n), num))

