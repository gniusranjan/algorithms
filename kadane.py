array =input().split(' ')
l=[]
s=[]
#print(array)
def add(i):
    k=[int(array[i])]
    while i+1<len(array) and int(array[i+1])>=0 :
        k.append(int(array[i+1]))
        i=i+1
    return(k)
for i in range(len(array)):
    l.append(add(i))
    s.append(sum(l[i]))
#print(l)
print(max(s))
