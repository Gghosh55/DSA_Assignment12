class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def deleteMiddle(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next
    slow.next = None

    return head



head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)

result1 = deleteMiddle(head1)

while result1:
    print(result1.data, end=" ")
    result1 = result1.next
print()

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(5)
head2.next.next.next.next.next = Node(1)

result2 = deleteMiddle(head2)

while result2:
    print(result2.data, end=" ")
    result2 = result2.next
print()
