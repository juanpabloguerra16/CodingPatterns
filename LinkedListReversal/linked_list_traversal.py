


def linkedListTraversal(head):

    current, nx = head, None
    while current:
        nx = current.next
        current = nx