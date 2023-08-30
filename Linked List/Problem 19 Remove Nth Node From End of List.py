"""19. Remove Nth Node From End of List (Difficulty: Medium).
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

Follow up: Could you do this in one pass?"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution19:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next


linked_list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
linked_list2 = ListNode(1)
linked_list3 = ListNode(1, ListNode(2))
solution = Solution19()
solution.removeNthFromEnd(linked_list1, n=2)
solution.removeNthFromEnd(linked_list2, n=1)
solution.removeNthFromEnd(linked_list3, n=1)
