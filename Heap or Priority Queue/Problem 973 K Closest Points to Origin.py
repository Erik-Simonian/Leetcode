"""973. K Closest Points to Origin (Difficulty: Medium).
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
    1 <= k <= points.length <= 104
    -104 <= xi, yi <= 104"""
import heapq


class Solution973:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        hashmap = {}
        min_heap = [(point[0] ** 2) + (point[1] ** 2) for point in points]
        for i in range(len(min_heap)):
            hashmap[min_heap[i]] = points[i]

        heapq.heapify(min_heap)
        while k > 0:
            closest_point = heapq.heappop(min_heap)
            result.append(hashmap[closest_point])
            k -= 1

        return result


solution = Solution973()
print(solution.kClosest(points=[[1, 3], [-2, 2]], k=1))
print(solution.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
