new=input()
j=new.split(' ')
i=int(j[0])
v=0
m=[]
while(v<i):
    x=input()
    m.append(x)
    v=v+1
print(m)
a=0
while(a<i):
    m[a]= m[a].split(' ')
    a=a+1
print(m)
n=[]
for b in m:
    n.append(int(b[1]))
#print(n)
n.sort()
print('answer')
for y in n:
    for x in m:
        if int(x[1])==y:
            print(x)