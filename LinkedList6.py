class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def skip_delete_linked_list(head, M, N):
    if not head:
        return head


    dummy = ListNode(0)
    dummy.next = head


    current = dummy
    count = 0

    while current.next:

        while count < M and current.next:
            current = current.next
            count += 1

        # Delete N nodes
        for _ in range(N):
            if current.next:
                current.next = current.next.next
            else:
                break

        count = 0

    return dummy.next
# Create the linked list
head = ListNode(1)
current = head

for i in range(2, 11):
    current.next = ListNode(i)
    current = current.next


M = 2
N = 2
result = skip_delete_linked_list(head, M, N)


current = result
while current:
    print(current.val, end=" ")
    current = current.next


