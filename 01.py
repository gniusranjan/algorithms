import requests
from bs4 import  BeautifulSoup
#from math import factorial
"""
 def trade_spider(max_pages):
     page =1
     iurl = "https://www.snapdeal.com/product/leeco-le2-x526-32gb-rose/673655791557"
     source = requests.get(iurl)
     itext = source.text
     soup = BeautifulSoup(itext)
     for link in soup.findAll('src'):
         print(link.get('href'))

 trade_spider(2)
"""
#print(.5%1)
#r=list(range(1,n+1))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def facto(n,k):
    r = list(range(1, n + 1))
    #k=k-1
    l=[]
    for i in range(1,n-1):
        x=int((k/factorial(n-i))-.00000001)
        y=(k-1)%factorial(n-i)
        k=y
        l.append(r[x])
        del r[x]
        if k==0:
            l.extend(r)
            break
    if n==2:
        y=k-1
    elif n==1:
        return(1)
    l.append(r[y])
    del r[y]
    l.append(r[0])
    print(l)
n=3

#for i in range(1,factorial(n)+1):
facto(4,2)
