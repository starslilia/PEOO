maior = 0
for i in range(1, 6):
  v = int(input())
  if v > maior:
    maior = v
    p = i + 1
print(maior)
print(p)
