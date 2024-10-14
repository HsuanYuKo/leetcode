import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        sum_num = 0
        for i in range(0, k):
            Max = max_heap[0]
            sum_num += Max
            heapq.heappop(max_heap)
            n = ceil((-1 * Max) / 3)
            heapq.heappush(max_heap, -1 * n)
        return -1 * sum_num
