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


def print_list_from_tail(msg, head):
    while head.next:
        head = head.next
    tail = head
    print(msg, end=': ')
    ptr = tail
    while ptr:
        print(ptr.val, end=" -> ")
        ptr = ptr.prev
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
            tmp.prev = curr
            curr.next = curr.child
            curr.child.prev = curr
            node = progress(curr.next)
            node.next = tmp
            tmp.prev = node
            while tmp.next:
                tmp = tmp.next
            return tmp
        else:
            return curr

    progress(curr)
    return head


# Elegant solution using a Stack
def flatten2(head: 'Node') -> 'Node':
    temp = head

    stack = []

    while head:
        if head.child:
            if head.next:
                stack.append(head.next)
            head.next = head.child
            head.next.prev = head
            head.child = None
        elif not head.next and stack:
            head.next = stack.pop()
            head.next.prev = head

        head = head.next

    return temp


if __name__ == '__main__':

    # building a LinkedList form the end, begin with child nodes
    head = None
    head2 = None
    head3 = None

    # create the list: 11 -> 12
    prev = None
    node = Node(0, None, None, None)
    for i in reversed(range(10, 12)):
        head3 = Node(i + 1, None, head3, None)
        node.prev = head3
        node = head3

    # print the list
    print_list('last list   ', head3)

    curr = head3

    # finding the eleven-node
    while curr.val != 11:
        curr = curr.next
    eleven_node = curr

    # create the list: 7 -> 8 -> 9 -> 10
    prev = None
    for i in reversed(range(6, 10)):
        head2 = Node(i + 1, None, head2, None)
        node.prev = head2
        node = head2

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
    prev = None
    for i in reversed(range(6)):
        head = Node(i + 1, None, head, None)
        node.prev = head
        node = head

    print_list('first list  ', head)

    # finding the third-node, associating it to the seven-node
    curr = head
    while curr.val != 3:
        curr = curr.next
    curr.child = seven_node

    # End Creating the three-lists and associating the child

    print('-----------------------')
    # Start the algo-testing
    new_head = flatten2(head)
    print_list('after    ', new_head)
    print_list_from_tail('from tail', new_head)
