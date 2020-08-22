from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Method1. Brute Force - 시간초과
        # for idx1 in range(len(nums)-1):
        #     for idx2 in range(idx1+1, len(nums)):
        #         if nums[idx1] + nums[idx2] == target:
        #             return [idx1, idx2]


        # # Method2. in 이용 : (리스트원스 - target)이 존재하는지 검사
        # for idx, val in enumerate(nums):
        #     complement = target - val

        #     if complement in nums[idx+1:]:
        #         return nums.index(val), nums[idx+1:].index(complement)+(idx+1)


        # Method3. (원소-target)이 있는지 딕셔너리에서 조회
        nums_map = {}
        #값을 key로, 인덱스를 value로 저장
        for idx, num in enumerate(nums):
            nums_map[num] = idx

        #(원소-target)이 있는지 딕셔너리에서 조회
        for idx, num in enumerate(nums):
            if target-num in nums_map and idx != nums_map[target-num]: #num+num=target인 경우 제외하기 위해
                return idx, nums_map[target-num]


        # # Method4. 하나의 for문으로 찾기
        # nums_map = {}
        # for idx, num in enumerate(nums):
        #     if target - num in nums_map:
        #         return [nums_map[target-num], idx]
        #     nums_map[num] = idx

        # # cf) 투포인터를 이용해 찾기
        # #단, 원소들을 정렬해야 하기 때문에 idx가 보존안됨 -> 여기서는 사용할 수 없음!
        # left, right = 0, len(nums)-1
        # while not left == right:
        #     #합이 크면 right 포인터를 줄이고
        #     if nums[left] + nums[right] > target:
        #         right -= 1
        #     #합이 작으면 left 포인터를 증가시킨다
        #     elif nums[left] + nums[right] < target:
        #         left += 1
        #     else:
        #         return left, right