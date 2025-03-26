class Node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
class linkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer=newNode
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            cur=self.head
            while cur is not None:
                print(cur.data,end=" ")
                cur=cur.pointer
            print()
    def sort(self):
        count=[0,0,0]
        cur=self.head
        while cur is not None:
            count[cur.data]+=1 
            cur=cur.pointer
        index=0
        cur=self.head
        while cur is not None:
            if count[index]==0:
                index+=1 
            else:
                cur.data=index
                count[index]-= 1 
                cur=cur.pointer
obj=linkedList()
n=int(input())
a=list(map(int,input().split()))
for i in a:
    obj.add(i)
obj.sort()
obj.print()
        
            