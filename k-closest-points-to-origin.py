from typing import List
import numpy as np
from collections import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # 방법1: list sort
        dist = [int(i[0])**2+int(i[1])**2 for i in points]
        idxs = sorted(range(len(dist)), key=lambda k: dist[k])[:K]
        return np.array(points)[idxs]

        # 방법2: priority queue
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y)) # (우선순위, 값)

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result
