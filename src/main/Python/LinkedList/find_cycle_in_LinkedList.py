def detect_cycle(head):
    if head.next is None:
        return head
    curr = head
    nodes_set = set()
    while curr:
        if curr not in nodes_set:
            nodes_set.add(curr)
            curr = curr.next
        else:
            return curr

    return None
