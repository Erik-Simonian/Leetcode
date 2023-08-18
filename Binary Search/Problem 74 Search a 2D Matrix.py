"""74. Search a 2D Matrix (Difficulty: Medium).
https://leetcode.com/problems/search-a-2d-matrix/

You are given an m x n integer matrix matrix with the following two properties:
    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
https://assets.leetcode.com/uploads/2020/10/05/mat.jpg

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104"""


class Solution74:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        lower_boundary = 0
        upper_boundary = rows * columns - 1

        while lower_boundary <= upper_boundary:
            mid = (lower_boundary + upper_boundary) // 2
            x = mid // columns
            y = mid % columns

            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                lower_boundary = mid + 1
            else:
                upper_boundary = mid - 1

        return False


solution = Solution74()
print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
print(solution.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13))
