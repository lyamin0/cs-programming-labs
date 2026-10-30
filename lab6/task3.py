n = int(input())
if n < 2:
    print('Ошибка')
    exit()
else:
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    print(*factors)