import os


def print_field(m):
    print(' ', '0', '1', '2')
    print('0|' + '|'.join(m[0]) + '|')
    print('1|' + '|'.join(m[1]) + '|')
    print('2|' + '|'.join(m[2]) + '|')


def gameover(m):
    for i in range(len(m)):
        if m[i][0] == m[i][1] == m[i][2] != '.':
            return True
    for i in range(len(m)):
        if m[0][i] == m[1][i] == m[2][i] != '.':
            return True
    if m[0][0] == m[1][1] == m[2][2] != '.':
        return True
    if m[0][2] == m[1][1] == m[2][0] != '.':
        return True
    return False


def is_enter_ok(s):
    if not all(i.isdigit() for i in s.split()):
        return False
    if len(s.split()) != 2:
        return False
    if int(s.split()[0]) not in (0, 1, 2) or int(s.split()[1]) not in (0, 1, 2):
        return False
    return True


field = [['.'] * 3 for _ in range(3)]
print_field(field)
h = 0
while True:
    print(
        f'Ход игрока {h % 2 + 1} ({"0" if h % 2 == 1 else "X"}). '
        f'Введите через пробел координаты клетки, в которую желаете поставить {"0" if h % 2 == 1 else "X"}')
    print('Сначала цифру по вертикали, затем по горизонтали')
    coords = input()
    if not is_enter_ok(coords):
        print('Неверный ввод. Попробуйте еще раз')
        continue
    coords = list(map(int, coords.split()))
    if field[coords[0]][coords[1]] != '.':
        print('Клетка уже занята. Введите другие координаты\n')
        continue
    field[coords[0]][coords[1]] = "0" if h % 2 == 1 else "X"
    os.system('cls||clear\n')
    print_field(field)
    if gameover(field):
        print(f'Игра окончена! Победил игрок {h % 2 + 1} ({"0" if h % 2 == 1 else "X"})')
        break
    if '.' not in field[0] and '.' not in field[1] and '.' not in field[2]:
        print('Игра окончена! Ничья!')
        break
    h += 1

input('Нажмите Enter для выхода\n')
