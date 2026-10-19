a = int(input())
b = int(input())
s = 0
p = 1
for i in range(a, b + 1):
    s += i
    p *= i
print(f'Сумма: {s}')
print(f'Произведение: {p}')