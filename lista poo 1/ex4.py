class cinema:
  def __init__(self):
    self.dia = ''
    self.hora = 0
  def calc_entrada(self):
    if self.dia == 'segunda' or self.dia == 'terca' or self.dia == 'quinta':
      ingresso = 16
    elif self.dia == 'quarta':
      ingresso = 8
    elif self.dia == 'sexta' or self.dia == 'sabado' or self.dia == 'domingo':
      ingresso = 20
    if self.hora >= 17 and self.hora < 24:
      ingresso = ingresso + (ingresso * 50) / 100
    return ingresso

x = cinema()
x.dia = input()
x.hora = int(input())
if x.dia == 'quarta':
  print(f'A entrada será {x.calc_entrada() - 4:.2f} R$')
else:
  print(f'A entrada inteira será {x.calc_entrada():.2f} R$, e meia entrada será {x.calc_entrada() / 2:.2f} R$')
  