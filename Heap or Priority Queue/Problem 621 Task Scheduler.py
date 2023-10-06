"""621. Task Scheduler (Difficulty: Medium).
https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task.
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time,
the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
    1 <= task.length <= 104
    tasks[i] is upper-case English letter.
    The integer n is in the range [0, 100]."""
import collections
import heapq


class Solution621:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)
        queue = collections.deque()
        time = 0

        while max_heap or queue:
            time += 1
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])

        return time


solution = Solution621()
print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2))
print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))
print(solution.leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2))
