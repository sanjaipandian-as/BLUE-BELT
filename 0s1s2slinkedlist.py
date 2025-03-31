class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
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
        if self.head is  None:
            print("Linked list is empty")
        else:
            cur=self.head
            while cur is not None:
                print(cur.data,end=" ")
                cur=cur.next
            print()
            
    def sort(self):
        if not self.head or not self.head.next:
            return
        low,mid,high=self.head,self.head,self.head
        while high.next:
            high=high.next
        while mid !=high.next:
            if mid.data==0:
                mid.data,low.data=low.data,mid.data
                low=low.next
                mid=mid.next
            elif mid.data==1:
                mid=mid.next
            else:
                mid.data,high.data=high.data,mid.data
                high=self.getprev(high)
        
    def getprev(self,node):
        cur=self.head
        while cur and cur.next !=node:
            cur=cur.next
        return cur
            
obj=Linkedlist()
n=int(input())
arr=list(map(int,input().split()))

for i in arr:
    obj.add(i)

obj.sort()
obj.print()

input (n=5) and arr(1,2,0,1,2,0) and  ()

fake =input (1,2,3,4,5)
fake2=input(1,2,3,4,5)