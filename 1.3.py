import os
import random


def print_field(m):
    print(' ', ' '.join([str(i) for i in range(len(m))]))
    for i in range(len(m)):
        print(f'{i}|' + '|'.join(m[i]) + '|')


def is_enter_ok(s):
    if len(s.split()) != 2:
        return False
    if s.split()[0].lower() not in ('г', 'в') or not s.split()[1].isdigit():
        return False
    if not 0 <= int(s.split()[1]) <= 7:
        return False
    return True


def gameover(m):
    return all('0' not in m[i] for i in range(8))


field = [['.'] * 8 for _ in range(8)]
while True:
    numbers_of_chips = input('Введите количество фишек, которые будут расстаавлены на доску(от 5 до 64):\n')
    if not numbers_of_chips.isdigit():
        print('Введите число!')
        continue
    elif not (5 <= int(numbers_of_chips) <= 64):
        print('Введите число из диапазона от 5 до 64!')
        continue
    else:
        numbers_of_chips = int(numbers_of_chips)
        break

nums = [i for i in range(64)]
for i in range(numbers_of_chips):
    ind = nums.pop(nums.index(random.choice(nums)))
    field[ind // 8][ind % 8] = '0'

h = 0
print_field(field)
while True:
    print(f'Ход игрока {h % 2 + 1}')
    print('Выберите, фишки с какой горизонтали или вертикали хотите забрать.'
          'Введите букву("г" для горизонтали или "в" для вертикали) и цифру(от 0 до 7) через пробел.')
    inp = input()
    if not is_enter_ok(inp):
        print('Неверный ввод. Попробуйте еще раз')
        continue
    g_v, index = inp.split()
    if g_v.lower() == 'г':
        if '0' not in field[int(index)]:
            print('Из этой горизонтали нельзя забрать фишки. Их на ней нет! Сделайте другой ход!')
            continue
        else:
            field[int(index)] = ['.'] * 8
    elif g_v.lower() == 'в':
        m = []
        for i in range(8):
            m.append(field[i][int(index)])
        if '0' not in m:
            print('Из этой вертикали нельзя забрать фишки. Их на ней нет! Сделайте другой ход!')
            continue
        else:
            for i in range(8):
                field[i][int(index)] = '.'
    os.system('cls||clear\n')
    print_field(field)
    if gameover(field):
        print('Игра окончена!!')
        print(f'Победил игрок {h % 2 + 1}')
        break
    h += 1

input('Нажмите Enter для выхода\n')
