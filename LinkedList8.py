class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_circular_linked_list(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False



head = Node(10)
node2 = Node(12)
node3 = Node(14)
node4 = Node(16)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(is_circular_linked_list(head))


node4.next = None

print(is_circular_linked_list(head))
