from linked_list_node import LinkedListNode
from linked_list import linkedList

def reverse(head):

    prev, nx = None, None
    curr = head

    while curr:
        nx = curr.next
        curr.next = prev
        prev = curr
        curr = nx
    
    head = prev
    return head
        