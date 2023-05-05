base, altura = map(float, input('Insira a base e a altura do retângulo: ').split())
def diagonal(b, h):
  d = (b ** 2 + h ** 2) ** 0.5
  return d
print(f'{diagonal(base, altura):.2f}')
