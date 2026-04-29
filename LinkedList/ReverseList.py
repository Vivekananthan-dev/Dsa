class ListNode:
    
    def __init__(self,val=0):
        self.val = val
        self.next = None
    
class LinkList:

    def __init__(self):
        self.head = None
    
    def add(self,val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def printL(self):
        curr = self.head
        while curr:
            print(curr.val,end=" -> ")
            curr = curr.next
        print("None")



def reverseList(li):
    prev = None
    curr = li
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

val = map(int,input("Enter the values: ").split())
l = LinkList()

for i in val:
    l.add(i)

l.printL()
l.head = reverseList(l.head)
l.printL()

