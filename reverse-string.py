class Solution:
    from typing import List

    # ########### Sol1 ###########
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     #리스트 원본에서 뒤집기
    #     length = len(s)
    #     half = int(len(s)/2)
    #     for i in range(half):
    #         temp = s[i]
    #         s[i] = s[length-1-i]
    #         s[length-1-i] = temp

    # ########### Sol2 ###########
    # # 투포인터를 이용한 swapping
    # def reverseString(self, s: List[str]) -> None:
    #     left, right = 0, len(s)-1
    #     while left < right:
    #         s[left], s[right] = s[right], s[left]
    #         left += 1
    #         right -= 1

    ########### Sol3 ###########
    # python method 이용
    def reverseString(self, s :List[str]) -> None:
        return s.reverse()

