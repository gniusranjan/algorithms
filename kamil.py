'''
A=[
  [0, 0]
]
n = len(A[0]) - 1
m = len(A) - 1
count = 0
def recur(i, j):
    global count
    if A[i][j] == 1:
        return 0
    elif i == m and j == n:
        count = count + 1
    elif i < m and j < n:
        recur(i + 1, j)
        recur(i, j + 1)
    elif i == m and j < n:
        recur(i, j + 1)
    elif i < m and j == n:
        recur(i + 1, j)
recur(0, 0)
print(count)
'''
l=[5,5,8,5]
f=['d','ds']
if l==f:
    print(''.join(f))














