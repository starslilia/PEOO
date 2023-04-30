print('Digite a base e a altura do retângulo')
b = float(input())
h = float(input())
a = b * h
p = b * 2 + h * 2
d = (b**2 + h**2) ** 0.5
print(f'\nÁrea = {a:.2f} - Perímetro = {p:.2f} - Diagonal = {d:.2f}')