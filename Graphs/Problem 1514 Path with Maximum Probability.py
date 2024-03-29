"""1514. Path with Maximum Probability (Difficulty: Medium).
https://leetcode.com/problems/path-with-maximum-probability/

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list
where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability
of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end
and return its success probability.

If there is no path from start to end, return 0.
Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
https://assets.leetcode.com/uploads/2019/09/20/1558_ex1.png
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end,
one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
https://assets.leetcode.com/uploads/2019/09/20/1558_ex2.png
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
https://assets.leetcode.com/uploads/2019/09/20/1558_ex2.png
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:
    2 <= n <= 10^4
    0 <= start, end < n
    start != end
    0 <= a, b < n
    a != b
    0 <= succProb.length == edges.length <= 2*10^4
    0 <= succProb[i] <= 1
    There is at most one edge between every two nodes."""
import collections
import heapq


class Solution1514:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int,
                       end_node: int) -> float:              # Dijkstra's Algorithm
        adjacency = collections.defaultdict(list)
        for i in range(len(edges)):
            source, distance = edges[i]
            adjacency[source].append([distance, succProb[i]])
            adjacency[distance].append([source, succProb[i]])

        visited = set()
        max_heap = [(-1, start_node)]

        while max_heap:
            probability, node = heapq.heappop(max_heap)
            visited.add(node)

            if node == end_node:
                return probability * -1
            for neighbour, edge_probability in adjacency[node]:
                if neighbour not in visited:
                    heapq.heappush(max_heap, (probability * edge_probability, neighbour))

        return 0


solution = Solution1514()
print(solution.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start_node=0, end_node=2))
print(solution.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start_node=0, end_node=2))
print(solution.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start_node=0, end_node=2))
