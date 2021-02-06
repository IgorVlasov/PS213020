q = list(map(int, input().split()))
a, b, c = q[0], q[1], q[2]
if a + b + c == 180:
  if a == 90 or b == 90 or c == 90 or a == b or a == c or b == c:
    print(1)
  else:
    print(0)
else:
  print("Какой-то несуществующий треугольник у вас")