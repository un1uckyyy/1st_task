import os
import random


def is_enter_ok(s, first=False):
    if first:
        if not all(i.isdigit() for i in s.split()):
            return False
        if len(s.split()) != 2:
            return False
        if not (1 <= int(s.split()[0]) <= 3) or not (1 <= int(s.split()[1]) <= 3):
            return False
    else:
        if not s.isdigit():
            return False
        if len(s.split()) != 1:
            return False
        if not 1 <= int(s) <= 3:
            return False
    return True


def print_field(m):
    print('   ', '   '.join([str(i + 1) for i in range(3)]))
    print('   ', '   '.join(['—' for _ in range(3)]))
    for i in range(len(m)):
        print(f'{i + 1} | ' + ' | '.join(m[i]) + ' |')


def gameover(m, c1, c2, f):
    if f:
        return m[0][c1] == m[1][c1] == m[2][c1] == m[c2][0] == m[c2][1] == m[c2][2] == '0'
    return m[c1][0] == m[c1][1] == m[c1][2] == m[0][c2] == m[1][c2] == m[2][c2] == '0'


field = [[str(random.randint(1, 9)) for __ in range(3)] for _ in range(3)]
h = 0
print_field(field)
score = [0, 0]
last = -1
lastlast = -1

while True:
    if gameover(field, last, lastlast, h % 2):
        print(f'Игра окончена.')
        if score[0] == score[1]:
            print('Ничья!')
        else:
            print(f'Победил игрок {score.index(max(score)) + 1}. Счёт: {":".join([str(i) for i in score])}')
        break
    if h == 0:
        print(f'Ход игрока {h % 2 + 1}. Счёт: {":".join([str(i) for i in score])}')
        print(f'Введите через пробел координаты клетки, число из которой хотите прибавить к свому счету.')
        print('Сначала цифру по вертикали, затем по горизонтали (от 1 до 3)')
        coords = input()
        if not is_enter_ok(coords, first=True):
            print('Неверный ввод! Попробуйте еще раз!')
            continue
        y, x = list(map(lambda q: int(q) - 1, coords.split()))
        score[h % 2] += int(field[y][x])
        field[y][x] = '0'
        last = x
        lastlast = last
    else:
        print(f'Ход игрока {h % 2 + 1}. Счёт: {":".join([str(i) for i in score])}')
        if h % 2:
            if field[0][last] == field[1][last] == field[2][last] == '0':
                print(f'Из {last + 1} столбца ничего нельзя прибавить. Ход переходит к игроку 1.')
                input('Нажмите Enter')
                os.system('cls||clear\n')
                print_field(field)
                h += 1
                last = lastlast
                continue
            print(f'Введите какой элемент из {last + 1} столбца хотите добавить к своему счету')
            coord = input()
            if not is_enter_ok(coord):
                print('Неверный ввод! Попробуйте еще раз.')
                continue
            if field[int(coord) - 1][last] == '0':
                print('Эту клетку нельзя выбрать!')
                continue
            score[h % 2] += int(field[int(coord) - 1][last])
            field[int(coord) - 1][last] = '0'
            lastlast = last
            last = int(coord) - 1
        else:
            if field[last][0] == field[last][1] == field[last][2] == '0':
                print(f'Из {last + 1} строки ничего нельзя прибавить. Ход переходит к игроку 2.')
                input('Нажмите Enter')
                os.system('cls||clear\n')
                print_field(field)
                h += 1
                last = lastlast
                continue
            print(f'Введите какой элемент из {last + 1} строки хотите добавить к своему счету')
            coord = input()
            if not is_enter_ok(coord):
                print('Неверный ввод! Попробуйте еще раз.')
                continue
            if field[last][int(coord) - 1] == '0':
                print('Эту клетку нельзя выбрать!')
                continue
            score[h % 2] += int(field[last][int(coord) - 1])
            field[last][int(coord) - 1] = '0'
            lastlast = last
            last = int(coord) - 1
    os.system('cls||clear\n')
    print_field(field)
    h += 1

input('Нажмите Enter для выхода\n')
