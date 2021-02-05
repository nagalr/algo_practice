import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # only for Doubly-List
        self.prev = None

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
    """
    Reverse the list in-place.
    Takes O(n) time.
    """
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


# full-copy of a List by a full-copy of the head,
# all other-items of the List will be fully-copied as-well.
# given 'head' of a List, 'my_head' will be a head of a full-copy
# of the List. (it was checked by me many times)
# changing my_head items will not affect 'head' items
# a full-copy can be done with only one code-line. (plus the import)
head = ListNode(0, None)  # some item
my_head = copy.deepcopy(head)
