n = int(input())
if n < 0:
    print('Ошибка')
    exit()
digits = 0
sum = 0
for digit in str(n):
    digits += 1
    sum += int(digit)
print(f'Цифр: {digits}')
print(f'Сумма цифр: {sum}')
