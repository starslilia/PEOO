x = []
for c in range(10):
  v = int(input())
  x.append(v)
k = 0
while k < 10:
  if x[k] <= 0: x[k] = 1
  k += 1
for i in range(10):
  print(f'X[{str(i)}] = {x[i]}')