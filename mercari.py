# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
# a=input()
#, solution(a)

def par(A):
    al = list(A)
    def check(c):
        for i in range(int(len(c) / 2)):
            if c[i] == c[-(i + 1)]:
                pass
            else:
                return (False)
                break
        return (True)
    n = 0
    a=[]
    s=set()
    def recur(l):
        nonlocal n
        if n >= len(al):
            s.add(tuple(a))
        else:
            for i in range(len(l)):
                t = l[:i + 1]
                if check(t):
                    n = n + len(t)
                    a.append(''.join(t))
                    recur(l[i + 1:])
                    del a[-1]
                    n = n - len(t)
    recur(al)
    ls=list(s)
    ls.sort()
    return (ls)
print(par('efe'))