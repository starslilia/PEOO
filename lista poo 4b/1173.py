v = int(input())
n = []
n.append(v)
while len(n) < 10:
  n.append(v * 2)
  v = v * 2
for i in range(10):
  print(f'N[{i}] = {n[i]}')
