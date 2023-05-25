from random import randint

def is_valid(num_rand, number):
    flag = False
    count = 1
    while flag != True:
        n = input(f'Введите число от 1 до {number}: ')
        if n.isdigit() and 1 <= int(n) <= number:
            num = int(n)
            if num < num_rand:
                count += 1
                print('Ваше число меньше загаданного, попробуйте ещё разок')
            elif num > num_rand:
                count += 1
                print('Ваше число больше загаданного, попробуйте ещё разок')
            else:
                flag = True
                print('Вы угадали, поздравляем!', f'Ваше количество попыток: {count}', sep='\n')
                choice = input('Хотите сыграть ещё раз? ' )
                if choice == 'Да':
                    number = int(input())
                    num_rand = randint(1, number)
                    count = 1
                    flag = False
                elif choice == 'Нет':
                    break
        else:
            print(f'А может быть всё-таки введём целое число от 1 до {number}?')

n = int(input())
num_rand = randint(1, n)

print('Добро пожаловать в числовую угадайку')
is_valid(num_rand, n)
print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')