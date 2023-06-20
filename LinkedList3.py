class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def findNthFromEnd(head, N):
    if head is None or N <= 0:
        return None

    slow = head
    fast = head


    for _ in range(N):
        if fast is None:
            return None
        fast = fast.next


    while fast:
        slow = slow.next
        fast = fast.next


    return slow.data




head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next = Node(7)
head1.next.next.next.next.next.next.next = Node(8)
head1.next.next.next.next.next.next.next.next = Node(9)

result1 = findNthFromEnd(head1, 2)
print(result1)


head2 = Node(10)
head2.next = Node(5)
head2.next.next = Node(100)
head2.next.next.next = Node(5)


result2 = findNthFromEnd(head2, 5)

print(result2)
