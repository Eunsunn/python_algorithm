from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ## 방법1: 재귀호출
        if len(nums)==0:
            return -1
        if nums[0]>target or nums[-1]<target: 
            return -1    


        half = len(nums) // 2

        if target == nums[half]:
            return half
        elif target < nums[half]:
            return self.search(nums[:half], target)
        else: # target > nums[half]
            ret = self.search(nums[half+1:], target)
            if ret==-1:
                return ret
            else:
                return half + 1 + ret

        ## 방법2: 반복문
        if len(nums)==0:
            return -1
        left, right = 0, len(nums)-1

        while left<=right:
            half = left + (right - left) // 2
            if nums[half]==target:
                return half
            elif nums[half]>target:
                right = half - 1
            else: # nums[half]<target
                left = half + 1
        return -1


        ## 방법3: 이진 검색 모듈
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1


        ## 방법4: 파이썬 index() 메서드 사용
        try:
            return nums.index(target)
        except ValueError:
            return -18