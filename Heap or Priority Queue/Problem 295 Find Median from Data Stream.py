"""295. Find Median from Data Stream (Difficulty: Hard).
https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far.
    Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?"""
import heapq


class MedianFinder:

    def __init__(self):
        self.small_numbers = []  # max_heap
        self.large_numbers = []  # min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_numbers, -1 * num)

        # check if all numbers in small_numbers are <= than every number in large_numbers
        if self.small_numbers and self.large_numbers and (-1 * self.small_numbers[0]) > self.large_numbers[0]:
            value = -1 * heapq.heappop(self.small_numbers)
            heapq.heappush(self.large_numbers, value)

        # check if the length difference between two heaps is less than 2
        if len(self.small_numbers) > len(self.large_numbers) + 1:
            value = -1 * heapq.heappop(self.small_numbers)
            heapq.heappush(self.large_numbers, value)
        if len(self.large_numbers) > len(self.small_numbers) + 1:
            value = heapq.heappop(self.large_numbers)
            heapq.heappush(self.small_numbers, -1 * value)

    def findMedian(self) -> float:
        if len(self.small_numbers) > len(self.large_numbers):
            return -1 * self.small_numbers[0]
        if len(self.large_numbers) > len(self.small_numbers):
            return self.large_numbers[0]

        return (-1 * self.small_numbers[0] + self.large_numbers[0]) / 2


solution = MedianFinder()
solution.addNum(1)
solution.addNum(2)
print(solution.findMedian())
solution.addNum(3)
print(solution.findMedian())
