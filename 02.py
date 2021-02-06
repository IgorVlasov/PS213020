a = input()
b, c = a[-2], a[-1]
if b != "0" and c !="0":
  d = (int(b) ** 2) * (int(c) ** 2)
  print (int(a) - int(d))
else:
  print(int(a) - int(a[0]) ** 2)