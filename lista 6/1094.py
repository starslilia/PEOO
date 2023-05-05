n = int(input())
tot, totcoelho, totrato, totsapo = 0, 0, 0, 0
for i in range(1, n+1):
  a = input().split()
  q = int(a[0])
  e = a[1]
  tot += q
  if e == 'C':
    totcoelho += q
  elif e == 'R':
    totrato += q
  else:
    totsapo += q
percentcoelho = (totcoelho * 100) / tot
percentrato = (totrato * 100) / tot
percentsapo = (totsapo * 100) / tot
print(f'Total: {tot} cobaias')
print(f'Total de coelhos: {totcoelho}')
print(f'Total de ratos: {totrato}')
print(f'Total de sapos: {totsapo}')
print(f'Percentual de coelhos: {percentcoelho:.2f} %')
print(f'Percentual de ratos: {percentrato:.2f} %')
print(f'Percentual de sapos: {percentsapo:.2f} %')
