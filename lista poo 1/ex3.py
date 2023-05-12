class viagem:
  def _init_(self):
    self.dist = 0
    self.tempo = 0
  def velocidade(self):
    return self.dist / self.tempo
x = viagem()
x.dist = float(input())
x.tempo = float(input())
print(f'{x.velocidade():.1f}')
