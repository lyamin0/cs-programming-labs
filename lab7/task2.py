numbers = list(map(int, input().split()))
squared_numbers = [x**2 for x in numbers if x % 2 != 0 and x > 0]
print(f'Квадраты: {squared_numbers}')
