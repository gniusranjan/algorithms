'''
x=int(input())
l=set()
for i in range(x):
    for j in range(x-i):
        l.add((i,j))
        l.add((-i,j))
        l.add((-i,-j))
        l.add((i,-j))
t=[]
p,q=1,0
for i in l:
    t.append([p+i[0],q-i[1]])

print(l)
print(t)
'''
'''
mat=[
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]
m=len(mat)
n=len(mat[0])
a=[[0]*n for i in range(m)]
for i in range(n):
    a[0][i]=mat[0][i]
for i in range(m):
    a[i][0]=mat[i][0]
ans=0
for i in range(1,m):
    for j in range(1,n):
        x=a[i-1][j-1]
        if mat[i][j]==0:
            a[i][j]=0
        elif x>0:
            for k in range(x,0,-1):
                if sum(mat[i][j-x:j+1])==x+1 and sum([mat[t][j] for t in range(i-x,i+1)])==x+1:
                    #print('dog')
                    a[i][j]=x+1
                    if a[i][j]>ans:
                        ans=a[i][j]
                    break

#recur(mat,0,0)
print(ans)
'''
ma=[
[1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]
mat=[[1]]
m=len(mat)
n=len(mat[0])
a=[[0]*n for i in range(m)]
b=list(a)

an=0
for i in range(m):
    for j in range(n):
        if j==0:
            a[i][j]=mat[i][j]
            an=max(an,a[i][j])
        elif mat[i][j]==1:
            a[i][j]=a[i][j-1]+1
            an=max(an,a[i][j])
            #print(an)

for i in range(1,m):
    for j in range(1,n):
        x=a[i][j]
        if x>0:
            mi=x
            for k in range(i):
                if a[i-k-1][j]==0:
                    break
                elif a[i-k-1][j]<mi:
                    mi=a[i-k-1][j]
                    an=max(an,mi*(k+2))
                else:
                    an = max(an, mi * (k + 2))
print(an)


















