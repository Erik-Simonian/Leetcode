"""1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree (Difficulty: Hard).
https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1,
and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge
between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges
that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST).
An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge.
On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Example 1:
https://assets.leetcode.com/uploads/2020/06/04/ex1.png
Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:
https://assets.leetcode.com/uploads/2020/06/04/msts.png
Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges,
so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges.
We add them to the second list of the output.

Example 2:
https://assets.leetcode.com/uploads/2020/06/04/ex2.png
Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4
will yield an MST. Therefore all 4 edges are pseudo-critical.

Constraints:
    2 <= n <= 100
    1 <= edges.length <= min(200, n * (n - 1) / 2)
    edges[i].length == 3
    0 <= ai < bi < n
    1 <= weighti <= 1000
    All pairs (ai, bi) are distinct."""


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1, node2):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution1489:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key=lambda e: e[2])
        mst_weight = 0
        union_find = UnionFind(n)
        for v1, v2, w, i in edges:
            if union_find.union(v1, v2):
                mst_weight += w

        critical, pseudo = [], []
        for n1, n2, edge_weight, index in edges:
            weight = 0
            union_find = UnionFind(n)
            for ver1, ver2, wei, ind in edges:
                if index != ind and union_find.union(ver1, ver2):
                    weight += wei
            if max(union_find.rank) != n or weight > mst_weight:
                critical.append(index)
                continue

            union_find = UnionFind(n)
            union_find.union(n1, n2)
            weight = edge_weight
            for v1, v2, w, j, in edges:
                if union_find.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(index)

        return [critical, pseudo]


solution = Solution1489()
print(solution.findCriticalAndPseudoCriticalEdges(n=5, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 2],
                                                              [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]]))
print(solution.findCriticalAndPseudoCriticalEdges(n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]]))
