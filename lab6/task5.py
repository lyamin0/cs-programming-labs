n = int(input())
if n not in range(1, 11):
    print('Ошибка')
    exit()
for i in range(n):
    row = []
    for j in range(n):
        if i > j:
            dist = i - j
        else:
            dist = j - i
        row.append(str(dist))
    print(' '.join(row))