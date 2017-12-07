a=int(input())
time=[]
order=[]
c=[]
for i in range(a):
    time.append(input().split(' '))
    order.append(int(time[i][1])+int(time[i][0]))
    c.append(time[i][0])
come=sorted(c)
print(time,'\n',order)
dicto=dict(zip(order,time))
order_sort=sorted(order)
wait=0
for x in order_sort:
    if wait >=order_sort:
        wait=wait+dicto[x][1]-dicto[x][0]
    else:
        wait=wait+dicto[x][1]

average=abs(wait/a)

'''
loop for the given time
check for all 

  
    

'''