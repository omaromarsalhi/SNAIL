x=True
while x == True:
 w = int(input())
 if (w>=1) and (w<=100):
     x = False
if (w % 2 != 0 ) or (   w == 2) :
    print('NO')
else:
    print('YES')