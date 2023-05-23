class bhaskara:

  def __init__(self, a, b, c):
    self.__a = 1
    self.__b = 0
    self.__c = 0
    self.set_a(a)
    self.set_b(b)
    self.set_c(c)

  def set_a(self, v):
    if v > 0: self.__a = v
    else: raise ValueError()

  def set_b(self, v):
    if v == str: raise ValueError()
    else: self.__b = v

  def set_c(self, v):
    if v == str: raise ValueError()
    else: self.__c = v

  def get_a(self):
    return self.__a

  def get_b(self):
    return self.__b

  def get_c(self):
    return self.__c

  def calc_delta(self):
    return self.__b**2 - 4 * self.__a * self.__c

  def tem_raizreal(self):
    if self.calc_delta() >= 0: return True
    else: return False

  def calc_raiz1(self):
    return (-self.__b + (self.calc_delta())**0.5) / (2 * self.__a)

  def calc_raiz2(self):
    return (-self.__b - (self.calc_delta())**0.5) / (2 * self.__a)

  def __str__(self):
    return f'a = {self.__a} b = {self.__b} c = {self.__c} Delta = {self.calc_delta()}'


class UI:

  @staticmethod
  def main():
    x = bhaskara(float(input()), float(input()), float(input()))
    print(x)
    print(x.tem_raizreal())
    if x.tem_raizreal() == True:
      print(x.calc_raiz1())
      print(x.calc_raiz2())
    else:
      print('FIM')
      
UI.main()
