a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a % b == 0 and b != 0:
    print(f'{a} делится на {b}')
    print(f'{a} / {b} = {a // b}')
elif b == 0:
    print('на ноль делить нельзя')

else: 
    print(f'{a} не делится на {b}')
    print(f'частное = {a // b}')
    print(f'остаток = {a % b}')
