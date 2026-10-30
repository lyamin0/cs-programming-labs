n = int(input())
if n < 2:
    print('Не простое')
    exit()
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print('Не простое')
        break
else:
    print('Простое')