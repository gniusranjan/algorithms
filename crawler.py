
'''
import urllib.request
from bs4 import BeautifulSoup
w = urllib.request.urlopen("https://www.cafecoffeeday.com/cafe-menu/beverages").read()
raita= BeautifulSoup(w)
print(raita.find_all('a'))
for x in raita.find_all('nav'):
    print(x)
'''
inp=input()
a,b=list(map(float,inp.split()))
if a%5==0 and a<b:
    print("{:.2f}".format(b-a-.50))
else:
    print("{:.2f}".format(b))
