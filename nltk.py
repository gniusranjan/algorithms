n = int(input())
w = []
c = []
for i in range(n):
    x = input()
    a, b = list(map(int, x.split()))
    w.append(a)
    c.append(b)
m = 30
print(w,c)
def recur(w, c, n, m):
    #global t
    if m <= 0 or n <= 0:
       # print('cat')
        return 0
    if w[n - 1] > m:
        #print('dog')
        return recur(w, c, n - 1, m)
    else:
        #t=max(c[n - 1] + recur(w, c, n - 1, m - w[n - 1],t), recur(w, c, n - 1, m,t))
        return max(c[n - 1] + recur(w, c, n, m - w[n - 1]), recur(w, c, n-1 , m))

t=0
#for i in range(1, m + 1):

print(recur(w,c,n,m))
