"""23. Merge k Sorted Lists (Difficulty: Hard).
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = ""
        pointer = self

        while pointer.next:
            result += str(pointer.val)
            pointer = pointer.next
        result += str(pointer.val)

        return result


class Solution23:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            result = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                result.append(self.merge(l1, l2))
            lists = result
        return lists[0]

    def merge(self, l1, l2):
        dummy_node = tail = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return dummy_node.next


list_node1 = ListNode(1, next=ListNode(4, next=ListNode(5)))
list_node2 = ListNode(1, next=ListNode(3, next=ListNode(4)))
list_node3 = ListNode(2, next=ListNode(6))
list_of_lists1 = [list_node1, list_node2, list_node3]

list_of_lists2 = []
solution = Solution23()

list_node4 = ListNode()
list_of_lists3 = [list_node4]
# print(solution.mergeKLists(list_of_lists1))
# print(solution.mergeKLists(list_of_lists2))
# print(solution.mergeKLists(list_of_lists3))
