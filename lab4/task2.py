cost = float(input())
age = int(input())
if cost >= 0 and 0 <= age <= 120:
    if 0 <= age <= 5:
        cost = 0
    elif 6 <= age <= 17:
        cost /= 2
    elif 60 <= age <= 120:
        cost *= 0.7
print(f'Стоимость: {cost:.2f}')


