import heapq

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val
    

def mergeKList(lists):

    heap = []

    for node in lists:
        if node:
            heapq.heappush(heap,node)

    dummy = Node(0)
    curr = dummy

    while heap:
        node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap,node.next)
        
    return dummy.next
    
def build_linklist(arr):

    dummy = Node(0)
    curr = dummy

    for val in arr:

        curr.next = Node(val)
        curr = curr.next
    
    return dummy.next

def print_list(head):
    res = []

    while head:
        res.append(head.val)
        head = head.next
    return res

Lists = [
    build_linklist([1,4,5]),
    build_linklist([1,3,4]),
    build_linklist([2,6])
]

merge = mergeKList(Lists)

print(print_list(merge))