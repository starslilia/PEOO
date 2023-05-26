class PeçaDominó:
  def __init__(self, lado1, lado2):
    self.__lado1 = 0
    self.__lado2 = 0
    self.set_lado1(lado1)
    self.set_lado2(lado2)

  def set_lado1(self, l):
    if 0 < l <= 6: self.__lado1 = l
    else: raise ValueError()
  def set_lado2(self, l):
    if 0 < l <= 6: self.__lado2 = l
    else: raise ValueError()
  def get_lado1(self):
    return self.__lado1
  def get_lado2(self):
    return self.__lado2

  def __str__(self):
    return f'Lado 1: {self.__lado1}\nLado 2: {self.__lado2}'

  def combinar(self, l1, l2):
    if 0 < l1 <= 6 or 0 < l2 <= 6:
      if l1 == self.__lado1 or l1 == self.__lado2 or l2 == self.__lado1 or l2 == self.__lado2: return True
      else: return False
    else: raise ValueError()
  
class UI:
  def main():
    x = PeçaDominó(int(input('Insira o primeiro lado da sua peça: ')), int(input('Insira o segundo lado da peça: ')))
    combina = x.combinar(int(input('Insira o primeiro lado da outra peça: ')), int(input('Insira o segundo lado da outra peça: ')))
    print(combina)

UI.main()
