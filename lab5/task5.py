pakupki = 0
cost = 0
while True:
    try: n = int(input())
    except: break
    pakupki += 1
    cost += n


print(f'Покупок: {pakupki}')
print(f'Общая стоимость: {cost}')
print(f'Средняя стоимость: {cost / pakupki}')
