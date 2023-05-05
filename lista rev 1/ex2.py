print('Digite quatro valores inteiros')
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
media = (v1 + v2 + v3 + v4) / 4
print(f'\nMédia = {media:.0f}')
menor = []
maiorouigual = []
if v1 < media:
  menor.append(v1)
if v2 < media:
  menor.append(v2)
if v3 < media:
  menor.append(v3)
if v4 < media:
  menor.append(v4)
if v1 >= media:
  maiorouigual.append(v1)
if v2 >= media:
  maiorouigual.append(v2)
if v3 >= media:
  maiorouigual.append(v3)
if v4 >= media:
  maiorouigual.append(v4)
print('Números menores que a média')
print(menor)
print('Números maiores ou iguais à média')
print(maiorouigual)