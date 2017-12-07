def co(n):
    ln=list(n)
    till=int(ln[0])+(len(ln)-1)*9+1
    dic=[0]*till
    def su(a):
        l=(list(map(int,list(str(a)))))
        return(sum(l))
    z=0
    for i in range(int(n)+1):
        si=su(i)
        #print(si)
        z=z+sum(dic[:si])
        dic[si]=dic[si]+1
    if z> 10**9+7:
        return(z-10**9-7)
    else:
        return(z)
print(co('58355'))
# 58354 vs 58355