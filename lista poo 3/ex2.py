class Frete:
  def __init__(self, d, p):
    self.__d = 0
    self.__p = 0
    self.set_distancia(d)
    self.set_peso(p)

  def set_distancia(self, v):
    if v >= 0: self.__d = v
    else: raise ValueError()
  def set_peso(self, v):
    if v >= 0: self.__p = v
    else: raise ValueError()
  def get_distancia(self):
    return self.__d
  def get_peso(self):
    return self.__p

  def calc_frete(self):
    return (self.__p / self.__d) / 100

  def __str__(self):
    return f'Distância = {self.__d} Peso = {self.__p}'

class UI:
  def main():
    x = Frete(float(input()), float(input()))
    print(x)
    print(f'Frete = {x.calc_frete():.2f} R$')
    x.set_distancia(float(input()))
    x.set_peso(float(input()))
    print(f'Frete = {x.calc_frete():.2f} R$')

UI.main()
