import os


def print_field(m):
    print(' ', ' '.join([str(i) for i in range(1, 6)]))
    for i in range(len(m)):
        print(f'{i + 1}|' + '|'.join(m[i]) + '|')


def is_enter_ok(s):
    if not all(i.isdigit() for i in s.split()):
        return False
    if len(s.split()) != 2:
        return False
    if not (1 <= int(s.split()[0]) <= 4) or not (1 <= int(s.split()[1]) <= 5):
        return False
    return True


def gameover(m):
    return all('.' not in m[i] for i in range(len(m)))


def check(m, ny, nx):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dy, dx in moves:
        dy1 = dy + ny
        dx1 = dx + nx
        if 0 <= dy1 <= 3 and 0 <= dx1 <= 4:
            if m[ny][nx] == m[dy1][dx1]:
                score[h % 3] += 1


field = [['.'] * 5 for _ in range(4)]
h = 0
symbols = ['@', '#', '$', '№', '%', '&', '*', '0', 'X']
chosen_syms = ['', '', '']
score = [0, 0, 0]

while h < 3:
    print(f'Игрок {h % 3 + 1}, введите символ, которым будете играть (из набора{symbols})')
    inp = input()
    if inp not in symbols:
        print('Такой символ не доступен для игры! Попоробуйте еще раз')
        continue
    chosen_syms[h % 3] = symbols.pop(symbols.index(inp))
    h += 1

print_field(field)

while True:
    print(
        f'Ход игрока {h % 3 + 1}({chosen_syms[h % 3]}). '
        f'Введите через пробел координаты клетки, в которую желаете поставить фишку.')
    print('Сначала цифру по вертикали(от 1 до 4), затем по горизонтали(от 1 до 5)')
    print(f'Счет({", ".join([str(score[i]) + str(chosen_syms[i]) for i in range(len(score))])})')
    coords = input()
    if not is_enter_ok(coords):
        print('Неверный ввод. Попробуйте еще раз')
        continue
    y, x = list(map(lambda q: int(q) - 1, coords.split()))
    if field[y][x] != '.':
        print('Клетка уже занята. Введите другие координаты\n')
        continue

    field[y][x] = chosen_syms[h % 3]

    os.system('cls||clear\n')
    print_field(field)
    check(field, y, x)
    if gameover(field):
        print(f'Игра окончена! Победил игрок {score.index(min(score)) + 1}.')
        print(f'Счет({", ".join([str(score[i]) + str(chosen_syms[i]) for i in range(len(score))])})')
        break
    h += 1

input('Нажмите Enter для выхода\n')
