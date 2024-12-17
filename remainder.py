# remainder.py

def compute_remainder(dividend, divisor):
    """
    Вычисляет остаток от деления dividend на divisor.

    :param dividend: Делимое
    :param divisor: Делитель
    :return: Остаток от деления
    :raises ValueError: Если делитель равен нулю
    """
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно.")
    return dividend % divisor
