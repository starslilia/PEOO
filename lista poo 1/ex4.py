class cinema:
  def __init__(self):
    self.__dia = ''
    self.__hora = 0
  def set_dia(self, dia):
    dias = ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
    if dia in dias: self.__dia = dia
    else: raise ValueError()
  def get_dia(self):
    return self.__dia
  def set_hora(self, hora):
    if hora >= 0 and hora <= 23: self.__hora = hora
  def get_hora(self):
    return self.__hora
  def calc_entrada(self):
    if self.__dia == 'segunda' or self.__dia == 'terca' or self.__dia == 'quinta':
      ingresso = 16
    elif self.__dia == 'quarta':
      ingresso = 8
    elif self.__dia == 'sexta' or self.__dia == 'sabado' or self.__dia == 'domingo':
      ingresso = 20
    if self.__hora >= 17 and self.__hora < 24:
      ingresso = ingresso + (ingresso * 50) / 100
    return ingresso

class UI:
  @staticmethod
  def main():
    d = input()
    h = int(input())
    x = cinema()
    x.set_dia(d)
    x.set_hora(h)
    if d == 'quarta':
      print(f'A entrada será {x.calc_entrada() - 4:.2f} R$')
    else:
      print(f'A entrada inteira será {x.calc_entrada():.2f} R$, e meia entrada será {x.calc_entrada() / 2:.2f} R$')

UI.main()
