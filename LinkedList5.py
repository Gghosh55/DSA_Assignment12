class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return

    slow = head
    fast = head


    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break


    if slow != fast:
        return


    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next


    fast.next = None


head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(4)
head1.next.next.next = head1.next

detectAndRemoveLoop(head1)


head2 = Node(1)
head2.next = Node(8)
head2.next.next = Node(3)
head2.next.next.next = Node(4)

detectAndRemoveLoop(head2)


head3 = Node(1)
head3.next = Node(2)
head3.next.next = Node(3)
head3.next.next.next = Node(4)
head3.next.next.next.next = Node(5)
head3.next.next.next.next.next = head3.next.next

detectAndRemoveLoop(head3)
