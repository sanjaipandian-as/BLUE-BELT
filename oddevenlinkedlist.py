class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def rearragene_odd_even(self):
        if self.head is None:
            return ("No elements")

        odd=self.head
        even=self.head.next
        even_head=even
        while even and even.next is not None:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=odd.next
        odd.next=even_head

    def print(self):
        if self.head is None:
            print("No elements")
            return
        cur=self.head
        while cur is not None:
            print(cur.data,end=" ")
            cur=cur.next
        print()
obj=Linkedlist()
n=int(input())
if n==0:
    print("No elements")
else:
    arr=list(map(int,input().split()))

    for num in arr:
        obj.add(num)

    obj.rearragene_odd_even()
    obj.print()

fake =input (1,2,3,4,5)
