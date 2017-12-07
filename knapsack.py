'''
w=[4,2,10]
v=[25,11,60]
m=30
'''
v=[60,100,120]
w=[10,20,30]
m=50
#k=[[0 for x in range(m+1)] for x in range(len(w)+1)]
k=[[0]*(m+1)for x in range(len(w)+1)]
print(k)
def knap(w,v,m,k):
    for i in range(len(v)+1):
        for j in range(m+1):
            if j==0 or i==0:
                k[i][j]=0
            elif w[i-1]<=j:
                k[i][j]=max(k[i-1][j],v[i-1]+k[i-1][j-w[i-1]])
            else:
                k[i][j]=k[i-1][j]
    return(k[-1][-1])
print(knap(w,v,m,k))
print(k)