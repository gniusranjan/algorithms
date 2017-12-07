from itertools import product
row=4
column=[0,1,2,3]
check=[0,-1,+1,max(column),-max(column)]
matrix=list(product(column,repeat=row))
print(len(matrix))
result=[]
def diff(l):
    a=0
    for i in range(max(column))  :
        if l[i]-l[i+1] in check:
            a=a+1
    if a==max(column):
        result.append(l)

for i in matrix:
    diff(list(i))
print(len(result))