n = int(input())
cont = 3
t1, t2 = 0, 1
print(f'{t1} {t2}', end=' ')
while cont <= n:
  t3 = t1 + t2
  cont += 1
  t1 = t2
  t2 = t3
  print(f'{t3}', end=' ')