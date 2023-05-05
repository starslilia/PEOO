a1 = int(input())
a2 = int(input())
a3 = int(input())
minA1 = a2 * 2 + a3 * 4
minA2 = a1 * 2 + a3 * 2
minA3 = a1 * 4 + a2 * 2
if min(minA1, minA2, minA3) == minA1:
  print(minA1)
elif min(minA1, minA2, minA3) == minA2:
  print(minA2)
else:
  print(minA3)
