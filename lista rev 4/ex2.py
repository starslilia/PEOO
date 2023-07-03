class Esporte:
  def __init__(self, nome, horarios, mensalidade):
    self.__nome = nome
    self.__horarios = horarios
    self.__mensalidade = mensalidade

  def get_mensalidade(self):
    return self.__mensalidade

  def __str__(self):
    return f'Esporte: {self.__nome}\nHorários: {self.__horarios}\nMensalidade: {self.__mensalidade:.2f}'

class Academia:
  def __init__(self, nome, endereco):
    self.__nome = nome
    self.__endereco = endereco
    self.esportes = []

  def set_nome(self, n):
    if n == '': raise ValueError()
    else: self.__nome = n

  def set_endereco(self, e):
    if e == '': raise ValueError()
    else: self.__endereco = e
      
  def Inserir(self, e):
    self.esportes.append(e)

  def Listar(self):
    return self.esportes

  def MediaMensalidade(self):
    media = 0
    for i in self.esportes:
      media += i.get_mensalidade()
    return media / len(self.esportes)

  def __str__(self):
    return f'Nome da academia: {self.__nome}\nEndereço: {self.__endereco}'

class UI:
  def main():
    print('Crie sua academia!\n')
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    academia = Academia(nome, endereco)
    user = 10
    while user != 0:
      print('O que você quer fazer?\n')
      print('[1] Editar nome [2] Editar endereço [3] Inserir esporte [4] Listar esportes [5] Calcular média de mensalidades [6] Ver detalhes [0] Encerrar\n')
      user = int(input())
      if user == 1:
        novoNome = input('Insira o novo nome: ')
        academia.set_nome(novoNome)
        print('Nome modificado com sucesso.\n')
      if user == 2:
        novoEndereco = input('Insira o novo endereço: ')
        academia.set_endereco(novoEndereco)
        print('Endereço atualizado com sucesso.\n')
      if user == 3:
        modalidade = input('Modalidade: ')
        horarios = input('Horários: ')
        mensalidade = float(input('Mensalidade: '))
        esporte = Esporte(modalidade, horarios, mensalidade)
        academia.Inserir(esporte)
        print('\nEsporte adicionado com sucesso!\n')
      if user == 4:
        for e in academia.Listar():
          print(e)
          print('')
      if user == 5:
        print(f'Média: {academia.MediaMensalidade():.2f}\n')
      if user == 6:
        print(academia)
        print('')
    print('Fim.')

UI.main()