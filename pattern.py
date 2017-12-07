st='GNIUSRANJAN'
#print(len(st))
n=len(st)
'''
for i in range(6):
    print(' ' * (5 - i), end='')
    for j in range(2*i+1):
        print(abs(abs(j-i)-i),end='')
    print(' ' * (5 - i))
for i in range(4,-1,-1):
    print(' ' * (5 - i), end='')
    for j in range(2*i+1):
        print(abs(abs(j-i)-i),end='')
    print(' ' * (5 - i))
'''
for i in range(4):
    for j in range(i):
        print(str(4-j),end='')
    print(str(4-i)*(2*(4-i)-1),end='')
    for k in range(4-i+1,5):
        print(str(k), end='')
    print()
for i in range(2,-1,-1):
    for j in range(i):
        print(str(4-j),end='')
    print(str(4-i)*(2*(4-i)-1),end='')
    for k in range(4-i+1,5):
        print(str(k), end='')
    print()

