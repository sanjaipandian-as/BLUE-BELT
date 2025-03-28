class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = newNode

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def duplicate(self):
        cur = self.head
        while cur and cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next
            else:
                cur = cur.next

obj = Linkedlist()
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    obj.add(i)
obj.duplicate()
obj.print()

input (n=6) and arr=(1,1,2,3,3,4)