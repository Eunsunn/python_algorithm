import collections
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # ### 풀이1 - 우선순위큐 모듈 heapq 이용 ###
        # freqs = collections.Counter(nums)
        # freqs_heap = []
        # #힙에 음수로 삽입
        # for i in freqs:
        #     heapq.heappush(freqs_heap, (-freqs[i], i))
        
        # topk = []
        # #k번 만큼 추출
        # for _ in range(k):
        #     topk.append(heapq.heappop(freqs_heap)[1])
        
        # return topk




        ### 풀이2 ###
        return list(zip(*collections.Counter(nums).most_common(k)))[0]