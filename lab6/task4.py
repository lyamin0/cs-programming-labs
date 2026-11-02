n = int(input())

if n < 0:
    print('Ошибка')
else:
    digits = 0
    digit_sum = 0
    if n == 0:
        digits = 1
        digit_sum = 0
    else:
        while n > 0:
            digit = n % 10
            digit_sum += digit
            digits += 1
            n = n // 10

    print(f'Цифр: {digits}')
    print(f'Сумма цифр: {digit_sum}')