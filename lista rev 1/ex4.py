print('Digite o primeiro horário no formato hh:mm')
h1, m1 = map(int, input().split(':'))
print('Digite o segundo horário no formato hh:mm')
h2, m2 = map(int, input().split(':'))
somahoras = h1 + h2
somaminutos = m1 + m2
if somaminutos >= 60:
  somahoras += 1
  somaminutos -= 60
if somahoras <= 9:
  print(f'Total de horas = 0{somahoras}:{somaminutos}')
else:
  print(f'Total de horas = {somahoras}:{somaminutos}')
