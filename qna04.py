x = int(input())
x1 = x // 1000
x2 = x // 100 % 10
x3 = x % 10//10
x4 = x % 10

x12 = x1*x2
x23 = x2 * x3
x34 = x3 * x4

if x12 % 3 == 0 and x23 % 5 == 0 and x34 % 10 == 0:
  print(x12 + x23 + x34)
elif x12 % 3 == 0:
  print(0)
elif x23 % 5 == 0:
  print(1)
elif x34 % 10 == 0:
  print(2)