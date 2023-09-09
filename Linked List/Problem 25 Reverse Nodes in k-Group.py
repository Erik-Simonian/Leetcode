"""25. Reverse Nodes in k-Group (Difficulty: Hard).
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?"""


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



class Solution25:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_node = ListNode(0, head)
        group_previous = dummy_node

        while True:
            kth = self.get_kth_node(group_previous, k)
            if not kth:
                break
            group_previous.next = kth
            group_next = kth.next

            # reverse group
            previous_node = group_next
            current_node = head

            while current_node != group_next:
                temp = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = temp

            group_previous = head
            head = group_next

        return dummy_node.next

    def get_kth_node(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current


list_head = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
list_head2 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
solution = Solution25()
print(solution.reverseKGroup(list_head, k=2))
print(solution.reverseKGroup(list_head2, k=3))
