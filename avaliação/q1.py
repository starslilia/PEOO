class Pais:

  def __init__(self, nome, pop, area):
    self.__nome = 'a'
    self.__pop = 0
    self.__area = 0
    self.set_nome(nome)
    self.set_pop(pop)
    self.set_area(area)

  def set_nome(self, n):
    if n == '': raise ValueError()
    else: self.__nome = n

  def set_pop(self, p):
    if p > 0: self.__pop = p
    else: raise ValueError()

  def set_area(self, a):
    if a > 0: self.__area = a
    else: raise ValueError()

  def get_nome(self):
    return self.__nome

  def get_pop(self):
    return self.__pop

  def get_area(self):
    return self.__area

  def dens_demografica(self):
    return self.__pop / self.__area

  def __str__(self):
    return f'Nome: {self.__nome}\nPopulação: {self.__pop}\nÁrea: {self.__area}\nDensidade demográfica: {self.dens_demografica():.2f}'


class UI:

  def main():
    x = Pais(input(), int(input()), float(input()))
    print(f'{x.dens_demografica():.2f}')
    for i in range(9):
      y = Pais(input(), int(input()), float(input()))
      print(f'{y.dens_demografica():.2f}')
      if y.dens_demografica() > x.dens_demografica(): x = y
    print(x)

UI.main()
