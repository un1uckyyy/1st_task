import random

nums = [i for i in range(10)]
random_number = ''.join([str(nums.pop(nums.index(random.choice(nums)))) for _ in range(4)])

bull_sklonenie = {0: 'быков', 1: 'бык', 2: 'быка', 3: 'быка', 4: 'быка',
                  5: 'быков', 6: 'быков', 7: 'быков', 8: 'быков', 9: 'быков'}
cow_sklonenie = {0: 'коров', 1: 'корова', 2: 'коровы', 3: 'коровы', 4: 'коровы',
                 5: 'коров', 6: 'коров', 7: 'коров', 8: 'коров', 9: 'коров'}

while True:
    number = input('Введите четырехзначное число: ')
    if not(number.isdigit() and len(number) == 4):
        print('Неправильный ввод!')
        continue
    if number == random_number:
        print('Угадали!', random_number)
        break
    cows = 0
    bulls = 0
    for i in range(len(number)):
        if number[i] == random_number[i]:
            bulls += 1
        elif number[i] in random_number:
            cows += 1
    print('Не угадали!')
    print(f'{cows} {cow_sklonenie[cows]}, {bulls} {bull_sklonenie[bulls]}')

input('Нажмите Enter для выхода\n')
