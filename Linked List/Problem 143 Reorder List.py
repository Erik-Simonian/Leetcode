"""143. Reorder List (Difficulty: Medium).
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution143:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        previous = slow.next = None
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp

        # merge two halves
        first = head
        second = previous
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


linked_list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
linked_list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution143()
solution.reorderList(linked_list1)
solution.reorderList(linked_list2)