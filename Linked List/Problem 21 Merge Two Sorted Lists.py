"""21. Merge Two Sorted Lists (Difficulty: Easy).
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution21:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy_node = ListNode()
        tail = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy_node.next


linked_list1 = ListNode(1, ListNode(2, ListNode(4)))
linked_list2 = ListNode(1, ListNode(3, ListNode(4)))
linked_list3 = ListNode()
linked_list4 = ListNode()
linked_list5 = ListNode()
linked_list6 = ListNode(0)

solution = Solution21()
solution.mergeTwoLists(linked_list1, linked_list2)
solution.mergeTwoLists(linked_list3, linked_list4)
solution.mergeTwoLists(linked_list5, linked_list6)
