"""1462. Course Schedule IV (Difficulty: Medium).
https://leetcode.com/problems/course-schedule-iv/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course ai first if you want to take course bi.

- For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.

Prerequisites can also be indirect. If course a is a prerequisite of course b,
and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query,
you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

Example 1:
https://assets.leetcode.com/uploads/2021/05/01/courses4-1-graph.jpg
Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.

Example 2:
Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.

Example 3:
https://assets.leetcode.com/uploads/2021/05/01/courses4-3-graph.jpg
Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

Constraints:
    2 <= numCourses <= 100
    0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
    prerequisites[i].length == 2
    0 <= ai, bi <= n - 1
    ai != bi
    All the pairs [ai, bi] are unique.
    The prerequisites graph has no cycles.
    1 <= queries.length <= 104
    0 <= ui, vi <= n - 1
    ui != vi"""
import collections


class Solution1462:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[
        bool]:
        adjacency = collections.defaultdict(list)
        for prerequisite, course in prerequisites:
            adjacency[course].append(prerequisite)
        result = []

        def dfs(c):
            if c not in prerequisite_map:
                prerequisite_map[c] = set()
                for prereq in adjacency[c]:
                    prerequisite_map[c] |= dfs(prereq)
                prerequisite_map[c].add(c)
            return prerequisite_map[c]

        prerequisite_map = {}
        for crs in range(numCourses):
            dfs(crs)

        for u, v in queries:
            result.append(u in prerequisite_map[v])
        return result


solution = Solution1462()
print(solution.checkIfPrerequisite(numCourses=2, prerequisites=[[1, 0]], queries=[[0, 1], [1, 0]]))
print(solution.checkIfPrerequisite(numCourses=2, prerequisites=[], queries=[[1, 0], [0, 1]]))
print(solution.checkIfPrerequisite(numCourses=3, prerequisites=[[1, 2], [1, 0], [2, 0]], queries=[[1, 0], [1, 2]]))
