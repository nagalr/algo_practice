import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # only for Doubly-List
        # self.prev = None

    def __repr__(self):  # 'toString' Impl
        return repr(self.val)


# prints the all Linked-List starting with the head
def print_list(head):
    result = []
    curr = head
    while curr:
        result.append(repr(curr))  # using ListNode 'repr'
        curr = curr.next

    return '[' + ', '.join(result) + ']'


# reveres a List in-place, changes the List
def reverse(head):
    my_head = head
    curr = head
    prev = None
    next = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    my_head = prev
    return my_head


# full-copy of a p by a full-copy of the head,
# all other-items of the List will be fully-copied as-well.
# given 'head' of a List, 'my_head' will be a head of a full-copy
# of the List. (it was checked by me many times)
# changing my_head items will not affect 'head' items
# a full-copy can be done with only one code-line. (plus the import)
head = ListNode(0, None)  # some item
my_head = copy.deepcopy(head)


# testing
Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)

head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = None

print(print_list(head))

print(print_list(reverse(head)))


