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
        if not cur:
            print(" ")
            return
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    def sort(self):
        end = None
        while end != self.head:
            cur = self.head
            while cur.next != end:
                nxt = cur.next
                if cur.data > nxt.data:
                    cur.data, nxt.data = nxt.data, cur.data
                cur = cur.next
            end = cur

n = int(input())
arr = list(map(int, input().split()))
obj = Linkedlist()
for i in arr:
    obj.add(i)
obj.sort()
obj.print()


fake =input (1,2,3,4,5)