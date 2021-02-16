import numpy as np


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного.Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return (count)  # выход из цикла, если угадали


score_game(game_core_v2)


def game_core_v3(number):
    """функция делит диапазон попалам, сравнивает загаданное число с серединой и адаптирует диапазон
    поиска, выставляя верхней/нижней границей текущее рандомное число"""
    count = 1
    minimum = 1
    maximum = 101
    medium = maximum / 2

    if number < medium:
        predict = np.random.randint(minimum, medium)
    else:
        predict = np.random.randint(medium, maximum)

    while number != predict:
        count += 1
        if predict < number:
            minimum = predict
        else:
            maximum = predict

        predict = np.random.randint(minimum, maximum)
        # print(minimum, maximum, predict, number)
    return count  # выход из цикла, если угадали


score_game(game_core_v3)


def game_core_v4(number):
    """более компактно переписана фунция game_core_v3"""
    count = 1
    minimum = 1
    maximum = 101
    medium = int(maximum / 2)
    predict = medium

    while number != predict:
        if predict < number:
            minimum = predict
        else:
            maximum = predict

        predict = np.random.randint(minimum, maximum)
        count += 1
        # print(minimum, maximum, predict, number)

    return count  # выход из цикла, если угадали


score_game(game_core_v4)


def game_core_v5(number):
    """функция каждый раз делит диапазон выборки пополам"""
    count = 1
    minimum = 1
    maximum = 101
    medium = int(maximum / 2)
    predict = medium

    while number != predict:
        count += 1
        if predict < number:
            minimum = predict
        else:
            maximum = predict
        predict = int((maximum - minimum) / 2 + minimum)  # всегда дели диапазон пополам
        # print(minimum, maximum, predict, number)

    return count  # выход из цикла, если угадали


score_game(game_core_v5)
