print('Digite quatro números inteiros')
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
somapar = 0
somaimpar = 0
if v1 % 2 == 0:
  somapar += v1
else:
  somaimpar += v1
if v2 % 2 == 0:
  somapar += v2
else:
  somaimpar += v2
if v3 % 2 == 0:
  somapar += v3
else:
  somaimpar += v3
if v4 % 2 == 0:
  somapar += v4
else:
  somaimpar += v4
print(f'\nSoma dos pares = {somapar}')
print(f'Soma dos ímpares = {somaimpar}')
