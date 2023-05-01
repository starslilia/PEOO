v = input().split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
if a != 0:
  delta = b ** 2 - 4 * a * c
  if delta > 0:
    r1 = (-b + delta ** 0.5) / (2 * a)
    r2 = (-b - delta ** 0.5) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
  elif delta == 0:
    r = -b / (2 * a)
    print(f'R = {r:.5f}')
  else:
    print('Impossível calcular')
else:
  print('Impossível calcular')