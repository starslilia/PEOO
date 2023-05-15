class disciplina:
    def __init__(self):
      self.__nome = ''
      self.__n1 = 0
      self.__n2 = 0
      self.__n3 = 0
      self.__n4 = 0
      self.__pf = 0
    def set_nome(self, nome):
      materias = ['sociologia', 'artes', 'filosofia', 'matematica', 'fisica', 'geografia', 'portugues', 'ed fisica', 'peoo', 'quimica', 'design']
      if nome in materias: self.__nome = nome
      else: raise ValueError()
    def get_nome(self):
      return self.__nome
    def set_n1(self, n1):
      if n1 >= 0 and n1 <= 100: self.__n1 = n1
      else: raise ValueError()
    def get_n1(self):
      return self.__n1
    def set_n2(self, n2):
      if n2 >= 0 and n2 <= 100: self.__n2 = n2
      else: raise ValueError()
    def get_n2(self):
      return self.__n2
    def set_n3(self, n3):
      if n3 >= 0 and n3 <= 100: self.__n3 = n3
      else: raise ValueError()
    def get_n3(self):
      return self.__n3
    def set_n4(self, n4):
      if n4 >= 0 and n4 <= 100: self.__n4 = n4
      else: raise ValueError()
    def get_n4(self):
      return self.__n4
    def set_pf(self, pf):
      if pf >= 0 and pf <= 100: self.__pf = pf
      else: raise ValueError()
    def get_pf(self):
      return self.__pf
    def media_parc(self):
      return (self.__n1 * 2 + self.__n2 * 2 + self.__n3 * 3 + self.__n4 * 3) / 10
    def media_final(self):
      return (((self.__n1 * 2 + self.__n2 * 2 + self.__n3 * 3 + self.__n4 * 3) / 10) + self.__pf) / 2

class UI:
  @staticmethod
  def main():
    x = disciplina()
    nome = input()
    x.set_nome(nome)
    n1 = int(input())
    x.set_n1(n1)
    n2 = int(input())
    x.set_n2(n2)
    n3 = int(input())
    x.set_n3(n3)
    n4 = int(input())
    x.set_n4(n4)
    print(f'{x.media_parc()}')
    if x.media_parc() < 60:
      print('Prova final')
      pf = int(input())
      x.set_pf(pf)
      print(f'{x.media_final()}')
      if x.media_final() >= 60:
        print('Aprovado')
      else:
        print('Reprovado')
    else:
      print('Aprovado')

UI.main()
