class disciplina:
    def _init_(self):
      self.nome = ''
      self.n1 = 0
      self.n2 = 0
      self.n3 = 0
      self.n4 = 0
      self.pf = 0

    def media_parc(self):
      return (self.n1 * 2 + self.n2 * 2 + self.n3 * 3 + self.n4 * 3) / 10

    def media_final(self):
      return (((self.n1 * 2 + self.n2 * 2 + self.n3 * 3 + self.n4 * 3) / 10) + self.pf) / 2

x = disciplina()
x.nome = input()
x.n1 = int(input())
x.n2 = int(input())
x.n3 = int(input())
x.n4 = int(input())
print(f'{x.media_parc()}')
if x.media_parc() < 60:
  print('Prova final')
  x.pf = int(input())
  print(f'{x.media_final()}')
  if x.media_final() >= 60:
    print('Aprovado')
  else:
    print('Reprovado')
else:
  print('Aprovado')
