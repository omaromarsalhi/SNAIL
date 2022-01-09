x={'0','1'}
z=True
while z:
    sit=input()
    k=len(sit)
    y=True
    for i in range(k):
        if (sit[i] in x) :
            y= False
    w=True
    if (k in range(1, 101)):
        w=False
    if (y==False ) and (w==False) :
        z= False
s=1
c=True
for i in range(k-1) :
    if sit[i]==sit[i+1]:
        s+=1
        if s >= 7:
            print('YES')
            c=False
            break
    elif sit[i]!=sit[i+1]:
        s=1
if c==True:
    print('NO')