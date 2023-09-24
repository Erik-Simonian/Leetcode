"""40. Combination Sum II (Difficulty: Medium).
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]

Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30"""


class Solution40:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()

        def backtracking(pos, current, total):
            if total == 0:
                result.append(current.copy())
            if total <= 0:
                return

            # Last number. Used to skip duplicate numbers in a sorted list
            previous = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == previous:
                    continue
                current.append(candidates[i])
                backtracking(i + 1, current, total - candidates[i])
                current.pop()
                previous = candidates[i]

        backtracking(0, [], target)
        return result


solution = Solution40()
print(solution.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
print(solution.combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
