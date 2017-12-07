import pandas as pd
orders =pd.read_table('http://bit.ly/chiporders')
#print(orders)
col=['a','b','c','d']
movie=pd.read_table('http://bit.ly/movieusers',sep='|',header=None,names=col)
#print(movie)
e=[]
for i in movie['a']:
    if i>25:
        e.append(True)
    else:
        e.append(False)

len=pd.Series(e)
print(movie[len])
