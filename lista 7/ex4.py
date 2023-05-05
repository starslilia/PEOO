n1 = int(input('Insira sua nota do primeiro bimestre: '))
n2 = int(input('Insira sua nota do segundo bimestre: '))
def aprovado(nota1, nota2):
  media = (n1 + n2) / 2
  print(f'{int(media)}')
  if media >= 60:
    print('Aprovado')
  else:
    print('Prova final')
