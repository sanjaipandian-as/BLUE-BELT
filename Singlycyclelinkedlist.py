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

    def cyclecheck(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            cur = self.head
            while cur is not None:  # Fixed the incorrect condition
                print(cur.data, end=" ")
                cur = cur.next
        print()

obj=LinkedList()
n=int(input())
arr=list(map(int,input().split()))
target=int(input())

for i in range(len(arr)-1,-1,-1):
    obj.add(arr[i])

if obj.cyclecheck():
    print("True")
else:
    print("False")

fake =input (1,2,3,4,5)