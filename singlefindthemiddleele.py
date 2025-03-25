class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=" ")
                cur = cur.next
            print()

    def middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

obj = LinkedList()
n=int(input())
arr=list(map(int,input().split()))

for i in arr:
    obj.add(i)

ans=obj.middle()
print(ans.data)
