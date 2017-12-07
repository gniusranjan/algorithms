### method for determining the no of prime nos in a given set of integers

till= int(input('tell the no upto which u want to find the prime numbers : '))
list=[2,3]

for n in range(4,till):
    test=[]
    for i in list:
        a=n%i
        if a!=0:
            test.append(1)
    if sum(test)==len(list):
        list.append(n)
print(list)