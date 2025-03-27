class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next=newNode
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            cur=self.head
            while cur is not None:
                print(cur.data,end=" ")
                cur=cur.next
            print()
    def sort(self):
        count=[0,0,0]
        cur=self.head
        while cur is not None:
            count[cur.data]+=1 
            cur=cur.next
        index=0
        cur=self.head
        while cur is not None:
            if count[index]==0:
                index+=1 
            else:
                cur.data=index
                count[index]-= 1 
                cur=cur.next
obj=linkedList()
n=int(input())
a=list(map(int,input().split()))
for i in a:
    obj.add(i)
obj.sort()
obj.print()

input=n=6, arr=0,2,1,2,0,1
        
            