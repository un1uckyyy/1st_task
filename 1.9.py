import os
import random
from collections import deque


def is_enter_ok(s):
    if len(s.split()) != 2:
        return False
    if s.split()[0].upper() not in 'АБВГДЕЖЗИК' or not s.split()[1].isdigit():
        return False
    if not 1 <= int(s.split()[1]) <= 10:
        return False
    return True


class Field:
    def __init__(self):
        self.real_board = [['.'] * 10 for _ in range(10)]
        self.user_board = [['.'] * 10 for _ in range(10)]
        self.bool_board = [[0] * 10 for _ in range(10)]

    def print_field(self):
        alph = 'АБВГДЕЖЗИК'
        print('\t' + '\t'.join([alph[i] for i in range(10)]))
        print('\t' + '\t'.join(['—' for _ in range(10)]))
        for i in range(10):
            print(f'{str(i + 1) + " " * (i + 1 != 10)}|\t' + '\t'.join(self.user_board[i]))

    def clear_board(self):
        self.real_board = [['.'] * 10 for _ in range(10)]
        self.user_board = [['.'] * 10 for _ in range(10)]
        self.bool_board = [[0] * 10 for _ in range(10)]

    def setup_cell(self, is_horizontal, ship_len, indy, indx):
        if is_horizontal:
            for x in range(indx, indx + ship_len):
                self.real_board[indy][x] = '0'
                self.bool_board[indy][x] = 2
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                    if (dy, dx) == (0, 1) and x != indx + ship_len - 1:
                        continue
                    if 0 <= (indy + dy) <= 9 and 0 <= (x + dx) <= 9:
                        if self.bool_board[indy + dy][x + dx] == 0:
                            self.bool_board[indy + dy][x + dx] = 1
        else:
            for y in range(indy, indy + ship_len):
                self.real_board[y][indx] = '0'
                self.bool_board[y][indx] = 2
                for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                    if (dy, dx) == (1, 0) and y != indy + ship_len - 1:
                        continue
                    if 0 <= (y + dy) <= 9 and 0 <= (indx + dx) <= 9:
                        if self.bool_board[y + dy][indx + dx] == 0:
                            self.bool_board[y + dy][indx + dx] = 1

    def setup_ships(self):
        if random.randint(0, 1):
            indy = random.randint(0, 9)
            indx = random.randint(0, 6)
            self.setup_cell(True, 4, indy, indx)
        else:
            indy = random.randint(0, 6)
            indx = random.randint(0, 9)
            self.setup_cell(False, 4, indy, indx)
        for i in range(2):
            while True:
                if random.randint(0, 1):
                    indy = random.randint(0, 9)
                    indx = random.randint(0, 7)
                    if self.bool_board[indy][indx] or self.bool_board[indy][indx + 1] or self.bool_board[indy][
                        indx + 2]:
                        continue
                    self.setup_cell(True, 3, indy, indx)
                    break
                else:
                    indy = random.randint(0, 7)
                    indx = random.randint(0, 9)
                    if self.bool_board[indy][indx] or self.bool_board[indy + 1][indx] or self.bool_board[indy + 2][
                        indx]:
                        continue
                    self.setup_cell(False, 3, indy, indx)
                    break
        for i in range(3):
            while True:
                if random.randint(0, 1):
                    indy = random.randint(0, 9)
                    indx = random.randint(0, 8)
                    if self.bool_board[indy][indx] or self.bool_board[indy][indx + 1]:
                        continue
                    self.setup_cell(True, 2, indy, indx)
                    break
                else:
                    indy = random.randint(0, 8)
                    indx = random.randint(0, 9)
                    if self.bool_board[indy][indx] or self.bool_board[indy + 1][indx]:
                        continue
                    self.setup_cell(False, 2, indy, indx)
                    break
        for i in range(4):
            while True:
                if random.randint(0, 1):
                    indy = random.randint(0, 9)
                    indx = random.randint(0, 9)
                    if self.bool_board[indy][indx]:
                        continue
                    self.setup_cell(True, 1, indy, indx)
                    break
                else:
                    indy = random.randint(0, 9)
                    indx = random.randint(0, 9)
                    if self.bool_board[indy][indx]:
                        continue
                    self.setup_cell(False, 1, indy, indx)
                    break

    def is_ship_down(self, y, x):
        q = deque()
        m = set()
        q.append((y, x))
        m.add((y, x))
        while len(q) != 0:
            ny, nx = q.popleft()
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                if 0 <= ny + dy <= 9 and 0 <= nx + dx <= 9:
                    if self.bool_board[ny + dy][nx + dx] == 2:
                        return False
                    if self.bool_board[ny + dy][nx + dx] == 3 and (ny + dy, nx + dx) not in m:
                        q.append((ny + dy, nx + dx))
                        m.add((ny + dy, nx + dx))
        return True

    def show_down_ship(self, y, x):
        q = deque()
        m = set()
        q.append((y, x))
        m.add((y, x))
        while len(q) != 0:
            ny, nx = q.popleft()
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
                if 0 <= (ny + dy) <= 9 and 0 <= (nx + dx) <= 9:
                    if self.bool_board[ny + dy][nx + dx] == 1:
                        self.user_board[ny + dy][nx + dx] = 'X'
                    if self.bool_board[ny + dy][nx + dx] == 3 and (ny + dy, nx + dx) not in m:
                        q.append((ny + dy, nx + dx))
                        m.add((ny + dy, nx + dx))

    def gameover(self):
        return all(2 not in self.bool_board[i] for i in range(len(self.bool_board)))


f = Field()
f.print_field()
f.setup_ships()
# print(*f.real_board, sep='\n')


while True:
    print('Введите координаты, куда собираетесь стрелять. В формате "<Буква> <Цифра>"')
    coords = input()
    if not is_enter_ok(coords):
        print('Неверный ввод! Попробуйте еще раз.')
        continue
    y, x = int(coords.split()[1]) - 1, 'АБВГДЕЖЗИК'.index(coords.split()[0].upper())
    if f.user_board[y][x] in ('X', '0'):
        print('В эту клетку уже нельзя выстрелить.')
        continue
    os.system('cls||clear\n')
    if f.real_board[y][x] == '0':
        f.user_board[y][x] = '0'
        print('Попадание!')
        f.bool_board[y][x] = 3
        if f.is_ship_down(y, x):
            print('Корабль уничтожен!')
            f.show_down_ship(y, x)
    else:
        f.user_board[y][x] = 'X'
        print('Мимо!')
    f.print_field()
    if f.gameover():
        print('Игра окончена!')
        break

input('Нажмите Enter для выхода\n')
