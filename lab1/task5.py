distance = float(input())
gasoline = float(input())
price = float(input())
need = distance / 100 * gasoline
cost = need * price
print(f'Топливо: {need:.2f} л')
print(f'Стоимость: {cost:.2f} л')