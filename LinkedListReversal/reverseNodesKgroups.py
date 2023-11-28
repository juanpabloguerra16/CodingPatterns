from linked_list import linkedList
from linked_list_node import LinkedListNode


def reverse_k_groups(head, k):
  
    dummy = LinkedListNode(0)
    dummy.next = head

    ptr = dummy

    while (ptr != None):
        tracker = ptr
        for i in range(k):
            if tracker == None:
                break

            tracker = tracker.next

        if tracker == None:
            break

        ptr = tracker
        previous, current = reverse_linked_list(ptr.next, k)

        last_node_of_reversed_group = ptr.next
        last_node_of_reversed_group.next = current
        ptr.next = previous
        ptr = last_node_of_reversed_group

    return dummy.next

def reverse_linked_list(head, k):

    previous, current, next = None, head, None

    for _ in range(k):
        next = current.next
        current.next = previous
        previous = current

        current = next

    return previous, current



    return -1
input = [1,2,3,4,5]