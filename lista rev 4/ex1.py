class Jogador:
  def __init__(self, nome, camisa, gols):
    self.__nome = nome
    self.__camisa = camisa
    self.__gols = gols

  def get_nome(self):
    return self.__nome

  def get_gols(self):
    return self.__gols
  
  def __str__(self):
    return f'Nome: {self.__nome}\nCamisa: {self.__camisa}\nGols: {self.__gols}'

class Time:
  def __init__(self, nome, estado):
    self.__nome = nome
    self.__estado = estado
    self.jogadores = []

  def Inserir(self, j):
    self.jogadores.append(j)

  def Listar(self):
    return self.jogadores

  def Artilheiro(self):
    artilheiro = self.jogadores[0]
    for i in self.jogadores:
      if i.get_gols() > artilheiro.get_gols():
        artilheiro = i
    return artilheiro

  def __str__(self):
    return f'Nome do time: {self.__nome}\nEstado: {self.__estado}\nJogadores: {self.jogadores}'

class UI:
  def main():
    nometime = input('Insira o nome do time: ')
    estado = input('Insira o estado do time: ')
    time = Time(nometime, estado)
    print('')
    print(time)
    user = 4
    while user != 0:
      print('\nO que você quer fazer?')
      print('\nInserir jogador[1] Listar jogadores[2] Mostrar Artilheiro[3] Encerrar[0]\n')
      user = int(input())
      if user == 1:
        print('')
        nomejogador = input('Insira o nome do jogador: ')
        camisa = int(input('Insira a camisa do jogador: '))
        gols = int(input('Insira o número de gols do jogador: '))
        jogador = Jogador(nomejogador, camisa, gols)
        time.Inserir(jogador)
        print('')
        print(jogador)
      if user == 2:
        for i in time.Listar():
          print('')
          print(i)
          print('')
      if user == 3:
        print('')
        print(time.Artilheiro())
    print('')
    print('Fim')

UI.main()