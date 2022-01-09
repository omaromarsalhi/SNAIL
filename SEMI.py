x= True
while x == True:
    n = int(input())
    if n in range(1,101):
        x= False
tab=[]
for i in range(n):
    y= True
    while y== True :
        temp=input()
        if( (temp[0] == temp[0].lower() ) and (temp[-1] == temp[-1].lower())  and (len(temp) in range(1,101))):
            y= False
    tab.append(temp)
for i in tab:
    if (len(i) <= 10):
        print(i)
    else:
        print(i[0]+str(len(i)-2)+i[-1])
