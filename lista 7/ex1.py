n1, n2 = map(int, input('Insira dois valores inteiros: ').split())

def maior(x, y):
  if x > y:
    m = x
  else:
    m = y
  return m

print(maior(n1, n2))
