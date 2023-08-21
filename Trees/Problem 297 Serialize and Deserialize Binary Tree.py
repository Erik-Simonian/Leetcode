"""297. Serialize and Deserialize Binary Tree (Difficulty: Hard).
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction
on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree.
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 104].
    -1000 <= Node.val <= 1000"""


from binarytree import Node                 # Added binarytree library for better answer visualisation


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:                                                    # DFS algorithm

    def serialize(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append("NULL")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        nodes = data.split(",")
        self.index = 0

        def dfs():
            if nodes[self.index] == "NULL":
                self.index += 1
                return None

            node = Node(int(nodes[self.index]))
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


ser = Codec()
deser = Codec()

tree1 = Node(1)
tree1.left = Node(2)
tree1.right = Node(3)
tree1.right.left = Node(4)
tree1.right.right = Node(5)

tree2 = Node(0)

print(deser.deserialize(ser.serialize(tree1)))
print(deser.deserialize(ser.serialize(tree2)))
