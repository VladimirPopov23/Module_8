# module_8_2.py
# 16.11.2024 Задача "План перехват"

def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        arithmetic_mean = result / (len(numbers) - incorrect_data)
        return arithmetic_mean
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
