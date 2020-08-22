from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        # # Method1. 투포인터
        # if not height:
        #     return 0

        # ret = 0
        # left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]

        # while left<right:
        #     left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        #     #더 높은 쪽을 향해 투포인터 이동
        #     if left_max <= right_max:
        #         ret += left_max - height[left]
        #         left += 1
        #     else:
        #         ret += right_max - height[right]
        #         right -= 1
        
        # return ret

        
        #Method2. Stack 이용
        stack = []
        ret = 0

        for i in range(len(height)):
            #변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                #스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                #이전과의 차이만큼 물높이를 채워넣는다
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                ret += distance * waters

            stack.append(i)
        
        return ret

