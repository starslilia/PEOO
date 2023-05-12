class cinema:
  def _init_(self):
    self.dia = ''
    self.hora = 0
  def calc_entrada(self):
    if self.dia == 'segunda' or self.dia == 'terca' or self.dia == 'quinta':
      ingresso = 16
    elif self.dia == 'quarta':
      ingresso = 8
    elif self.dia == 'sexta' or self.dia == 'sabado' or self.dia == 'domingo':
      ingresso = 20
    return ingresso
  def calc_entrada_2(self):
    return ingresso * 50 / 100

x = cinema()
x.dia = input()
x.hora = int(input())
if x.dia == 'quarta':
  print(f'A entrada será {x.calc_entrada():.2f} R$')
else:
  print(f'A entrada inteira será {x.calc_entrada():.2f} R$, e meia entrada será {x.calc_entrada() / 2:.2f} R$')
if x.hora >= 17 and x.hora < 24:
  print(f'A entrada será {x.calc_entrada_2():.2f} R$')
