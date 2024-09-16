class DoublyLinkedList:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def print_doubly_linked_list(head):
    prev = None
    print('None -> ', end = "")
    while(head != None):
        print(head.data, end=" -> ")
        prev=head
        head=head.right
    print('None')
    print('None <- ', end = "")
    while(prev != None):
        print(prev.data, end=" <- ")
        prev=prev.left
    print('None')
    
    
if __name__ == "__main__":
    head = DoublyLinkedList(90)
    node2 = DoublyLinkedList(80)
    node3 = DoublyLinkedList(75)
    node4 = DoublyLinkedList(70)
    node5 =DoublyLinkedList(79)
    node6 = DoublyLinkedList(69)
    node7 = DoublyLinkedList(65)
    head.left = None
    head.right = node2
    node2.left = head
    node2.right = node3
    node3.left = node2
    node3.right = node4
    node4.left = node3
    node4.right = node5
    node5.left = node4
    node5.right = node6
    node6.left = node5
    node6.right = node7
    node7.left = node6
    node7.right = None
    
    
    
    print("Doubly Linked List: ")
    print_doubly_linked_list(head)
