__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    if len(arr) < 2:
        return 0
    even_sum = 0
    odd_sum = 0

    for number in arr:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    if even_odd == 0 or odd_sum == 0:
        return 0
    return even_sum / odd_sum
