"""
Задача: написать функцию для сложения двух дробей, заданных числителями и знаменателями.

Результат работы функции (x, y) должен удовлетворять свойствам:
1. a/b + c/d = x/y
2. x/y несократима
3. y >= 0

Можно считать, что передаваемые в функцию b и d всегда ненулевые.
"""


def add_fractions(a, b, c, d):
    """
    Функция сложения дробей a/b и c/d
    Должна возвращать числитель и знаменатель дроби-результата
    """
    return Ellipsis # Напишите тело функции и правильный return
    up = x = a*d + c*b
    down = y = b*d

    while x != 0 and y != 0:
        if



