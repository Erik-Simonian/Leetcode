"""684. Redundant Connection (Difficylty: Medium).
https://leetcode.com/problems/redundant-connection/

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates
that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
return the answer that occurs last in the input.

Example 1:
https://assets.leetcode.com/uploads/2021/05/02/reduntant1-1-graph.jpg
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
https://assets.leetcode.com/uploads/2021/05/02/reduntant1-2-graph.jpg
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

Constraints:
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected."""


class Solution684:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # Union-Find solution
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(node):
            p = parent[node]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(node1, node2):
            p1, p2 = parent[node1], parent[node2]

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


solution = Solution684()
print(solution.findRedundantConnection(edges=[[1, 2], [1, 3], [2, 3]]))
print(solution.findRedundantConnection(edges=[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
