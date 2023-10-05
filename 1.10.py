import os
import random


def print_field(m):
    print('\t' + '\t'.join([str(i + 1) for i in range(len(m))]))
    print('\t' + '\t'.join(['—' for _ in range(len(m))]))
    for i in range(len(m)):
        print(f'{i + 1} |\t' + '\t'.join(m[i]))


def is_enter_ok(s):
    if not all(i.isdigit() for i in s.split()):
        return False
    if len(s.split()) != 2:
        return False
    if not (1 <= int(s.split()[0]) <= 4) or not (1 <= int(s.split()[1]) <= 4):
        return False
    return True


def gameover(m):
    return m[0] == ['1', '2', '3', '4'] and m[1] == ['5', '6', '7', '8'] and m[2] == ['9', '10', '11', '12'] and m[
        3] == ['13', '14', '15', '.']


nums_indexes = [i for i in range(16)]
nums = [i for i in range(1, 16)]
field = [['.'] * 4 for _ in range(4)]
for i in range(15):
    ind = nums_indexes.pop(nums_indexes.index(random.choice(nums_indexes)))
    num = nums.pop(nums.index(random.choice(nums)))
    field[ind // 4][ind % 4] = str(num)

# field = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '.', '15']]
empty_y, empty_x = 0, 0
for i in range(len(field)):
    if '.' in field[i]:
        empty_y, empty_x = i, field[i].index('.')

h = 1
print_field(field)

while True:
    print(f'Ход {h}')
    print('Введите координаты клетки, которую хотите передвинуть в пустую клеткку.')
    print('Сначала координату по вертикали(от 1 до 4), затем по горизонтали(от 1 до 4)')
    available_moves = []
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        if 0 <= (empty_y + dy) <= 3 and 0 <= (empty_x + dx) <= 3:
            available_moves.append((empty_y + dy + 1, empty_x + dx + 1))
    print(f'Доступные ходы: {sorted(available_moves)}')
    coords = input()
    if not is_enter_ok(coords):
        print('Неверный ввод. Попробуйте еще раз')
        continue
    y, x = list(map(lambda q: int(q) - 1, coords.split()))
    if (y + 1, x + 1) not in available_moves:
        print('Недоступный ход. Попробуйте еще раз')
        continue
    field[empty_y][empty_x], field[y][x] = field[y][x], field[empty_y][empty_x]
    empty_y, empty_x = y, x
    os.system('cls||clear\n')
    print_field(field)
    if gameover(field):
        print(f'Игра окончена. Вы справились за {h} ходов')
        break
    h += 1

input('Нажмите Enter для выхода\n')
