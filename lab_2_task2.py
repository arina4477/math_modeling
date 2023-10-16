a=int(input('Введите первый член прогрессии: '))
b=int(input('Введите знаменатель:'))
c=int(input('Введите количество членов:'))

d = 1

for i in range(1, c + 1):
    print(a * b**(i-1))
