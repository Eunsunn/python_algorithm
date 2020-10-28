import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 최대힙으로 k번째 원소 찾기(1)
        heap = []
        for num in nums:
            heapq.heappush(heap, (-num, num))
        
        for i in range(k-1):
            heapq.heappop(heap)
        return heapq.heappop(heap)[1]


        # 최대힙으로 k번째 원소 찾기 (2)
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        for _ in range(k-1):
            heapq.heappop(heap)
        
        return -heapq.heappop(heap)


        # 최소힙으로 n-k+1번째 원소 찾기: 훨씬 빠르다
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)


        # heapq nlargest 이용
        return heapq.nlargest(k, nums)[-1]


        # 정렬을 이용한 풀이
        nums.sort() # 오름차순
        return nums[-k]

