r = float(input('Insira o raio do seu círculo: '))
def areacirculo(raio):
  area = 3.14 * raio ** 2
  return area
print(f'{areacirculo(r):.2f}')
