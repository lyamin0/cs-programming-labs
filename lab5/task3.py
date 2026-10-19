n = int(input())
nizhe = 0
vishe = 0
raven  = 0
for item in range(n):
    temp = float(input())
    if temp < 0:
        nizhe += 1
    elif temp > 0:
        vishe += 1
    else:
        raven += 1
print(f'Ниже нуля: {nizhe}')
print(f'Равны нулю: {raven}')
print(f'Выше нуля: {vishe}')


