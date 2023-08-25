"""206. Reverse Linked List (Difficulty: Easy).
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution206:
    def reverseList_iteratively(self, head: ListNode) -> ListNode:
        last = None
        current = head

        while current:
            temp_next = current.next
            current.next = last
            last = current
            current = temp_next
        return last

    def reverseList_recursively(self, head: ListNode) -> ListNode:
        def recursion(current, previous):
            if not current:
                return previous
            else:
                next_node = current.next
                current.next = previous
                return recursion(next_node, current)

        return recursion(head, None)


linked_list_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linked_list_2 = ListNode(1, ListNode(2))
linked_list_3 = ListNode()
solution = Solution206()

solution.reverseList_iteratively(linked_list_1)
solution.reverseList_recursively(linked_list_1)
solution.reverseList_iteratively(linked_list_2)
solution.reverseList_recursively(linked_list_2)
solution.reverseList_iteratively(linked_list_3)
solution.reverseList_recursively(linked_list_3)
