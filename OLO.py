x=True
while x==True:
    num = input()
    num=num.split(" ")
    if  (int(num[0])>=int(num[1])):
        x=False
y= True
while y==True:
    tab=input().split(" ")
    s=len(tab)
    for i in range(s):
        tab[i]=int(tab[i])
    if ((sorted(tab,reverse=True)== tab) and (s == int(num[0]))):
        y=False
k=0
d=int(num[1])
if tab[d-1]==0:
    print('0')
elif tab[d-1]!=0:
    for i in tab:
        if i >= tab[d-1]:
           k+=1
    print(k)