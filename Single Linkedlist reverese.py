class Node:
    def _init_(self,data):
        self.data=data
        self.pointer=None
class linkedlist:
    def _init_(self):
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
    def reverse(self):
        prev=None
        cur=self.head
        while cur is not None:
            nextnode=cur.pointer
            cur.pointer=prev
            prev=cur
            cur=nextnode
        self.head=prev
            
obj=linkedlist()
n=int(input())
a=list(map(int,input().split()))
for i in a:
    obj.add(i)
obj.reverse()
obj.print()