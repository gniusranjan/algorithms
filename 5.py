'''
def fun(A):
    d=[]
    for i in range(1,len(A)):
        d.append(A[i]-A[i-1])
    if len(A)<3:
        return(len(A))
    def check(l):
        nonlocal a
        nonlocal s
        for i in range(len(l)):
            #print(a)
            if sum(l[:i+1])==s:
                a=a+1
                check(l[i+1:])
                break
    n=0
    for i in range(len(d)):
        for j in range(i+1,len(d)+1):
            s=sum(d[i:j])
            a=0
            check(d[j:])
            if a>n:
                #print(a,s)
                n=a
    return(n+2)
print(fun([0 ,1, 3 ,4 ,8, 11, 14, 14, 17, 20]))

'''
def alpha(x):
    x.sort(key=lambda a: len(list(a)),reverse=True)
    l=[]
    for i in x:
        l.append(list(i))
    #l.sort(key=lambda a:len(a),reverse=True)
    def sbar(a):
        tf=[]
        for i in range(1,len(a)+1):
            tf.append(a[:i])
        tb=[]
        for i in range(len(a)):
            tb.append(a[i:len(a)])
        t=tf[::-1]+tb[::-1]
        return(t)
    d=dict()
    for i in range(len(x)):
        d[x[i]]=tuple(sbar(l[i]))
    #return(d)

    mc=list(l[0])
    mcs=list(d[x[0]])
    def check(b):
        for i in len(len(mc)):
            if mc[i:i+len(b)]==b:
                return True
        return False
    def lu():
        global mc, mcs,l
        for i in range(1,len(l)):
            if check(l[i]):
                pass
            else:
                for j in range(len(d[x[i]])/2):
                    if d[x[i]][j] in mcs:
                        ik=mcs.index(d[x[i]][j])+1
                        if ik>len(mcs)/2 :
                            mc=mc+l[i][len(l[i])-len(d[x[i]][j]):]
                            mcs=sbar(mc)
                            break
                    elif d[x[i]][-j-1] in mcs:
                        ik=mcs.index(d[x[i]][-j-1])+1
                        if ik<=len(mcs)/2 :
                            mc=l[i][:len(l[i])-len(d[x[i]][-j-1])]+mc
                            mcs=sbar(mc)
                            break

'''




x=['abcdef','aed','donkey','do']
print(alpha(x))

#print(x)



















