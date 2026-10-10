x = float(input())
y = float(input())
if x == 0 and y == 0:
    print('Начало координат')
if x == 0 and y != 0:
    print('Ось Х')
if x != 0 and y == 0:
    print('Ось Y')
if x > 0 and y > 0:
    print('I четверть')
if x < 0 and y > 0:
    print('II четверть')
if x < 0 and y < 0:
    print('III четверть')
if x > 0 and y < 0:
    print('IV четверть')




