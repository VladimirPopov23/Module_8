# module_8_1.py
# 13.11.2024 Задание "Программистам всё можно"

def add_everything_up(a, b):
    try:
        c = a + b
        return round(c, 3)
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
