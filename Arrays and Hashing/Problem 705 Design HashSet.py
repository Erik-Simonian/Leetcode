"""705. Design HashSet (Difficulty: Easy).
https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.
Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

Constraints:
    0 <= key <= 106
    At most 104 calls will be made to add, remove, and contains."""


class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        self.hash_set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        current_node = self.hash_set[key % len(self.hash_set)]
        while current_node.next:
            if current_node.next.key == key:
                return
            current_node = current_node.next
        current_node.next = ListNode(key)

    def remove(self, key: int) -> None:
        current_node = self.hash_set[key % len(self.hash_set)]
        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def contains(self, key: int) -> bool:
        current_node = self.hash_set[key % len(self.hash_set)]
        while current_node.next:
            if current_node.next.key == key:
                return True
            current_node = current_node.next
        return False


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.contains(2))
