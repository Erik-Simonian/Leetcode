"""1584. Min Cost to Connect All Points (Difficulty: Medium).
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path between any two points.

Example 1:
https://assets.leetcode.com/uploads/2020/08/26/d.png
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
https://assets.leetcode.com/uploads/2020/08/26/c.png
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
    1 <= points.length <= 1000
    -106 <= xi, yi <= 106
    All pairs (xi, yi) are distinct."""
import heapq


class Solution1584:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = set()
        result = 0
        adjacency_list = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adjacency_list[i].append([distance, j])
                adjacency_list[j].append([distance, i])

        min_heap = [[0, 0]]
        while len(visited) < n:  # Prim's algorithm
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            result += cost
            visited.add(point)
            for nei_cost, nei in adjacency_list[point]:
                if nei not in visited:
                    heapq.heappush(min_heap, [nei_cost, nei])

        return result


solution = Solution1584()
print(solution.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(solution.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
