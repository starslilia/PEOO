n1, n2 = map(int, input('Insira dois números inteiros: ').split())
def menor(x, y):
  if x < y:
    m = x
  else:
    m = y
  return m
print(menor(n1, n2))
