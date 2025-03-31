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
        if self.head is None:
            print("")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=" ")
                cur = cur.next
            print()

    def deletealloccurences(self, x):
        while self.head is not None and self.head.data == x:
            self.head = self.head.next

        cur = self.head
        while cur is not None and cur.next is not None:
            if cur.next.data == x:
                cur.next = cur.next.next
            else:
                cur = cur.next

obj = Linkedlist()
n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    obj.add(i)

x = int(input())
obj.deletealloccurences(x)
obj.print()


input (1,2,3,4,5)

fake =input (1,2,3,4,5)
fake2=input(1,2,3,4,5)