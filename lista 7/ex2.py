n1, n2, n3 = map(int, input('Digite três números: ').split())
def maior(x, y, z):
  if x > y and x > z:
    m = x
  elif y > x and y > z:
    m = y
  else:
    m = z
  return m
print(maior(n1, n2, n3))
