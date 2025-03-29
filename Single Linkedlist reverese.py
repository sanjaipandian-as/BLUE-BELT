class Node:
    def __init__(self, data):  # Fixed constructor name
        self.data = data
        self.next = None  # Changed pointer to next

class LinkedList:
    def __init__(self):  # Fixed constructor name
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            cur = self.head
            while cur.next is not None:  # Fixed pointer
                cur = cur.next
            cur.next = newNode  # Fixed pointer

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=" ")
                cur = cur.next  # Fixed pointer
            print()

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nextNode = cur.next  # Fixed pointer
            cur.next = prev  # Fixed pointer
            prev = cur
            cur = nextNode
        self.head = prev

obj = LinkedList()
n = int(input())  # Number of elements
a = list(map(int, input().split()))  # List input
for i in a:
    obj.add(i)
obj.reverse()
obj.print()

input (n=5) and arr=(1,2,3,4,5)