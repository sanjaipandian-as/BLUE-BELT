class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
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
            newNode.prev = cur

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def reverse(self):
        cur = self.head
        while cur is not None:
            temp = cur.next
            cur.next = cur.prev
            cur.prev = temp

            if temp is None:
                self.head = cur
            cur = temp

ob=LinkedList()
n=int(input())
arr=list(map(int,input().split()))

for i in arr:
    ob.add(i)

ob.reverse()
ob.print()