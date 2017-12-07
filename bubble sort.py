
l='doctorbitchtor'

d=dict()
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
ad=d.keys()
k=list(ad)

v=list(d.values())
z=list(zip(k,v))
#z.sort(key=lambda x:(x[1],x[0]))
z.sort()
print(z)