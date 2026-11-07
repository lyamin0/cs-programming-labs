numbers = list(map(int, input().split()))
total = int(input())
indexes = []
for index, number in enumerate(numbers):
    if number == total:
        indexes.append(index)
print(f'Индексы: {indexes}')