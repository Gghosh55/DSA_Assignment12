class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def isPalindrome(head):
    if head is None:
        return True


    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    stack = []
    current = head

    while current != slow:
        stack.append(current.data)
        current = current.next


    if fast:
        slow = slow.next


    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True




head1 = Node('R')
head1.next = Node('A')
head1.next.next = Node('D')
head1.next.next.next = Node('A')
head1.next.next.next.next = Node('R')

result1 = isPalindrome(head1)

print(result1)


head2 = Node('C')
head2.next = Node('O')
head2.next.next = Node('D')
head2.next.next.next = Node('E')

result2 = isPalindrome(head2)

print(result2)
