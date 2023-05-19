class viagem:
  def __init__(self):
    self.__dist = 0
    self.__tempo = 0
  def set_dist(self, dist):
    if dist > 0: self.__dist = dist
    else: raise ValueError()
  def get_dist(self):
    return self.__dist
  def set_tempo(self, tempo):
    if tempo > 0: self.__tempo = tempo
    else: raise ValueError()
  def get_tempo(self):
    return self.__tempo
  def velocidade(self):
    return self.__dist / self.__tempo

class UI:
  @staticmethod
  def main():
    x = viagem()
    d = float(input())
    x.set_dist(d)
    horas, minutos = map(int, input().split())
    t = horas + minutos / 60
    x.set_tempo(t)
    print(f'{x.velocidade():.1f}')

UI.main()
