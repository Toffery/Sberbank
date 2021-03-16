n = int(input())
list1 = [input().split(',') for i in range(n)]
for i in range(n):
    for j in range(1):
        print('Номер бронирования ', list1[i][j], ', ', sep='' ,end='')
        print('забронирован ', list1[i][j + 1], '. ', sep='', end='')
        a = list1[i][j + 2]
        a = a.split('.')
        print('Цена:', a[0], 'руб.', a[1], 'коп.')