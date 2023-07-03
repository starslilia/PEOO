import random

class Bingo:
  def __init__(self):
    self.__numBolas = 1
    self.__sorteados = []
  def Iniciar(self, numBolas):
    if numBolas > 0: 
      self.__numBolas = numBolas
      self.__sorteados = []
    else: raise ValueError()
  def Proximo(self):
    if len(self.__sorteados) == self.__numBolas:
      return -1
    x = random.randrange(1, self.__numBolas + 1)
    while x in self.__sorteados:
      x = random.randrange(1, self.__numBolas + 1)
    self.__sorteados.append(x)
    return x
  def Sorteados(self):
    s = self.__sorteados
    s.sort()
    return s

class UI:
  def main():
    op = int(input('1 - Novo jogo, 2 - Sortear, 3 - Sorteados, 0 - Fim: '))
    jogo = Bingo()
    while op != 0:
      if op == 1:
        bolas = int(input('Insira quantos números podem ser sorteados: '))
        jogo.Iniciar(bolas)
      if op == 2:
        p = jogo.Proximo()
        if p == -1: print('Você já sorteou todas as bolas')
        else: print(f'A bola sorteada foi {p}')
      if op == 3:
        print(f'Bolas já sorteadas: {jogo.Sorteados()}')
      op = int(input('1 - Novo jogo, 2 - Sortear, 3 - Sorteados, 0 - Fim: '))
    print('Fim')

UI.main()
