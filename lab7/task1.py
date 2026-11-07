numbers = list(map(int, input().split()))
copynumbers = numbers.copy()
for item in range(len(copynumbers)):
    if copynumbers[item] < 0:
        copynumbers[item] = 0
print(f'Исходные остатки: {numbers}')
print(f'Исправленные остатки: {copynumbers}')

