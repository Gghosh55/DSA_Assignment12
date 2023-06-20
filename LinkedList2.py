class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def hasLoop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(4)
head1.next.next.next = head1.next

result1 = hasLoop(head1)

print(result1)


head2 = Node(1)
head2.next = Node(8)
head2.next.next = Node(3)
head2.next.next.next = Node(4)

result2 = hasLoop(head2)

print(result2)
