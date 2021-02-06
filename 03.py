q = list(map(int, input().split()))
a, b, c = q[0], q[1], q[2]
if a == 90 or b == 90 or c == 90 or a == b or b == c or c == a:
  print("1")

