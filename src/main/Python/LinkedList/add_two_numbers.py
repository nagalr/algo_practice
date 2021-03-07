# You are given two non-empty linked lists representing two non-negative integer
# s. The digits are stored in reverse order, and each of their nodes contains a si
# ngle digit. Add the two numbers and return the sum as a linked list.
#
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself.
#
#
#  Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
#
#  Example 2:
#
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
#
#  Example 3:
#
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in each linked list is in the range [1, 100].
#  0 <= Node.val <= 9
#  It is guaranteed that the list represents a number that does not have leading
#  zeros.
#
#  Related Topics Linked List Math Recursion
#  👍 11026 👎 2654


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val=val, next=None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val=val, next=None)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # define two running-pointers
        curr, curr2 = l1, l2

        # define two lists to hold the Nodes values
        list1 = []
        list2 = []

        # build the two lists
        while curr or curr2:
            if curr: list1.append(curr.val)
            if curr2: list2.append(curr2.val)

            if curr is not None and curr.next is not None:
                curr = curr.next
            else:
                curr = None

            if curr2 is not None and curr2.next is not None:
                curr2 = curr2.next
            else:
                curr2 = None

        # Reveres the two list-strings
        list1 = list1[::-1]
        list2 = list2[::-1]

        # Minimize the strings
        list1 = ''.join(str(e) for e in list1)
        list2 = ''.join(str(e) for e in list2)

        # Convert the strings into ints
        list1 = int(list1)
        list2 = int(list2)

        # sum the two int values
        list3 = list1 + list2

        # Convert the result into a string
        list3 = str(list3)

        # Creates a new list to include chars of the previous one
        list4 = []

        for i in range(len(list3)):
            list4.append(list3[i])


        sl = SinglyLinkedList()

        while list4:
            sl.append(list4.pop())

        return sl.head

# leetcode submit region end(Prohibit modification and deletion)

# define two Linked-Lists

# first linked-list
Node1 = ListNode(9)
Node2 = ListNode(9)
Node3 = ListNode(9)
Node4 = ListNode(9)
Node5 = ListNode(9)
Node6 = ListNode(9)
Node7 = ListNode(9)
Node8 = ListNode(9)
Node9 = ListNode(9)

head = Node1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7
Node7.next = Node8
Node8.next = Node9
Node9.next = None

# second linked-list
Node11 = ListNode(9)
Node12 = ListNode(9)
Node13 = ListNode(9)
Node14 = ListNode(9)

head2 = Node11
Node11.next = Node12
Node12.next = Node13
Node13.next = Node14
Node14.next = None

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

s1 = Solution()
s1.addTwoNumbers(head, head2)

