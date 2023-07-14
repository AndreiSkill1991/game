"""Игра угадай число!
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    x_min = 0 # задаем переменную с минимальным значением промежутка для выбора компьютером произвольного числа
    x_max = 101 # задаем переменную с минимальным значением промежутка для выбора компьютером произвольного числа
    count = 0 # переменная для фиксации количества попыток
    while True:
        count += 1
        predict_number = np.random.randint(x_min, x_max)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла, если угадали
        # если число не угадано, то сравниваем загаданное число с серединой интервала,
        # и корректируем интервал в зависимости от того больше заданное число середины интервала, или меньше
        elif number > int((x_max + x_min) / 2): #
            x_min = int((x_max + x_min) / 2)
        elif number < int((x_max + x_min) / 2):
            x_max = int((x_max + x_min) / 2)
        else:
            continue
    return (count) # возвращаем количество попыток для определения загаданного числа


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)