"""141. Linked List Cycle (Difficulty: Easy).
https://leetcode.com/problems/linked-list-cycle/

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution141:
    def hasCycle(self, head: ListNode) -> bool:   # O(n) solution
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False

    def hasCycle_2(self, head: ListNode) -> bool:  # O(1) solution
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


linked_node1 = ListNode(3)
linked_node2 = ListNode(2)
linked_node3 = ListNode(0)
linked_node4 = ListNode(-4)
linked_node1.next = linked_node2
linked_node2.next = linked_node3
linked_node3.next = linked_node4
linked_node4.next = linked_node2

linked_node5 = ListNode(1)
linked_node6 = ListNode(2)
linked_node5.next = linked_node6
linked_node6.next = linked_node5

linked_node7 = ListNode(1)

solution = Solution141()
print(solution.hasCycle(linked_node1))
print(solution.hasCycle(linked_node5))
print(solution.hasCycle(linked_node7))

print(solution.hasCycle_2(linked_node1))
print(solution.hasCycle_2(linked_node5))
print(solution.hasCycle_2(linked_node7))
