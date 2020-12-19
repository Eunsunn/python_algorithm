from typing import List
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # 방법1: Greedy algorithm
        cnt = 0
        if not g or not s:
            return cnt
        
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)

        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                cnt += 1
                g_idx += 1
                s_idx += 1
            else:
                g_idx += 1

        return cnt

        # 방법2: 이진검색
        g.sort()
        s.sort()

        count = 0
        for i in s:
            # 이진검색으로 정렬을 유지하고 들어갈 인덱스 + 1 번째 탐색
            index = bisect.bisect_right(g, i)
            # 쿠키는 한번만 나눠준다
            if index > count:
                count += 1
        
        return count


if __name__ == '__main__':
    g = [1,3,7]
    s = [4,5]
    sol = Solution()
    print(sol.findContentChildren(g,s))