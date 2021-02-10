class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# Utility function to print a linked list
def print_list(msg, head):
    print(msg, end=': ')
    ptr = head
    while ptr:
        print(ptr.val, end=" -> ")
        ptr = ptr.next
    print("None")


def flatten(head: 'Node') -> 'Node':
    curr = head

    def progress(curr):
        if curr.next is None and curr.child is None:
            return curr
        while curr.next and curr.child is None:
            curr = curr.next
        if curr.child:
            tmp = curr.next
            curr.next = curr.child
            node = progress(curr)
            node.next = tmp
        else:
            return curr

    progress(curr)
    return head


if __name__ == '__main__':

    # building a LinkedList form the end, begin with child nodes
    head = None
    head2 = None
    head3 = None

    # create the list: 11 -> 12
    for i in reversed(range(10, 12)):
        head3 = Node(i + 1, None, head3, None)

    # print the list
    print_list('last list   ', head3)

    curr = head3

    # finding the eleven-node
    while curr.val != 11:
        curr = curr.next
    eleven_node = curr

    # create the list: 7 -> 8 -> 9 -> 10
    for i in reversed(range(6, 10)):
        head2 = Node(i + 1, None, head2, None)

    print_list('second list ', head2)

    # finding the eight-node
    curr = head2
    while curr.val != 7:
        curr = curr.next
    seven_node = curr
    eight_node = seven_node.next

    # create association between eight-and-eleven nodes
    eight_node.child = eleven_node

    # create the first list
    for i in reversed(range(6)):
        head = Node(i + 1, None, head, None)

    print_list('first list  ', head)

    # finding the third-node, associating it to the seven-node
    curr = head
    while curr.val != 3:
        curr = curr.next
    curr.child = seven_node

    # End Creating the three-lists and associating the child

    # Start the algo-testing
