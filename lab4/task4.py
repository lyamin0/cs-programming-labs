a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif (a < 0 or b < 0 or c < 0
    or a + b <= c or a + c <= b
    or c + b <= a):
    print('Треугольник не существует')
elif a == b or b == c or c == a:
    print('Равнобедренный')
else:
    print('Разносторонний')


