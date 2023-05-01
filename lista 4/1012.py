n = input().split()
a = float(n[0])
b = float(n[1])
c = float(n[2])
tri = (a * c) / 2
cir = 3.14159 * c ** 2
tra = ((a + b) * c) / 2
qua = b ** 2
ret = a * b
print(f'TRIANGULO: {tri:.3f}\n'
      f'CIRCULO: {cir:.3f}\n'
      f'TRAPEZIO: {tra:.3f}\n'
      f'QUADRADO: {qua:.3f}\n'
      f'RETANGULO: {ret:.3f}')