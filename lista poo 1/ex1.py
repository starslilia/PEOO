class circulo:
    def __init__(self):
        self.__raio = 0
    def set_raio(self, raio):
      if raio > 0: self.__raio = raio
      else: raise ValueError()
    def get_raio(self):
      return self.__raio
    def calc_area(self):
      return 3.14 * self.__raio**2
    def calc_circ(self):
      return (2 * 3.14) * self.__raio

class UI:
  @staticmethod
  def main():
    r = float(input())
    x = circulo()
    x.set_raio(r)
    print(f'{x.calc_area():.1f}')
    print(f'{x.calc_circ():.1f}')

UI.main
