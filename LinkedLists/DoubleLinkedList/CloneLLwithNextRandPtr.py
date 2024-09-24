"""
# Clone a linked list with next and random pointer

You are given a special linked list where each node has a next pointer pointing to its next node. 
You are also given some random pointers, where you will be given some pairs denoting two nodes 
a and b i.e. a->random = b (random is a pointer to a random node).

Construct a copy of the given list. The copy should consist of the same number of new nodes, where 
each new node has its value set to the value of its corresponding original node. Both the next and 
random pointer of the new nodes should point to new nodes in the copied list such that the original 
and copied list pointers represent the same list state. None of the pointers in the new list should 
point to nodes in the original list.

For example, if there are two nodes x and y in the original list, where x->random = y, then for the 
corresponding two nodes xnew and ynew in the copied list, xnew->random = ynew.

Return the head of the copied linked list.

NOTE : 
1. If there is any node whose arbitrary pointer is not given then it's by default NULL. 
2. Don't make any changes to the original linked list.
"""
class Node:
    def __init__(self, val=0):
        self.data = val
        self.next = None
        self.random = None

def copyList(head):
    # code here
    d = dict()
    temp = head
    while temp:
        d[temp] = Node(temp.data)
        temp = temp.next
        
    d[None] = None
    temp = head
    
    while temp:
        d[temp].next = d[temp.next]
        d[temp].random = d[temp.random]
        temp = temp.next
    return d[head]
    


def validation(head, res):

    headp = head
    resp = res

    d = {}

    while head and res:
        if head == res:
            return
        if head.data != res.data:
            return

        if head.random:
            if not res.random:
                return

            if head.random.data != res.random.data:
                return

        elif res.random:
            return
        if head not in d:
            d[head] = res
        head = head.next
        res = res.next

    if not head and res:
        return
    elif head and not res:
        return

    head = headp
    res = resp
    while head:
        if head == res:
            return
        if head.random:
            if head.random not in d:
                return
            if d[head.random] != res.random:
                return
        head = head.next
        res = res.next

    return True
    
if __name__ == "__main__":

    # Creating a linked list with a loop
    head = Node(2)
    node2 = Node(4)
    node3 = Node(7)
    node4 = Node(8)
    node5 = Node(9)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    
    head.random = None
    node2.random = head
    node5.random = node2
    node3.random = node5
    node4.random = node3
    
    res = copyList(head)
    
    if validation(head, res):
        print(True)
    else:
        print(False)
    
    
