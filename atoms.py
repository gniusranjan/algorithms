#n dimentional grid coordinates
rupsa=input(" ").split()
upsa=list(reversed(rupsa))
i=0
t=len(rupsa)
sum=0
for a in upsa:
    j=1
    while(j<(len(rupsa)-i)):
        sum=sum+(2**(t-j-i-1))*int(a)*int(upsa[len(rupsa)-j-i-1])
        j=j+1
    sum=sum+int(a)*int(rupsa[0])
    i=i+1
print(sum)