class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):  # 'toString' Impl
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):  # 'toString' Impl, for 'print'
        result = []
        curr = self.head
        while curr:
            result.append(repr(curr))  # using ListNode 'repr'
            curr = curr.next
        return '[' + ', '.join(result) + ']'

    def prepend(self, data=None):
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data, next=None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data, next=None)

    def find(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr

    def remove(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr and prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev  # prev it the new head


# ALL the methods are within the class,
# to remove them, remove the 'self'
# locate them outside the class-scope,
# and test to see if working

# testing
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

a = SinglyLinkedList()
a.append(Node1)
a.append(Node2)
a.append(Node3)
a.append(Node4)
a.append(Node5)

print(a)  # [1,2,3,4,5]
a.reverse()
print(a)  # [5,4,3,2,1]

a.remove(Node2)
print(a)  # [5, 4, 3, 1] - removes Node2

print(type(a))  # <class '__main__.SinglyLinkedList'>

