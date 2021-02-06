d = list(map(int, input().split()))
a, b, c = d[0], d[1], d[2]
if a == 90 or b == 90 or c == 90 or a == b or a == c or b == c:
  print(1)
else:
  print(0) 