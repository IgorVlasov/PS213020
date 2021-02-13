x = int(input())
x1 = x // 1000
x2 = x // 100 % 10
x3 = x % 10//10
x4 = x % 10
if x3 != 0  and x4 != 0:
  x = x - (x3 ** 2 * x4 ** 2)
else:
  x = x - x1 ** 2

print(x)