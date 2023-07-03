import datetime

class Musica:
  def __init__(self, titulo, artista, album, minutos, segundos):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
    self.__dataInclusao = datetime.date.today()
    self.__duracao = datetime.timedelta(seconds=segundos, minutes=minutos)

  def get_tituloEartista(self):
    return f'- {self.__titulo}, {self.__artista}'
  
  def get_duracao(self):
    return self.__duracao

  def __str__(self):
    return f'Título: {self.__titulo}\nArtista: {self.__artista}\nÁlbum: {self.__album}\nData de inclusão: {self.__dataInclusao}\nDuração: {self.__duracao}'

class PlayList:
  def __init__(self, nome, descricao):
    self.__nome = nome
    self.__descricao = descricao
    self.musicas = []

  def set_nome(self, nome):
    if nome == '': raise ValueError()
    else: self.__nome = nome

  def set_desc(self, desc):
    self.__descricao =  desc

  def Inserir(self, m):
    self.musicas.append(m)

  def Listar(self):
    return self.musicas

  def TempoTotal(self):
    soma = datetime.timedelta(minutes=0, seconds=0)
    for i in self.musicas:
      soma += i.get_duracao()
    return soma

  def __str__(self):
    return f'Nome da playlist: {self.__nome}\nDescrição: {self.__descricao}'

class UI:
  def main():
    print('Bem vindo! Crie sua playlist:\n')
    nome = input('Nome: ')
    desc = input('Descrição: ')
    print('\nPlaylist criada!\n')
    playlist = PlayList(nome, desc)
    user = 7
    while user != 0:
      print('O que você quer fazer?\n')
      print('[1] Editar nome [2] Editar descrição [3] Inserir música [4] Listar músicas [5] Mostrar duração total da playlist [6] Mostrar detalhes [0] Encerrar\n')
      user = int(input())
      if user == 1:
        novoNome = input('Insira o novo nome: ')
        playlist.set_nome(novoNome)
        print('Nome editado com sucesso.\n')
      if user == 2:
        novaDesc = input('Insira a nova descrição: ')
        playlist.set_desc(novaDesc)
        print('Descrição editada com sucesso.\n')
      if user == 3:
        titulo = input('Título: ')
        artista = input('Artista: ')
        album = input('Álbum: ')
        minutos, segundos = map(int, input('Duração(mm:ss): ').split(':'))
        musica = Musica(titulo, artista, album, minutos, segundos)
        playlist.Inserir(musica)
        print('\nMúsica inserida! Detalhes:\n')
        print(musica)
        print('')
      if user == 4:
        for l in playlist.Listar():
          print(l.get_tituloEartista())
        print('')
      if user == 5:
        print(f'\nTempo total: {playlist.TempoTotal()}')
        print('')
      if user == 6:
        print('')
        print(playlist)
        print('')
    print('Fim.')

UI.main()