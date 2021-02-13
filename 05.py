q = input()
a, b, c, d = q[0], q[1], q[2], q[3]
w = []
w.append(int(a))
w.append(int(b))
w.append(int(c))
w.append(int(d))
max1, min1, maxind, minind = max(w), min(w), w.index(max(w)), w.index(min(w))
w[maxind], w[minind] = min1, max1
for i in range(len(w) - 1):
  print(w[i], end=" ")
print(w[-1])