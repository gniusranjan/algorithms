class node ():

    def __init__(self,value):
        self.value = value
        self.nextnode =None


class linked_list():

    def __init__(self):
        self.head=None

    def add(self,num):
        nod=node(num)
        if self.head==None:
            self.head=nod
        else:
            nod.nextnode=self.head
            self.head=nod

    def print(self):
        #print(self.head)
        ab=self.head
        while(ab != None):
            print(ab.value)
            ab=ab.nextnode

    def reverse(self):
        a= self.head
        w=None
        i=0
        while(a is not None):
            i=i+1
            x=a.nextnode
            a.nextnode=w
            w=a
            a=x
        self.head=w
        print(int(4.5))
l=linked_list()
l.add(9)
l.add(6)
l.add(3)
l.add(5)
l.reverse()
l.print()
