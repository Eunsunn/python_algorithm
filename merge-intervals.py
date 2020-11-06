from typing import List
from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ########  방법 1  #########
        ls = sorted(intervals, key=lambda x: x[0]) # 오름차순 정렬
        ls = deque(ls)
        ret = []

        if not intervals:
            return ret

        # left=deque[0], right=deque[1]
        left, right = ls.popleft(), None
        while ls:
            right = ls.popleft()
            if left[1] >= right[0]:
                left = [left[0], max(left[1], right[1])]
            else:
                ret.append(left)
                left = right
        if left:
            ret.append(left)

        return ret


        ########  방법 2  #########
        merged = []
        for entry in sorted(intervals, key=lambda x:x[0]):
            if merged and entry[0] <= merged[-1][1]:
                merged [-1][1] = max(merged[-1][1], entry[1])
            else:
                merged += entry, # equal to += [entry]

        return merged
