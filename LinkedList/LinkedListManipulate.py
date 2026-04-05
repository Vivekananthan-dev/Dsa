class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None
class LinkesList:
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
    def __str__(self):
        
        values = []
        current = self.head
        while current:
            values.append(str(current.val))
            print(values)
            current = current.next
        return " -> ".join(values) + " -> None"
l = LinkesList()
l.add(1)
l.add(2)
l.add(3)

l1 = l.head

l1 = l1.next
if l1:
    print(l1.val)
else:
    print("None")
print(l.head.val)