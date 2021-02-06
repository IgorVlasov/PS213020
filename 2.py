a = input()
b, c = a[-2], a[-1]
print(int(a) - (int(b) ** 2) * (int(c) ** 2)) if b != "0" and c != "0" else print(int(a) - int(a[0]) ** 2)