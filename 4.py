a = input()
a1, a2, a3, a4 = int(a[0]), int(a[1]), int(a[2]), int(a[3])
q, w, e = a1 * a2, a2 * a3, a3 * a4
r = 0
if q % 3 == 0:
  print(0)
  r += 1
if w % 5 == 0:
  print(1)
  r += 1
if e % 10 == 0:
  print(2)
  r += 1
if r == 3:
  print(q + w + e)