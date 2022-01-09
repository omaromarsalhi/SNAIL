x =True
while x == True:
    n = int(input())
    if n in range(1,1001):
        x = False
k=0
lighne=[]
for i in range(n):
    lighne.append(input())
for i in lighne:
    summ = int(i[0]) + int(i[2]) + int(i[-1])
    if summ >=2:
         k+=1
print(k)





