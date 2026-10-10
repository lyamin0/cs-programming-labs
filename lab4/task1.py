current = float(input())
desired = float(input())
if current > desired:
    print('Охлаждение')
elif current < desired:
    print('Нагрев')
else:
    print('Выключен')


