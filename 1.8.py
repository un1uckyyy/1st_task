import os
from collections import deque


def is_enter_ok(s):
    if not all(i.isdigit() for i in s.split()):
        return False
    if len(s.split()) != 2:
        return False
    if not (0 <= int(s.split()[0]) <= 9) or not (0 <= int(s.split()[1]) <= 9):
        return False
    return True


class Field:
    def __init__(self):
        self.board = [[' '] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if i % 2 == 0 and j % 2 == 1:
                    self.board[i][j] = '0'
                elif i % 2 == 1 and j % 2 == 0:
                    self.board[i][j] = 'X'

    def print_field(self):
        print('\t' + '\t'.join([str(i) for i in range(1, 10)]))
        print('\t' + '\t'.join(['—' for _ in range(9)]))
        for i in range(9):
            print(f'{str(i + 1)} |\t' + '\t'.join(self.board[i]))

    def gameover(self, h):
        q = deque()
        if h % 2 == 0:
            q.extend([(1, 0), (3, 0), (5, 0), (7, 0)])
            m = {(1, 0), (3, 0), (5, 0), (7, 0)}
        else:
            q.extend([(0, 1), (0, 3), (0, 5), (0, 7)])
            m = {(0, 1), (0, 3), (0, 5), (0, 7)}
        while len(q) != 0:
            ny, nx = q.popleft()
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= (ny + dy) <= 8 and 0 <= (dy + ny) <= 8:
                    if dy in (1, -1) and self.board[ny + dy][nx] == '|' and (ny + dy + 1, nx) not in m:
                        if ny + dy + 1 == 8:
                            return True
                        q.append((ny + dy + 1, nx))
                        m.add((ny + dy + 1, nx))
                    elif dx in (1, -1) and self.board[ny][nx + dx] == '—' and (ny, nx + dx + 1) not in m:
                        if nx + dx + 1 == 8:
                            return True
                        q.append((ny, nx + dx + 1))
                        m.add((ny, nx + dx + 1))

        return False


f = Field()
f.print_field()
h = 0

while True:
    print(f'Ход игрока {h % 2 + 1} ({"X" if h % 2 == 0 else "0"}). ')
    print(f'Введите координаты, куда хотите поставить "—" или "|" через пробел.')
    print('Сначала координату по вертикали(от 1 до 9), затем по горизонтали (от 1 до 9)')
    coords = input()
    if not is_enter_ok(coords):
        print('Неверный ввод! Попробуйте еще раз.')
        continue
    y, x = list(map(lambda q: int(q) - 1, coords.split()))
    if f.board[y][x] != ' ':
        print(f'В эту клетку нельзя поставить {"—" if h % 2 == 0 else "|"}. Попробуйте еще раз.')
        continue
    if y in (0, 8) or x in (0, 8):
        print('В эту клетку ничего нельзя поставить! Попробуйте еще раз.')
        continue
    if h % 2 == 0:
        if y % 2 == 1:
            f.board[y][x] = "—"
        else:
            f.board[y][x] = '|'
    else:
        if y % 2 == 0:
            f.board[y][x] = '—'
        else:
            f.board[y][x] = '|'

    os.system('cls||clear\n')
    f.print_field()
    if f.gameover(h % 2):
        print(f'Игра окончена. Победил игрок {h % 2 + 1} ({"X" if h % 2 == 0 else "0"})')
        break
    h += 1

input('Нажмите Enter для выхода\n')
