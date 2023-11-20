"""207. Course Schedule (Difficulty: Medium).
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique."""


class Solution207:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        hash_map = {i: [] for i in range(numCourses)}
        visited = set()
        for course, prerequisite in prerequisites:
            hash_map[course].append(prerequisite)

        def dfs(crs):
            if crs in visited:
                return False

            if not hash_map[crs]:
                return True

            visited.add(crs)
            for pre in hash_map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            hash_map[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


solution = Solution207()
print(solution.canFinish(numCourses=2, prerequisites=[[1, 0]]))
print(solution.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
