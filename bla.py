cont,lis=[int(i) for i in input().split(" ")],[int(i) for i in input().split(" ")]
print(sum([ (i>=lis[cont[1]-1] and i>0) for i in lis ] ) )