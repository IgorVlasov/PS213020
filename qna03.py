a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

if a + b + c != 180:
   print( 0 )
elif (a == b  or b == c or c == a) and (a == 90 or c == 90 or b == 90):
  print( 1 )
else:
  print( 0 )
